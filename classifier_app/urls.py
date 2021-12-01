from django.urls import path
from . import views

app_name = 'classifier_app'
urlpatterns = [
    path('', views.AnalyzerApi.as_view(), name='analyze'),
    path('file/', views.ShowFileOperations.as_view(), name='file_upload'),
    path('file/search/', views.SearchInFile.as_view(), name='file_search'),
    path('file/sentiment/', views.SentimentOfFile.as_view(), name='file_sentiment'),

]
