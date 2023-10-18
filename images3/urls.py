# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.ImageUploadView.as_view(), name='image_upload'),
]
