from wagtail_editor_extensions.conf import get_setting


def get_feature_choices(feature_setting):
    """Gets all features from settings.
    """
    return tuple(get_setting(feature_setting).items())


def get_feature_name(feature_name, name):
    """Creates the feature name for Wagtail.
    """
    feature = '%s_%s' % (feature_name, name)
    return feature


def get_feature_name_upper(feature_name, name):
    """The feature name for Wagtail frontend.
    """
    return get_feature_name(feature_name, name).upper()


def get_feature_name_list(feature_setting, feature_name):
    """Used for rendering to view.
    """
    return [get_feature_name_upper(feature_name, name) for name in get_setting(feature_setting).keys()]
