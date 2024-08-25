from django.urls import path
from . import views

urlpatterns = [
    # Course URLs
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    
    # CourseInstance URLs
    path('getinstances/', views.CourseInstanceListView.as_view(), name='instance-list'),
    path('instances/<int:year>/<int:semester>/', views.CourseInstanceListCreateView.as_view(), name='course-instance-list-create'),
    path('instances/', views.CourseInstanceListCreateView.as_view(), name='course-instance-list-create'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', views.CourseInstanceDetailView.as_view(), name='course-instance-detail'),
]
