from django.urls import path
from .import views


urlpatterns = [
    
    # Brand
    path('brands/', views.brand_list_create, name='brand_list_create'),
    path('brands/<int:pk>/', views.brand_detail, name='brand_detail'),
    
    # Category
    path('categories/', views.Category, name='category_list_create'),
]
