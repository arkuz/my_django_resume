from django.shortcuts import render
from .models import Resume, MoreContacts, Works


def index(request):
    try:
        resume = Resume.objects.get(is_active=True)
    except Resume.DoesNotExist:
        resume = None

    if resume is not None:
        more_contacts = MoreContacts.objects.filter(resume_id=resume.id).filter(is_active=True)
        works = Works.objects.filter(resume_id=resume.id).filter(is_active=True).order_by('-id')
    else:
        more_contacts = None
        works = None

    context = {
        'resume': resume,
        'more_contacts': more_contacts,
        'works': works
    }

    return render(request, 'resume/index.html', context=context)

