from wagtailsvg.models import Svg
from wagtail.admin.widgets.chooser import BaseChooser


class AdminSvgChooser(BaseChooser):
    """Custom chooser widget for SVG files that includes preview URL."""

    model = Svg
    chooser_modal_url_name = "svg_chooser:choose"
    template_name = "wagtailsvg/widgets/chooser.html"

    def get_value_data_from_instance(self, instance):
        """
        Override to include the preview_url in the widget data.
        """
        data = super().get_value_data_from_instance(instance)
        if instance:
            data["preview_url"] = instance.url
        else:
            data["preview_url"] = None
        return data

    def get_context(self, name, value_data, attrs):
        """
        Override to include preview_url in the template context.
        """
        context = super().get_context(name, value_data, attrs)
        context["preview_url"] = value_data.get("preview_url") if value_data else None
        return context
