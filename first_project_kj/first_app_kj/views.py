from django.shortcuts import render
from django.http import HttpResponse

def print_text(request):
    html = '<em>My Second App</em>'
    response = HttpResponse(html)

    return response
