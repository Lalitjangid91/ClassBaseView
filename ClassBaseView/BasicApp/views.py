from django.shortcuts import render
from django.views.generic import View,UpdateView,ListView,DetailView,CreateView,DeleteView
from .models import *
from django.urls import reverse_lazy
class Home(View):
    def get(self,request):
        return render(request,'index.html',{'key':'Django'})
class SchoolListView(ListView):
    model=School
class StudentListView(ListView):
    model=Student

class StudentData(ListView):
    model=Student
    template_name='BasicApp/student_data.html'

class SchoolDetailView(DetailView):
    model=School
class SchoolCreate(CreateView):
    model=School
    fields=["name","principal","location"]



class StudentCreate(CreateView):
    model=Student
    fields=['name','age','school']

class SchoolDelete(DeleteView):
    model=School
    success_url=reverse_lazy('school')
class StudentDelete(DeleteView):
    model=Student
    success_url=reverse_lazy('deletestudent')

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
class StudentUpdate(UpdateView):
    model=Student
    fields='__all__'
