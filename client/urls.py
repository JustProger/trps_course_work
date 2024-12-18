from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.clients_list, name='list'),
    path('<int:pk>', views.clients_detail, name='detail'),
    path('<int:pk>/delete/', views.clients_delete, name='delete'),
    path('<int:pk>/comment_delete/', views.clients_comment_delete, name='comment_delete'),
    path('<int:pk>/file_delete/', views.clients_file_delete, name='file_delete'),
    path('<int:pk>/edit/', views.clients_edit, name='edit'),
    path('<int:pk>/add-comment', views.clients_detail, name='add_comment'),
    path('<int:pk>/add-file', views.clients_add_file, name='add_file'),
    path('add/', views.clients_add, name='add'),
    path('export/', views.clients_export, name='export'),
]
