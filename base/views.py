from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from django.views.generic.edit import FormView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm, ExitPointForm
import smtplib

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.utils.translation import get_language, activate

class Login(LoginView):
    # model = User
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base')

class RegisterPage(FormView):
    template_name = 'user/register.html'
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

class ExitPointView(LoginRequiredMixin, FormView):
    template_name = 'exitpoint.html'
    form_class = ExitPointForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ExitPointView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('base')

def mail_wysylam(request):
    subject = 'Moj temat'
    message = 'moja wiadomosc'
    send_mail(subject, message, 'project.half.brain@gmail.com', ['project.half.brain@gmail.com'], fail_silently=False)
    return HttpResponse('Udalo sie!')

# def register_confirm_mail(request):
#     EmailMessage

def index(request):
    trans = translate(language='pl')
    projekt = _('hello')
    slowa = _('i looking for flowers')

    # user = request.
    return render(request, 'index.html', {'projekt': projekt, 'trans': trans, 'slowa': slowa})


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = _('how are you')
    finally:
        activate(cur_language)
    return text


