from django.template import loader, Context, Template, RequestContext
from django.template.response import SimpleTemplateResponse

from django.shortcuts import render, redirect

from django.http import Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):

    r_context = {}

    if request.method == "GET" and "next" in request.GET:
        r_context["next"] = request.GET["next"]

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if next in request.POST:
                next_page = request.POST["next"]
                return redirect(next_page)
            else:
                return redirect(details_view)
        else:
            r_context["login_failed"] = True
            r_context["error_message"] = "Invalid username or password. Please try again."

    return render(request, "account/login.html", r_context)

def logout_view(request):
    if not request.user.is_authenticated():
        raise Http404()
    else:
        logout(request)
        return render(request, "account/logout.html")

@login_required
def details_view(request):
    r_context = {}

    r_context["user"] = request.user

    return render(request, "account/details.html", r_context)