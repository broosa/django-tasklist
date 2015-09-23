from django.template import loader, Context, Template
from django.template.response import SimpleTemplateResponse

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from tasklist.models import base

def site_index_view(request):
    index_template = loader.get_template('index.html')
    
    if "name" in request.GET:
        user_name = request.GET["name"]
    else:
        user_name = "Stranger!"
    context = Context({"user_name": user_name, "task_list": base.objects.all()})
    
    return render(request, "index.html")
