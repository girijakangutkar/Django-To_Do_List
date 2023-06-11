


from django.contrib import admin
#from django.urls import include
from django.urls import path,include
from django.contrib.auth import views 


urlpatterns = [

    path(r'admin/', admin.site.urls),
    path(r'', include('task.urls')),
    path(r'login/', views.LoginView.as_view(), name='login'),
    path(r'logout/', views.LogoutView.as_view(), name='logout',kwargs={'next_page':'/'}),
]
