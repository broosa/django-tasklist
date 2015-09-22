from django.template import loader, Context, Template
from django.template.response import SimpleTemplateResponse

from django.contrib.auth.decorators import login_required

from tasklist.models import base

@login_required
def site_index_view(request):
    index_template = loader.get_template('index.html')
    
    if "name" in request.GET:
        user_name = request.GET["name"]
    else:
        user_name = "Stranger!"
    context = Context({"user_name": user_name, "task_list": base.objects.all()})
    
    return SimpleTemplateResponse(index_template, context)
