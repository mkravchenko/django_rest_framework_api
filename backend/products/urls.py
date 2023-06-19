from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateProductApiView.as_view()),
    path('<int:pk>/', views.ProductDetailsApiView.as_view()),
    path('update/<int:pk>', views.UpdateProductApiView.as_view()),
    path('delete/<int:pk>', views.DeleteProductApiView.as_view()),
]
