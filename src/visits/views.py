from django.shortcuts import render


def homepage_view(request):
    # Returns the home.html template
    return render(request, "homepage.html")
