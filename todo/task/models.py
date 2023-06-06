from django.db import models
from django.utils import timezone
from django.urls import reverse 
# Create your models here.
from model_utils import Choices 

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
   
class Status(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def get_absolute_url(self):
      return reverse("list", args=[self.id])

    def __str__(self):
      template = '{0.title}'
      return template.format(self)
 
    
    
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    published_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
      self.published_date = timezone.now()
      self.save()

    def get_absolute_url(self):
      return reverse("list", args=[self.id])

    def __str__(self):
      template = '{0.title}'
      return template.format(self)
      
        #return self.title, self.status

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date=models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    
    def publish(self):
      self.published_date = timezone.now()
      self.save()

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )
    """
    def __str__(self):
      template = '{0.title} {0.description} {0.due_date} {0.published_date} {0.todo_list} {0.created_date} {0.status}'
      return template.format(self)
      """
    def __str__(self):
        return f"{self.title}: due {self.due_date}"
     
    class Meta:
        ordering = ["due_date"]




