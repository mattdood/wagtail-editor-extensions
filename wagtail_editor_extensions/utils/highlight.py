import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from wagtail_editor_extensions.conf import get_setting
from wagtail_editor_extensions.utils.feature import get_feature_name, get_feature_name_upper


def register_highlight_feature(name, highlight, features):
    feature_name = get_feature_name('highlight', name)
    type_ = get_feature_name_upper('highlight', name)
    tag = 'span'
    detection = '%s[style="background-color: %s;"]' % (tag, highlight)

    control = {
        'type': type_,
        'icon': get_setting('ICON'),
        'description': highlight,
        'style': {'background-color': highlight}
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
                            'background-color': highlight
                        }
                    }
                }
            }
        },
    })

    features.default_features.append(feature_name)


def register_all_highlight_features(features):
    for name, highlight in get_setting('HIGHLIGHT').items():
        register_highlight_feature(name, highlight, features)
