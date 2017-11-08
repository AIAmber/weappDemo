from django.conf.urls import url, include
import cmsDemo.views

urlpatterns = [
    url(r'^add_book/$', cmsDemo.views.add_book,),
    url(r'^show_books/$', cmsDemo.views.show_books,),
]