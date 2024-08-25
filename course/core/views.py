from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer
from rest_framework import status
from rest_framework.response import Response

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # message for delete and status code successfully deleted
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# CourseInstance Views
class CourseInstanceListView(generics.ListAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseInstanceListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer
    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)
   
   

class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CourseInstanceSerializer
    lookup_field = 'course_id' 

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        if course_id is not None and year is not None and semester is not None:
            return CourseInstance.objects.filter(year=year, semester=semester, course__id=course_id)
        else:
            return CourseInstance.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Course Instance deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    
