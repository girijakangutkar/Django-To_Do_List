from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse, reverse_lazy
from .models import ToDoList, ToDoItem, Status
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'task/about.html')
        
class ListListView(ListView):
    model = ToDoList
    template_name = "task/index.html"
    
    def get_queryset(self):
      return ToDoList.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class ItemListView(ListView):
    model = ToDoItem
    template_name = "task/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class StatusCreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'task/todoitem_form.html'
    model = Status
    fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return
      
      
      
class ListCreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'task/todolist_form.html'
    model = ToDoList
    fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return 


class ItemCreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'task/todoitem_form.html'
    model = ToDoItem
    fields = [
        "todo_list",
        "status",
        "title",
        "description",
        "due_date",
        "published_date",
       
        
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self, **kwargs):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list", "status"] = todo_list
        context["title", "status"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'task/todoitem_form.html'
    model = ToDoItem
    fields = [
        "todo_list",
        "status",
        "title",
        "description",
        "due_date",
        "published_date",
        
    ]

    def get_context_data(self, **kwargs):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list", "status"] = self.object.todo_list
        context["title" , "status"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ListDelete(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'task/todolist_confirm_delete.html'
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")


class ItemDelete(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'task/todoitem_confirm_delete.html'
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context 
       
@login_required
def ToDoList_publish(request,pk):
  post = get_object_or_404(Post,pk=pk)
  post.publish()
  return redirect('todo_list',pk=pk)
  
