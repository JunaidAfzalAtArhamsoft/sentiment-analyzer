from django.urls import path
from . import views

app_name = 'classifier_app'
urlpatterns = [
    path('', views.AnalyzerApi.as_view(), name='analyze'),
]
