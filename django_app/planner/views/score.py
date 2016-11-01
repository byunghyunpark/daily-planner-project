from itertools import count

from django.shortcuts import render
from django.db.models import Q

from planner.models import Schedule

__all__ = [
    'score',
]

def score(request):
    total_schedule_count = Schedule.objects.all().count()
    complete_schedule = Schedule.objects.filter(
        Q(plan_start__isnull=False) &
        Q(plan_finish__isnull=False) &
        Q(real_start__isnull=False) &
        Q(real_finish__isnull=False)
    )
    complete_schedule_count = len(list(complete_schedule))
    percentage = complete_schedule_count / total_schedule_count
    context = {
        'total': total_schedule_count,
        'complete': complete_schedule_count,
        'percentage': percentage,
    }
    print('전체 일정수: %s 개' % total_schedule_count)
    print('완료 일정수: %s 개' % complete_schedule_count)
    print('완료율: %s' % percentage)
    return render(request, 'planner/count.html', context)