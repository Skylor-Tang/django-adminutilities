from django.urls import path

from adminutilities.views import CustomFunctionFormView


urlpatterns = [
    path('', CustomFunctionFormView.as_view(), name='customcunction_admin'),
]
