
from __future__ import absolute_import

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect

from braces import views

from .forms import RegistrationForm, LoginForm

class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class SignUpView(
    views.AnonymousRequiredMixin,
    views.FormValidMessageMixin,
    generic.CreateView
):
    form_class = RegistrationForm
    form_valid_message = 'Thanks for signing up!'
    model = User
    template_name = 'accounts/signup.html'


class LoginView(
    views.AnonymousRequiredMixin,
    views.FormValidMessageMixin,
    generic.FormView
):
    form_class = LoginForm
    form_valid_message = "You're logged in!"
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


# class LogOutView(generic.RedirectView):
#     url = reverse_lazy('home')
#
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super(LogOutView, self).get(request, *args, **kwargs)

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You're logged out")
    return HttpResponseRedirect(reverse_lazy('home'))



# from django.shortcuts import render_to_response
# from django.http import HttpResponseRedirect
# from django.contrib import auth
# from django.core.context_processors import csrf
# from forms import MyRegistrationForm
#
# def login(request):
#     c = {}
#     c.update(csrf(request))
#     return render_to_response('login.html', c)
#
# def auth_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#
#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect('/accounts/loggedin')
#     else:
#         return HttpResponseRedirect('/accounts/invalid')
#
# def loggedin(request):
#     return render_to_response('loggedin.html',
#                              {'full_name': request.user.username})
#
# def invalid_login(request):
#     return render_to_response('invalid_login.html')
#
# def logout(request):
#     auth.logout(request)
#     return render_to_response('logout.html')
#
# def register_user(request):
#     if request.method == 'POST':
#         form = MyRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/accounts/register_success')
#
#     args = {}
#     args.update(csrf(request))
#
#     args['form'] = MyRegistrationForm()
#     print args
#     return render_to_response('register.html', args)
#
# def register_success(request):
#     return render_to_response('register_success.html')