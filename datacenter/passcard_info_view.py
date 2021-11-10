from typing import List

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard: Passcard = Passcard.objects.get(passcode=passcode)
    visits: List[Visit] = passcard.visit_set.all()
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(),
            'is_strange': visit.is_visit_long()
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
