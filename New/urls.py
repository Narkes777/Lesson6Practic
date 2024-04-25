from . import views
from django.urls import path

urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car_detail'),
    path('cars/create', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),

    path('manufacturers/', views.ManufacturerList.as_view(), name='manufacturers_list'),
    path('manufacturers/<int:pk>', views.ManufacturerDetail.as_view(), name='manufacturers_detail'),
    path('manufacturers/create', views.ManufacturerCreate.as_view(), name='manufacturers_create'),
    path('manufacturers/<int:pk>/update/', views.ManufacturerUpdate.as_view(), name='manufacturers_update'),
    path('manufacturers/<int:pk>/delete/', views.ManufacturerDelete.as_view(), name='manufacturers_delete'),
    
]