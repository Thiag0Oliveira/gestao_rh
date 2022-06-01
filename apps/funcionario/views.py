from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from .models import Funcionario


class FuncionarioList(ListView):
    model=Funcionario
    #paginate_by = 100

    def get_queryset(self):

        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')

class FuncionarioNew(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        #split passando ' ' separa o primeiro do segundo nome do usuário, nesse caso buscamos e depois concatenamos
        #username= funcionario.nome.split(' ')[0]+funcionario.nome.split(' ')[1]
        username = funcionario.nome
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNew,self).form_valid(form)