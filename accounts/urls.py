from django.conf.urls import url, include
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^logout/', views.logoutview, name='logout'),
    #url(r'^user/<user>', views.user_detail, name = 'user_detail'),
    #url(r'^user/(?P<userid>[0-9]+)', views.user_detail, name='user_detail'),
]
