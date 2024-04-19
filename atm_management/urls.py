from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_atm_sites, name='import_atm_sites'),
    path('import-atm-sites/', views.import_atm_sites, name='import_atm_sites'),
    path('atms/', views.atm_list, name='atm_list'),
    path('atm/<int:pk>/', views.atmview, name='atmview'),
    path('atms/<int:pk>/edit/', views.atmupdate, name='atmupdate'),
    path('atms/<int:pk>/delete/', views.atmdelete, name='atmdelete'),
]