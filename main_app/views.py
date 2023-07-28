from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Food, Cook
from .forms import EatingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def foods_index(request):
  foods = Food.objects.all()
  return render(request, 'foods/index.html', {'foods': foods})

def foods_detail(request, food_id):
   food = Food.objects.get(id=food_id)
   id_list = food.cooks.all().values_list('id')
   cooks_food_doesnt_have = Cook.objects.exclude(id__in=id_list)
   eating_form = EatingForm()
   return render(request, 'foods/detail.html', {'food': food, 'eating_form': eating_form, 'cooks': cooks_food_doesnt_have})

class FoodCreate(CreateView):
   model = Food
   fields = '__all__'
   success_url = ['name', 'origin', 'description']

class FoodUpdate(UpdateView):
   model = Food
   fields = ['origin', 'description']
   success_url = '/foods/'


class FoodDelete(DeleteView):
   model = Food
   success_url = '/foods/'

def add_eating(request, food_id):
  form = EatingForm(request.POST)
  if form.is_valid():
    new_eating = form.save(commit=False)
    new_eating.food_id = food_id
    new_eating.save()
  return redirect('detail', food_id=food_id)

class CookList(ListView):
  model = Cook

class CookDetail(DetailView):
  model = Cook

class CookCreate(CreateView):
  model = Cook
  fields = '__all__'

class CookUpdate(UpdateView):
  model = Cook
  fields = ['name', 'title']

class CookDelete(DeleteView):
  model = Cook
  success_url = '/cooks'

def assoc_cook(request, food_id, cook_id):
  Food.objects.get(id=food_id).cooks.add(cook_id)
  return redirect('detail', food_id=food_id)

def unassoc_cook(request, food_id, cook_id):
  Food.objects.get(id=food_id).cooks.remove(cook_id)
  return redirect('detail', food_id=food_id)