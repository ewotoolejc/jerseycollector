from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Jersey, Hat
from .forms import CleaningForm


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def JerseyCleaning(request, jersey_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.jersey_id = jersey_id
        new_cleaning.save()
        return redirect('details', pk=jersey_id)

class JerseyList(LoginRequiredMixin, ListView):
    model = Jersey
    # testing below after auth is set up! tested in cat and it worked!
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class JerseyDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Jersey
    form_class = CleaningForm 
    extra_context={'hats': Hat.objects.all()}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['availhats'] = Hat.objects.exclude(jersey=self.object)
        return context

class JerseyCreate(LoginRequiredMixin, CreateView):
    model = Jersey
    fields = ['jersey_name', 'team_name', 'sport', 'year', 'description', 'picture']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JerseyUpdate(LoginRequiredMixin, UpdateView):
  model = Jersey
  fields = ['jersey_name', 'team_name', 'sport', 'year', 'description', 'picture']

class JerseyDelete(LoginRequiredMixin, DeleteView):
  model = Jersey
  success_url = '/jersey'

class HatList(LoginRequiredMixin, ListView):
    model = Hat

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class HatDetailView(LoginRequiredMixin, DetailView):
    model = Hat

class HatCreate(LoginRequiredMixin, CreateView):
    model = Hat
    fields = ['name', 'color', 'team_name', 'picture']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HatUpdate(LoginRequiredMixin, UpdateView):
  model = Hat
  fields = ['name', 'color', 'team_name', 'picture']

class HatDelete(LoginRequiredMixin, DeleteView):
  model = Hat
  success_url = '/hat'

@login_required
def assoc_hat(request, jersey_id, hat_id):
    Jersey.objects.get(id=jersey_id).hats.add(hat_id)
    return redirect('details', pk=jersey_id)

@login_required
def unassoc_hat(request, jersey_id, hat_id):
    Jersey.objects.get(id=jersey_id).hats.remove(hat_id)
    return redirect('details', pk=jersey_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)