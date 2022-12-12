from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Portafolio
from django.contrib.auth.models import User


# Create your views here.
class Index(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        object_list = User.objects.all()
        self.context['object_list'] = object_list

        return render(request, self.template_name, self.context)


class PortafolioAdd(LoginRequiredMixin, View):
    template_name = 'portafolio_add.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        self.context = {
            'foto': request.POST['foto'],
            'titulo_project': request.POST['titulo_project'],
            'description': request.POST['description'],
            'tags': request.POST['tags'],
            'url_github': request.POST['url_github']
        }

        print('self.context:', self.context)

        user = User.objects.get(pk=request.user.id)
        new_portafolio = Portafolio(**self.context, id_user=user)
        new_portafolio.save()

        messages.success(
            request, 'Se registró el proyecto satisfactoriamente!!!')

        return redirect('portafolio_add')


class PortafolioView(LoginRequiredMixin, View):
    template_name = 'portafolio.html'
    context = {}

    def get(self, request):
        object_list = Portafolio.objects.filter(id_user=request.user.id)
        self.context['object_list'] = object_list

        return render(request, self.template_name, self.context)


class PortafolioDetail(View):
    template_name = 'portafolio_details.html'
    context = {}

    def get(self, request, id):
        user_item = User.objects.get(id=id)
        object_list = Portafolio.objects.filter(id_user=id)

        self.context['object_list'] = object_list
        self.context['user'] = {
            'first_name': user_item.first_name,
            'last_name': user_item.last_name,
        }

        print('self.context', self.context)

        return render(request, self.template_name, self.context)
