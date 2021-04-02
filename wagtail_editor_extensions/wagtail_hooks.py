from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse, path, include
from django.utils.html import format_html_join, format_html
from django.utils.translation import ugettext as _

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.core import hooks

from wagtail_editor_extensions.conf import get_setting
from wagtail_editor_extensions.utils.colour import register_all_colour_features
from wagtail_editor_extensions.utils.font_size import register_all_font_size_features
from wagtail_editor_extensions.utils.highlight import register_all_highlight_features
from wagtail_editor_extensions.utils.line_space import register_all_line_space_features


@hooks.register('register_admin_urls')
def register_admin_urls():
    """Register the URLs for the forms.
    """
    from wagtail_editor_extensions import urls
    return [
        path('wagtail_editor_extensions/', include((urls, 'wagtail_editor_extensions'))),
    ]


@hooks.register('insert_editor_css')
def editor_css():
    """Add the CSS required for each feature.
    """
    css_files = [
        'colourpicker/css/colourpicker.css',
        'font_size/css/font_size_picker.css',
        'highlight/css/highlight_picker.css',
        'line_space/css/line_space_picker.css',
    ]
    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}">',
        ((static(filename), ) for filename in css_files)
    )
    return css_includes


@hooks.register('insert_editor_js')
def insert_editor_js():
    """Add the JS required for each feature.
    """
    js_files = [
        # We require this file here to make sure it is loaded before the other.
        'wagtailadmin/js/draftail.js',
        'colourpicker/js/colourpicker.js',
        'font_size/js/font_size_picker.js'
        'line_space/js/line_space_picker.js'
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}"></script>',
        ((static(filename), ) for filename in js_files)
    )

    # Modals with URLs for each of the features
    js_includes += format_html(
        "<script>window.chooserUrls.colourChooser = '{0}';</script>",
        reverse('wagtail_editor_extensions:colour_chooser')
    )
    js_includes += format_html(
        "<script>window.chooserUrls.fontsizeChooser = '{0}';</script>",
        reverse('wagtail_editor_extensions:font_size_chooser')
    )
    js_includes += format_html(
        "<script>window.chooserUrls.highlightChooser = '{0}';</script>",
        reverse('wagtail_editor_extensions:highlight_chooser')
    )
    js_includes += format_html(
        "<script>window.chooserUrls.linespaceChooser = '{0}';</script>",
        reverse('wagtail_editor_extensions:line_space_chooser')
    )
    return js_includes


@hooks.register('register_rich_text_features')
def register_textcolour_feature(features):
    """Each of the colour choices is a separate feature.

    These are registered then assigned to the
    "main" feature.
    """
    # register all colour features
    register_all_colour_features(features)

    # register the color picker
    feature_name = 'textcolour'
    type_ = feature_name.upper()

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': _('Text Colour'),
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            control,
            js=['colourpicker/js/chooser.js']
        )
    )

    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def register_textsize_feature(features):
    # register all font size features
    register_all_font_size_features(features)

    # register the font size picker
    feature_name = 'textsize'
    type_ = feature_name.upper()

    control = {
        'type': type_,
        'icon': 'title',
        'description': _('Text Size'),
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            control,
            js=['font_size/js/font_size_chooser.js']
        )
    )

    features.default_features.append(feature_name)

@hooks.register('register_rich_text_features')
def register_highlight_feature(features):
    # register all highlight features
    register_all_font_size_features(features)

    # register the highlight picker
    feature_name = 'texthighlight'
    type_ = feature_name.upper()

    control = {
        'type': type_,
        'icon': 'pick',
        'description': _('Text Highlight'),
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            control,
            js=['highlight/js/highlight_chooser.js']
        )
    )

    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def register_line_space_feature(features):
    # register all line space features
    register_all_font_size_features(features)

    # register the line space picker
    feature_name = 'textlinespace'
    type_ = feature_name.upper()

    control = {
        'type': type_,
        'icon': 'arrows-up-down',
        'description': _('Line Spacing'),
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            control,
            js=['line_space/js/line_space_chooser.js']
        )
    )

    features.default_features.append(feature_name)

