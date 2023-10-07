from django.urls import path
from blog.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('create_post', PostCreate.as_view(), name='create_post'),
    path('post/<pk>', PostDetail.as_view(), name='post'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
