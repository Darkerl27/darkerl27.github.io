from django.shortcuts import render,reverse
from django.views import generic
from  .forms import CreateUserForm,UpdateUserForm
from django.urls import reverse_lazy
from .models import customuser
from post.models import News
from users.models import customuser
from django.http import HttpResponseRedirect
# Create your views here.


class CreateUSerView(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'singup.html'
    success_url = reverse_lazy('home')



class UserProfileView(generic.ListView):
    model = News
    template_name = 'profile.html'
    def get_queryset(self):
        return News.objects.filter(author=self.kwargs['pk'])

class UserProfileEditView(generic.UpdateView):
    form_class = UpdateUserForm
    template_name = 'edituser.html'

    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class UserDeleteView(generic.DeleteView):
    model = customuser
    template_name = 'userdelete.html'
    success_url = reverse_lazy('login')