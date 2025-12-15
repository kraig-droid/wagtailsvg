from wagtailsvg.models import Svg
from wagtail.admin.widgets.chooser import BaseChooser
from wagtail.admin.telepath import Adapter
from wagtail.admin.telepath.widgets import WidgetAdapter
from wagtail.admin.telepath import register
from django.forms import Media


class AdminSvgChooser(BaseChooser):
    """Custom chooser widget for SVG files that includes preview URL."""

    template_name = 'wagtailsvg/widgets/chooser.html'
    chooser_modal_url_name = 'svg_chooser:choose'
    model = Svg

    def get_value_data_from_instance(self, instance):
        """
        Override to include the preview_url in the widget data.
        This allows the JavaScript to display the SVG preview.
        """
        data = super().get_value_data_from_instance(instance)
        if instance:
            data['preview_url'] = instance.url
        else:
            data['preview_url'] = None
        return data

    def get_context(self, name, value_data, attrs):
        """
        Override to include preview_url in the template context.
        """
        context = super().get_context(name, value_data, attrs)
        context["preview_url"] = value_data.get("preview_url") if value_data else None
        return context

    @property
    def media(self):
        return Media(js=['wagtailsvg/js/chooser-widget.js'])


class AdminSvgChooserAdapter(WidgetAdapter):
    """Telepath adapter for the AdminSvgChooser widget."""
    js_constructor = 'wagtailsvg.widgets.AdminSvgChooser'

    def js_args(self, widget):
        return [
            widget.render_html('__NAME__', None, attrs={'id': '__ID__'}),
            widget.id_for_label('__ID__'),
        ]


register(AdminSvgChooserAdapter(), AdminSvgChooser)
