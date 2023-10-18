from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from rest_framework.parsers import (MultiPartParser, FormParser)


# Create your views here.
# views.py



class ImageUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser,FileUploadParser,]
    
    def post(self, request, *args, **kwargs):
        uploaded_file = request.data['file']
        # Create a new UploadedImage instance
        uploaded_image = UploadedImage(image=uploaded_file)
        uploaded_image.save()
        # Get the URL of the uploaded image
        image_url = request.build_absolute_uri(uploaded_image.image.url)
        return Response({'image_url': image_url}, status=status.HTTP_201_CREATED)

