from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def mycv(request):
    template=loader.get_template('show.html')
    return HttpResponse(template.render())
   
