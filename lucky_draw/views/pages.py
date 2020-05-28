from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views


def render_login_page(request):
    if request.user.is_authenticated:
        render_index_page(request=request)

    return redirect('404.html')


def render_index_page(request):
    redirect_location = 'unauthorized.html'
    if request.user.is_authenticated:
        redirect_location = 'lucky_draw/index.html'

    return render(request, redirect_location)


def not_found(request):
    return render(request, '404.html')
