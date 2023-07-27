from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Food
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
   eating_form = EatingForm()
   return render(request, 'foods/detail.html', {'food': food, 'eating_form': eating_form})

class FoodCreate(CreateView):
   model = Food
   fields = '__all__'
   success_url = '/foods/'

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