from django.urls import path
from . import views
urlpatterns = [
    path('', views.receive, name='home'),
    path('about/', views.about_app, name='about'),
    path('delete/<list_id>', views.delete, name = 'delete'),
    path('cross_off/<list_id>', views.cross_off, name = 'cross_off'),
    path('uncross/<list_id>', views.uncross, name = 'uncross'),
    path('edit/<list_id>', views.edit, name = 'edit'),
]