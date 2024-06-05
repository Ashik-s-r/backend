from django.contrib import admin
from django.urls import path,include
from medicine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.hlo,name='home1'),
     path('signup/',views.signup,name='signup'),
      path('login/',views.login1,name='login'),
       path('crea/',views.create,name='create'),
        path('retrieve/',views.read,name='read'),
         path('update/<int:id>/',views.update,name='update1'),
          path('delete/<int:id>',views.delete1,name='delete1'),
          path('search/', views.search, name='search_medicine'),
          path('api/', include('api.urls')),
          

]
