from django.shortcuts import render
from .models import Resume


def index(request):
    resume = None
    try:
        resume = Resume.objects.get(is_active=True)
    except Resume.DoesNotExist:
        pass
    print(resume)
    return render(request, 'resume/index.html', context={'resume': resume})

