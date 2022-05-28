from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista, name='lista'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('save_task', views.save_task, name='save_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('details_task/<int:id>', views.details_task, name='details_task'),
]
