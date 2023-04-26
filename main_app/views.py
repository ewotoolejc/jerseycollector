from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Jersey, Hat
from .forms import CleaningForm


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

# def jerseys_index(request):
#     return render(request, 'jerseys/index.html')

def JerseyCleaning(request, jersey_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.jersey_id = jersey_id
        new_cleaning.save()
        return redirect('details', pk=jersey_id)

class JerseyList(ListView):
    model = Jersey

class JerseyDetailView(FormMixin, DetailView):
    model = Jersey
    form_class = CleaningForm 
    extra_context={'hats': Hat.objects.all()}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['availhats'] = Hat.objects.exclude(jersey=self.object)
        return context

class JerseyCreate(CreateView):
    model = Jersey
    fields = ['jersey_name', 'team_name', 'sport', 'year', 'description', 'picture']

class JerseyUpdate(UpdateView):
  model = Jersey
  fields = ['jersey_name', 'team_name', 'sport', 'year', 'description', 'picture']

class JerseyDelete(DeleteView):
  model = Jersey
  success_url = '/jersey'

class HatList(ListView):
    model = Hat

class HatDetailView(DetailView):
    model = Hat

class HatCreate(CreateView):
    model = Hat
    fields = '__all__'

class HatUpdate(UpdateView):
  model = Hat
  fields = '__all__'

class HatDelete(DeleteView):
  model = Hat
  success_url = '/hat'

def assoc_hat(request, jersey_id, hat_id):
    Jersey.objects.get(id=jersey_id).hats.add(hat_id)
    return redirect('details', pk=jersey_id)

def unassoc_hat(request, jersey_id, hat_id):
    Jersey.objects.get(id=jersey_id).hats.remove(hat_id)
    return redirect('details', pk=jersey_id)