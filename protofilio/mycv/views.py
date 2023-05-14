from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .models import courses
def mycv(request):
    template=loader.get_template('show.html')
    return HttpResponse(template.render())
def list_view(request):
    context={}
    context["database"]=Student.objects.all()
    return render(request, "list_view.html", context)
