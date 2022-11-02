
from django.urls import path, re_path
from django.views.generic import RedirectView
from Shortner import views
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('', RedirectView.as_view(url='/decompress/')),
    path('decompress/', views.get_form, name='urlform'),
]
