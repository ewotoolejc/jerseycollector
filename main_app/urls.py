from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('jerseys/', views.JerseyList.as_view(), name='index'),
    path('jerseys/<int:pk>', views.JerseyDetailView.as_view(), name='details'),
    path('jerseys/create', views.JerseyCreate.as_view(), name='jerseys_create'),
    path('jerseys/<int:pk>/update/', views.JerseyUpdate.as_view(), name='jerseys_update'),
    path('jerseys/<int:pk>/delete/', views.JerseyDelete.as_view(), name='jerseys_delete'),
    path('jerseys/<int:jersey_id>/add_cleaning', views.JerseyCleaning, name='jersey_cleaning'),
    path('jerseys/<int:jersey_id>/assoc_hat/<int:hat_id>/', views.assoc_hat, name='assoc_hat'),
    path('jerseys/<int:jersey_id>/unassoc_hat/<int:hat_id>/', views.unassoc_hat, name='unassoc_hat'),
    path('hats/', views.HatList.as_view(), name='hat_index'),
    path('hats/<int:pk>', views.HatDetailView.as_view(), name='hat_details'),
    path('hats/create', views.HatCreate.as_view(), name='hats_create'),
    path('hats/<int:pk>/update/', views.HatUpdate.as_view(), name='hats_update'),
    path('hats/<int:pk>/delete/', views.HatDelete.as_view(), name='hats_delete'),
]