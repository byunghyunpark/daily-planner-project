from datetime import datetime

from django.utils import dateparse
from django.shortcuts import render, redirect
from planner.forms import ScheduleAddForm
from planner.models import Schedule

__all__ = [
    'add_schedule',
    'index_schedule',
]


def index_schedule(request):
    return render(request, 'planner/index_schedule.html', {})


def add_schedule(request):
    if request.method == "POST":
        name = request.POST['name']
        plan_start = request.POST['plan_start']
        plan_finish = request.POST['plan_finish']
        # 11/03/2016 8:37PM    -> YYYY-MM-DD HH:MM
        print(type(plan_start))
        print(plan_start)

        plan_start = dateparse.parse_datetime(plan_start)
        plan_finish = dateparse.parse_datetime(plan_finish)

        print(type(plan_start))
        print(plan_start)

        # plan_start = datetime.strptime(plan_start, '%m/%d/%Y %H:%Mp')

        Schedule.objects.create(
            name=name,
            plan_start=plan_start,
            plan_finish=plan_finish,
        )
        return redirect('planner:index_schedule')
    else:
        return render(request, 'planner/index_schedule.html', {})
