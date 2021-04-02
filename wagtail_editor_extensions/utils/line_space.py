import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from wagtail_editor_extensions.conf import get_setting
from wagtail_editor_extensions.utils.feature import get_feature_name, get_feature_name_upper


def register_line_space_feature(name, line_space, features):
    """This is called for each feature in settings.

    Each of the dictionary entries is a new
    feature for the editor to display.
    They're created/registered here.
    """
    feature_name = get_feature_name('line_space', name)
    type_ = get_feature_name_upper('line_space', name)
    tag = 'span'
    detection = '%s[style="line-height: %s;"]' % (tag, line_space)

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': line_space,
        'style': {'line-height': line_space}
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
                            'line-height': line_space
                        }
                    }
                }
            }
        },
    })

    features.default_features.append(feature_name)


def register_all_line_space_features(features):
    """Dynamically create all features.
    """
    for name, line_space in get_setting('LINE_SPACE').items():
        register_line_space_feature(name, line_space, features)
