from django.contrib import admin
from task.models import ToDoItem,ToDoList, Status
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(ToDoItem)
admin.site.register(Status)