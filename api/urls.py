from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup_api'),
     path('login', views.login, name='login_api'),
     path('create', views.create_product, name='createproductapi'),
     path('list', views.list_products, name='retrieveproductapi'),
      path('<int:pk>/update', views.update_product, name='updateproductapi'),
      path('<int:pk>/delete', views.delete_product, name='deleteproductapi'),
     path('search/<str:query>/', views.search_data, name='searchdata'),
     path('search/', views.my_model_search, name='my_model_search')
    
]