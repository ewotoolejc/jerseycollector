from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Jersey


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

# def jerseys_index(request):
#     return render(request, 'jerseys/index.html')

class JerseyList(ListView):
    model = Jersey

class JerseyDetailView(DetailView):
    model = Jersey

class JerseyCreate(CreateView):
    model = Jersey
    fields = '__all__'


class JerseyUpdate(UpdateView):
  model = Jersey
  fields = '__all__'


class JerseyDelete(DeleteView):
  model = Jersey
  success_url = '/jersey'