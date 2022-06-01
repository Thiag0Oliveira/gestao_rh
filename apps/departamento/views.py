from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from .models import Departamento


class DepartamentoList(ListView):
    model=Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)



class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamento')

class DepartamentoNew(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoNew,self).form_valid(form)