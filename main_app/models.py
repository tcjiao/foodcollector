from django.db import models
from django.urls import reverse


# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Food(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})
    
class Eating(models.Model):
    date = models.DateField('eating date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
     ordering = ['-date']
