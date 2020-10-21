from django.shortcuts import render


def homePage(request):
    template_name = 'homePage.html'
    return render(request, template_name)