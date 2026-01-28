from django.urls import path
from .import views

urlpatterns = [
   


    #For adding new task
    path('addtask',views.addtask,name='addtask'),
    #For mark as done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    #For mark as undone
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    #For deleting a task
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
    #For editing task:-
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    
    
]