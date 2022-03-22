from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView
# from .forms import UserForm


def index(request):
    return render(request, "kanban/index.html")


@login_required
def home(request):
    return render(request, "kanban/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
    return render(request, 'kanban/signup.html', context)



class UserDetailView(DetailView):#モデルのデータを個別に詳細表示するビューを継承
    model = User #templateでは小文字のuserとして取得することができる。
    template_name = "kanban/users/detail.html"
