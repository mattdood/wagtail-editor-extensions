import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from wagtail_editor_extensions.conf import get_setting
from wagtail_editor_extensions.utils.feature import get_feature_name, get_feature_name_upper


def register_color_feature(name, colour, features):
    """This is called for each feature in settings.

    Each of the dictionary entries is a new
    feature for the editor to display.
    They're created/registered here.
    """
    feature_name = get_feature_name('colour', name)
    type_ = get_feature_name_upper('colour', name)
    tag = 'span'
    detection = '%s[style="color: %s;"]' % (tag, colour)

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': colour,
        'style': {'color': colour}
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {detection: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'style': {
                            'color': colour
                        }
                    }
                }
            }
        },
    })

    features.default_features.append(feature_name)


def register_all_colour_features(features):
    """Dynamically create all features.
    """
    for name, colour in get_setting('COLOURS').items():
        register_color_feature(name, colour, features)
