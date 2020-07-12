from django.urls import path,include
from . import views
from .views import (
    ResumeListView,
    ResumeDetailView,
    ResumeCreateView,
)
urlpatterns = [
    path('', ResumeListView.as_view(), name='resume-home'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('resume/new/', ResumeCreateView.as_view(), name='resume-create'),
]