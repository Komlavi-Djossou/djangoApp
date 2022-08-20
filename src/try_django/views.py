from turtle import title
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import ContactForm, CreateUserForm
from blog.models import BlogPost
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    my_title = "Hello There...."
    qs = BlogPost.objects.all()[:5]
    context = {"title":"Welcome To KD Blog", "blog_list": qs}
    return render(request, "home.html", context)
    # template_name = "title.txt"
    # template_obj = get_template(template_name)
    # rendered_string = template_obj.render(context)
    # print(rendered_string)
    # return HttpResponse("<h1>Hello World</h1>")
    # return render(request, "hello_world.html", {"title":rendered_string})
   



def about_page(request):
    # return HttpResponse("<h1>About Us</h1>")
    return render(request, "hello_world.html", {"title":"About"})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, "login.html", context)

def register_page(request):
   form = CreateUserForm()
   if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')


   context = { 'form': form}
   return render(request, "register.html", context)



def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form

    }
    return render(request, "form.html", context)

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)

