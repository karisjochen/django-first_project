from django.shortcuts import render # render calls the HttpResponse
from django.http import HttpResponse

def test(request):

    display = 'This is the first function'

    return HttpResponse(display)



def help(request):
    display = 'This is the help page!!!'
    tag_dict = {'help_insert':display}
    return render(request,'tapp_kj/second_help.html',context=tag_dict)



    
