from django.urls import path
from review import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('data-upload', views.data_upload, name='data-upload' ),
    path('review-rating', views.review_rating, name='review-rating' ),
    path('review-analysis', views.review_analysis, name='review-analysis' ),
]
