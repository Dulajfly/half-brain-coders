from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy

from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegisterForm, ExitPointForm
import smtplib

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail, BadHeaderError

class Login(LoginView):
    # model = User
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        print('user1 ', self.request.POST['email'])
        if user is not None:
            login(self.request, user)
            print('user', user)
            # self._send_mail()
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base')
        return super(RegisterPage, self).get(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('base')

class ExitPointView(FormView):
    template_name = 'exitpoint.html'
    form_class = ExitPointForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ExitPointView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('base')

# def mail_wysylam(request):
#     # print('_sendmail: ', self.request.user)
#     send_mail(
#         subject='Dziękujemy za rejestrację. Half brain spółka w zoo',
#         message='DZIEMKI XD',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=['jakubdulaj@outlook.com'],
#         fail_silently=False
#     )
#     return HttpResponse('Udalo sie!')

def index(request):
    return render(request, 'index.html', {'projekt': 'Projekt'})




