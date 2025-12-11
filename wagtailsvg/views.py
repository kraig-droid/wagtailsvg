from functools import cached_property
from wagtailsvg.models import Svg
from django.utils.translation import gettext_lazy as _
from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail.admin.views.generic.chooser import ChooseView


class SvgChooseView(ChooseView):
    """Custom choose view to include preview_url in response data."""

    def get_chosen_response_data(self, item):
        """Override to include the preview_url in the modal response."""
        response_data = super().get_chosen_response_data(item)
        response_data['preview_url'] = item.url
        return response_data


class SvgChooserViewSet(ChooserViewSet):
    model = Svg
    icon = 'image'
    choose_one_text = _("Choose an SVG")
    choose_another_text = _("Choose another SVG")
    edit_item_text = _("Edit this SVG")
    per_page = 10
    choose_view_class = SvgChooseView

    @cached_property
    def widget_class(self):
        """Use custom widget that includes preview_url."""
        from wagtailsvg.widgets import AdminSvgChooser
        return AdminSvgChooser

    def get_object_list(self, search_term=None, **kwargs):
        """Custom search implementation to filter by title."""
        objects = super().get_object_list(**kwargs)

        if search_term:
            objects = objects.filter(title__icontains=search_term)

        return objects
