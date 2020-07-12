from django.shortcuts import render,redirect
from .models import Resume
from .forms import ResumeForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

# Create your views here.
def index(request):
    context = {
        'resumes': Resume.objects.all()
    }
    return render(request,'index.html',context)

class ResumeListView(ListView):
    model = Resume
    template_name = 'index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'resumes'
    
class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resumedetails.html'


class ResumeCreateView(CreateView):
    model = Resume
    fields = ['name','age','dob','sslc','hslc','cgpa','languages','program','experience','achivements','skils']
    template_name = 'insert.html'
