from . import views
from django.urls import path
app_name = 'task'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:tid>',views.details,name='details'),
    # add task
    path('add', views.add , name="add"),
    # edit task
    path('edit/<int:id>' , views.edit , name="edit") ,
    #delete task
    path('delete/<int:id>' , views.delete , name="delete") , 

]
