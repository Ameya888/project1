from django.urls import path,include
from  .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('test', views.Testfun,name='test'),
    path('test2',views.Test2fun,name='test2')
   
]