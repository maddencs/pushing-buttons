from django.contrib import admin
from django.conf.urls import include, url

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^push-button$', views.PushButtonView.as_view(), name='push_button'),
    url(r'^button-totals$', views.ButtonTotalsView.as_view(), name='button_totals'),
]
