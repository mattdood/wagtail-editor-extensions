from wagtailcolourpicker.conf import get_setting


def get_feature_choices(feature_setting):
    return tuple(get_setting(feature_setting).items())


def get_feature_name(feature_name, name):
    feature = '%s_%s' % (feature_name, name)
    return feature


def get_feature_name_upper(feature_name, name):
    return get_feature_name(feature_name, name).upper()


def get_feature_name_list(feature_setting, feature_name):
    return [get_feature_name_upper(feature_name, name) for name in get_setting(feature_setting).keys()]
