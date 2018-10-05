from django.shortcuts import render

def index(request):
    context = {
        'title': "Web Kesekjenan HMIF"
    }
    return render(request, 'frontend/index.html', context)