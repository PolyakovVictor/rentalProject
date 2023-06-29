from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from .forms import CreateUserForm


class Register(View):
    template_name = "register.html"

    def get(self, request):
        context = {
            'form': CreateUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("/")
        context = {
            "form": form
        }
        return render(request, self.template_name, context)
