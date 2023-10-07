from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView

from blog.forms import FormPost, SignupForm
from blog.models import Post


# Create your views here.

# Vistas para las páginas principales

class Home(ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/main/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().order_by('-publish_date')


class About(TemplateView):
    template_name = 'blog/main/about.html'


class Contact(TemplateView):
    template_name = 'blog/main/contact.html'


# CRUD de los POSTS

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = FormPost
    template_name = 'blog/crud/create_post.html'
    success_url = 'home'
    login_url = 'login'

    def form_valid(self, form):
        print(form.cleaned_data)
        cleaned_data = form.cleaned_data
        author = get_object_or_404(User, pk=1)
        post = Post(title=cleaned_data['title'],
                    sub_title=cleaned_data['sub_title'],
                    content=cleaned_data['content'],
                    category=cleaned_data['category'],
                    author=author)
        post.save()
        tags = cleaned_data['tags']
        post.tags.set(tags)
        return redirect(self.success_url)


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/crud/post_detail.html'
    context_object_name = 'post'


class SignUp(FormView):
    template_name = 'blog/auth/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'blog/auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
