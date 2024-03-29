"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from blog.views import (
     blog_post_create_view,
       # I rewrite them here because there anot working in the blog folder 
    #  blog_post_detail_view,
    #  blog_post_delete_view,
    #  blog_post_list_view
     #end here
)
from searches.views import search_view


from .views import (
         home_page,
         about_page,
         contact_page,
         example_page,
         login_page,
         register_page,
)

urlpatterns = [  
    path('', home_page, name='home'),

    # I rewrite them here because there anot working in the blog folder 
    # path('blog/', blog_post_list_view),
    # path('<str:slug>/', blog_post_detail_view),
    # path('<str:slug>/delete/', blog_post_delete_view),
    # end here

    path('blog-new/', blog_post_create_view),
    path('blog/',include('blog.urls')),
    path('search/', search_view),
    path('search/searche/', search_view),
    path('search/search/', search_view),

    # re_path(r'^blog/(?P<slug>\w+)/$',  blog_post_detail_page)
    path('about/', about_page),
    path('login/', login_page, name='login'),
    path('register/', register_page),
    path('example/' , example_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)