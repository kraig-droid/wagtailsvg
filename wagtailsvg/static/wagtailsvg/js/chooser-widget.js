/*
 * Custom chooser widget for SVG files that extends Wagtail's BaseChooser
 * to handle the preview_url field for displaying SVG previews.
 */

(function() {
    'use strict';

    class AdminSvgChooser extends window.wagtail.widgets.ChooserWidget {
        /*
         * Extends Wagtail's ChooserWidget to handle preview_url for SVG previews
         */

        constructor(html, idPattern) {
            super(html, idPattern);
            // Find the preview image element
            this.previewElement = this.chooserElement.querySelector('.preview-url');
        }

        getStateFromHTML() {
            /*
             * Extract the current state from the HTML, including the preview_url
             */
            const state = super.getStateFromHTML();
            if (this.previewElement) {
                state.preview_url = this.previewElement.getAttribute('src');
            }
            return state;
        }

        renderState(newState) {
            /*
             * Update the widget display with new state, including the preview image
             */
            super.renderState(newState);

            // Update the preview image if we have a preview element
            if (this.previewElement && newState && newState.preview_url) {
                this.previewElement.setAttribute('src', newState.preview_url);
            }
        }
    }

    // Register the widget with Wagtail's telepath system
    window.telepath.register('wagtailsvg.widgets.AdminSvgChooser', AdminSvgChooser);
})();
