import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from wagtail_editor_extensions.utils.feature import get_feature_name, get_feature_name_upper,get_setting


def register_font_size_feature(name, size, features):
    """This is called for each feature in settings.

    Each of the dictionary entries is a new
    feature for the editor to display.
    They're created/registered here.
    """
    feature_name = get_feature_name('font_size', name)
    type_ = get_feature_name_upper('font_size', name)
    tag = 'span'
    detection = '%s[style="font-size: %s;"]' % (tag, size)

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': size,
        'style': {'font-size': size}
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
                            'font-size': size
                        }
                    }
                }
            }
        },
    })

    features.default_features.append(feature_name)


def register_all_font_size_features(features):
    """Dynamically create all features.
    """
    for name, size in get_setting('FONT_SIZE'):
        register_font_size_feature(name, size, features)