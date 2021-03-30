from django.urls import path

from wagtailcolourpicker.views import colour_chooser


app_name = 'wagtailcolourpicker'

urlpatterns = [
    path('colour_chooser/', colour_chooser, name='colour_chooser'),
]
