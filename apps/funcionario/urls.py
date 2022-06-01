from django.urls import path
from .views import FuncionarioList,FuncionarioEdit,FuncionarioDelete,FuncionarioNew

urlpatterns = [

    path('',FuncionarioList.as_view(),name='list_funcionario'),
    path('novo/',FuncionarioNew.as_view(),name='create_funcionario'),
    path('editar/<int:pk>/',FuncionarioEdit.as_view(),name='update_funcionario'),
    path('deletar/<int:pk>/',FuncionarioDelete.as_view(),name='delete_funcionario')

]
