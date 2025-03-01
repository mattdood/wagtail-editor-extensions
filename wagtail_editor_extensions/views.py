from wagtail.admin.modal_workflow import render_modal_workflow

from wagtail_editor_extensions.forms import ColourForm, FontSizeForm
from wagtail_editor_extensions.utils.feature import get_feature_name_list, get_feature_name_upper

def colour_chooser(request):
    if request.method == 'POST':
        form = ColourForm(request.POST)

        if form.is_valid():

            feature_name = ''
            if form.cleaned_data.get('colour'):
                feature_name = get_feature_name_upper('colour', form.cleaned_data.get('colour'))

            all_features = get_feature_name_list('COLOURS', 'colour')

            return render_modal_workflow(
                request, None, None, None,
                json_data={
                    'step': 'colour_chosen',
                    'toggled_feature': feature_name,
                    'all_features': all_features
                }
            )
    else:
        form = ColourForm()

    return render_modal_workflow(
        request, 'colourpicker/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )


def font_size_chooser(request):
    if request.method == 'POST':
        form = FontSizeForm(request.POST)

        if form.is_valid():

            feature_name = ''
            if form.cleaned_data.get('font_size'):
                feature_name = get_feature_name_upper('font_size', form.cleaned_data.get('font_size'))

            all_features = get_feature_name_list('FONT_SIZE', 'font_size')

            return render_modal_workflow(
                request, None, None, None,
                json_data={
                    'step': 'colour_chosen',
                    'toggled_feature': feature_name,
                    'all_features': all_features
                }
            )
    else:
        form = ColourForm()

    return render_modal_workflow(
        request, 'colourpicker/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )
