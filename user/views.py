from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class UserRegisterView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('inicial')

    def test_func(self):
        return self.request.user.is_superuser
    
class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'workers'
