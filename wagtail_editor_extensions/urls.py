from django.urls import path

from wagtail_editor_extensions.views import colour_chooser, font_size_chooser


app_name = 'wagtail_editor_extensions'

urlpatterns = [
    path('colour_chooser/', colour_chooser, name='colour_chooser'),
    path('font_size_chooser/', font_size_chooser, name='font_size_chooser'),
]
