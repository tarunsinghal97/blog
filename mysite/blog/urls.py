from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/',views.blog_list, name="blog_list"),
    url(r'^home/',views.home, name="home"),
    url(r'^register/',views.register, name="register"),
]