from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jerseys/', views.JerseyList.as_view(), name='index'),
    path('jerseys/<int:pk>', views.JerseyDetailView.as_view(), name='details'),
    path('jerseys/create', views.JerseyCreate.as_view(), name='jerseys_create'),
    path('jerseys/<int:pk>/update/', views.JerseyUpdate.as_view(), name='jerseys_update'),
    path('jerseys/<int:pk>/delete/', views.JerseyDelete.as_view(), name='jerseys_delete'),
]