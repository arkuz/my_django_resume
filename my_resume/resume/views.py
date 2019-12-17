from django.shortcuts import render
from .models import Resume, MoreContacts, Works, Educations, Skills, SkillsIcon, Courses


def index(request):
    try:
        resume = Resume.objects.get(is_active=True)
    except Resume.DoesNotExist:
        resume = None

    if resume is not None:
        more_contacts = MoreContacts.objects.filter(resume_id=resume.id).filter(is_active=True)
        works = Works.objects.filter(resume_id=resume.id).filter(is_active=True).order_by('-id')
        educations = Educations.objects.filter(resume_id=resume.id).filter(is_active=True).order_by('-id')
        skills = Skills.objects.filter(resume_id=resume.id).filter(is_active=True)
        skills_icon = SkillsIcon.objects.filter(resume_id=resume.id).filter(is_active=True)
        courses = Courses.objects.filter(resume_id=resume.id).filter(is_active=True).order_by('-id')
    else:
        more_contacts = None
        works = None
        educations = None
        skills = None
        skills_icon = None
        courses = None

    context = {
        'resume': resume,
        'more_contacts': more_contacts,
        'works': works,
        'educations': educations,
        'skills': skills,
        'skills_icon': skills_icon,
        'courses': courses,
    }

    return render(request, 'resume/index.html', context=context)

