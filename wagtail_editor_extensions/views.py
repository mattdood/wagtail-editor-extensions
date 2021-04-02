from wagtail.admin.modal_workflow import render_modal_workflow

from wagtail_editor_extensions.forms import ColourForm, FontSizeForm, HighlightForm, LineSpaceForm
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
                    'step': 'font_size_chosen',
                    'toggled_feature': feature_name,
                    'all_features': all_features
                }
            )
    else:
        form = FontSizeForm()

    return render_modal_workflow(
        request, 'font_size/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )


def highlight_chooser(request):
    if request.method == 'POST':
        form = HighlightForm(request.POST)

        if form.is_valid():

            feature_name = ''
            if form.cleaned_data.get('highlight'):
                feature_name = get_feature_name_upper('highlight', form.cleaned_data.get('highlight'))

            all_features = get_feature_name_list('HIGHLIGHT', 'highlight')

            return render_modal_workflow(
                request, None, None, None,
                json_data={
                    'step': 'highlight_chosen',
                    'toggled_feature': feature_name,
                    'all_features': all_features
                }
            )
    else:
        form = HighlightForm()

    return render_modal_workflow(
        request, 'highlight/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )


def line_space_chooser(request):
    if request.method == 'POST':
        form = LineSpaceForm(request.POST)

        if form.is_valid():

            feature_name = ''
            if form.cleaned_data.get('line_space'):
                feature_name = get_feature_name_upper('line_space', form.cleaned_data.get('line_space'))

            all_features = get_feature_name_list('LINE_SPACE', 'line_space')

            return render_modal_workflow(
                request, None, None, None,
                json_data={
                    'step': 'line_space_chosen',
                    'toggled_feature': feature_name,
                    'all_features': all_features
                }
            )
    else:
        form = LineSpaceForm()

    return render_modal_workflow(
        request, 'line_space/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )

