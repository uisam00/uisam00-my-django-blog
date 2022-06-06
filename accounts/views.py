from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationsFormWithEmail
# Create your views here.

class SignUpView(generic.CreateView):
	form_class = UserCreationsFormWithEmail
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'
