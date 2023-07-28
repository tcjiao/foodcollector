from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('foods/', views.foods_index, name='index'),
    path('foods/<int:food_id>', views.foods_detail, name='detail'),
    path('foods/create/>', views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
    path('foods/<int:food_id>/add_eating/', views.add_eating, name='add_eating'),
    path('foods/<int:food_id>/assoc_cook/<int:cook_id>/', views.assoc_cook, name='assoc_cook'),
    path('foods/<int:food_id>/unassoc_cook/<int:cook_id>/', views.unassoc_cook, name='unassoc_cook'),
    path('cooks/', views.CookList.as_view(), name='cooks_index'),
    path('cooks/<int:pk>/', views.CookDetail.as_view(), name='cooks_detail'),
    path('cooks/create/', views.CookCreate.as_view(), name='cooks_create'),
    path('cooks/<int:pk>/update/', views.CookUpdate.as_view(), name='cooks_update'),
    path('cooks/<int:pk>/delete/', views.CookDelete.as_view(), name='cooks_delete'),
]