from django.http import HttpResponse
from django.shortcuts import render

from apps.investigator.models import Investigative
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def main(request, investigator_id):
    try:
        investigator = Investigative.objects.get(id=investigator_id)
        skills = investigator.skill
        arts = skills.arts
        characteristics = investigator.characteristics

        context = {
            'investigator': investigator,
            'skills': skills,
            'arts': arts,
            'characteristics': characteristics,
            'player': request.user
        }
        return render(request, 'investigators/investigator.html', context)

    except ObjectDoesNotExist:
        return HttpResponse("Объект не сушествует")

    except MultipleObjectsReturned:
        return HttpResponse("Найдено более одного объекта")
