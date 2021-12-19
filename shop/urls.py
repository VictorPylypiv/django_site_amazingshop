# from django.conf.urls import url
from . import views
# from django.contrib import admin
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('a/', views.index),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_filtered'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('register/', views.RegisterFormView.as_view()),
    # path('login/', views.LoginFormView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view()),
    # path('shop/', List.as_view(), name='list-view'),
]
