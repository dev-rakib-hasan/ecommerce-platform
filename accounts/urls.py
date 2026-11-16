from django.urls import path
from .import views


urlpatterns = [
    
    # Brand
    path('brands/', views.brand_list_create, name='brand_list_create'),
    path('brands/<int:pk>/', views.brand_detail, name='brand_detail'),
    
    # Category
    path('categories/', views.category_list_create, name='category_list_create'),
    path('categories/<int:pk>/', views.category_detail, name= 'category_detail'),
    
    # Product
    path('products/', views.product_list_create, name='product_list_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail')
]
