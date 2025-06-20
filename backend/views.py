from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'About_us.html')

def contacts(request):
    return render(request, 'contacts.html')

def events(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def leadership(request):
    return render(request, 'leadership.html')

def membership(request):
    return render(request, 'membership.html')

def news(request):
    return render(request, 'news.html')
