from rest_framework.response import Response
from api import models, serializers
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    DestroyAPIView 
)

# Create your views here.

class StudentListView(ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class = serializers.StudentSerializers

class StudentDetailsView(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class =  serializers.StudentSerializers

class StudentDeleteView(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializers
