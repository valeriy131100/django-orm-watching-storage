from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from math import floor


def format_duration(duration):
    seconds = floor(duration.total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    result = f'{hours}ч {minutes}мин'
    return result


def storage_information_view(request):
    # Программируем здесь

    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(visit.get_duration()),
        } for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
