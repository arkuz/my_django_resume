from django.shortcuts import render
from .models import Resume, MoreContacts


def index(request):
    try:
        resume = Resume.objects.get(is_active=True)
    except Resume.DoesNotExist:
        resume = None

    if resume is not None:
        more_contacts = MoreContacts.objects.filter(resume_id=resume.id).filter(is_active=True)
    else:
        more_contacts = None

    context = {
        'resume': resume,
        'more_contacts': more_contacts,
    }

    return render(request, 'resume/index.html', context=context)

