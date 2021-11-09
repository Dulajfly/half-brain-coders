from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, force_str

from django.views.generic.edit import FormView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, ExitPointForm
import smtplib

from best_project import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .tokens import account_activation_token
from django.contrib.auth.models import User


class Login(LoginView):
    # model = User
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base')


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64)).encode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Dziemki Za potwierdzenie maila XD')
    else:
        return HttpResponse('Invalid link')


# Neovo123!
class RegisterPage(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        # print('user1 ', self.request.POST['email'])
        if user is not None:
            user.is_active = False
            user.save()
            # login(self.request, user)
            self.send_email_confirmation(user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base')
        return super(RegisterPage, self).get(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('base')

    def send_email_confirmation(self, user):
        template = render_to_string(
            'email.html',
            {'username': self.request.user.username,
             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
             'token': account_activation_token.make_token(user),
             })
        email = EmailMessage(
            'Find Ur Exit - Activate your account',
            template,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.fail_silently = False
        email.send()


class ExitPointView(LoginRequiredMixin, FormView):
    template_name = 'exitpoint.html'
    form_class = ExitPointForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ExitPointView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('base')


# def mail_wysylam(request):
#     subject = 'Moj temat'
#     message = 'moja wiadomosc'
#     send_mail(subject, message, 'project.half.brain@gmail.com', ['project.half.brain@gmail.com'], fail_silently=False)
#     return HttpResponse('Udalo sie!')

# def send_email_confirmation(request):
#     template = render_to_string(
#         'email.html',
#         {'username': request.user.username,
#          'uid': urlsafe_base64_encode(force_bytes(request.user.pk)).decode(),
#          'token': account_activation_token.make_token(request.user),
#          })
#     email = EmailMessage(
#         'Find Ur Exit - Activate your account',
#         template,
#         settings.EMAIL_HOST_USER,
#         [request.user.email],
#     )
#     email.fail_silently=False
#     email.send()
#     print('Confirm your email address')
#
# def activate_account(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Dziemki Za potwierdzenie maila XD')
#     else:
#         return HttpResponse('Invalid link')

@login_required()
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
