from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail_editor_extensions.utils.feature import get_feature_choices


class ColourRadioSelect(forms.widgets.RadioSelect):
    option_template_name = 'colourpicker/forms/widgets/colour_option.html'


class FontSizeRadioSelect(forms.widgets.RadioSelect):
    option_template_name = 'font_size/forms/widgets/font_size_option.html'


class HighlightRadioSelect(forms.widgets.RadioSelect):
    option_template_name = 'highlight/forms/widgets/highlightoption.html'


class ColourForm(forms.Form):
    colour = forms.ChoiceField(
        label=_("Colours"),
        choices=get_feature_choices('COLOURS'),
        widget=ColourRadioSelect,
        required=False
    )


class FontSizeForm(forms.Form):
    font_size = forms.ChoiceField(
        label=_("Font size"),
        choices=get_feature_choices('FONT_SIZE'),
        widget=FontSizeRadioSelect,
        required=False
    )

class HighlightForm(forms.Form):
    font_size = forms.ChoiceField(
        label=_("Font size"),
        choices=get_feature_choices('FONT_SIZE'),
        widget=FontSizeRadioSelect,
        required=False
    )
