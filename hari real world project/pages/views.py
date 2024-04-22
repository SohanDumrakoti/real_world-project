from django.shortcuts import render


# Create your views here.

def home_page(request):
    context = {
        'activate_home': 'active'
    }

    return render(request, 'pages/home.html', context)


def service_page(request):
    context = {
        'activate_service': 'active'
    }

    return render(request, 'pages/services.html', context)


def about_page(request):
    context = {
        'activate_about': 'active'
    }

    return render(request, 'pages/about.html', context)
