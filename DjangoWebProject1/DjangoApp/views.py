from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, Django. This is Hanbing speaking!")

from datetime import datetime
#def index(request):
#    now = datetime.now()
#
#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"
#
#    return HttpResponse(html_content)

def index(request):
    now = datetime.now()

    return render(
        request,
        "DjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "DjangoApp/about.html",
        {
            'title' : "About DjangoApp",
            'content' : "Example app page for Django."
        }
    )