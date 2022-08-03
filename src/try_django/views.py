from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Hello There...."
    context = { "title": "my_title"}
    if request.user.is_authenticated:
        context = {"title":my_title, "myList": [1,2,3,4]}
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

def contact_page(request):
    return HttpResponse("<h1>Contact Us</h1>")

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)