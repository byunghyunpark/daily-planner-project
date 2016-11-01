from django.shortcuts import render, redirect
from planner.forms import ScheduleAddForm
from planner.models import Schedule

__all__ = [
    'add_schedule',
    'index_schedule',
]


def index_schedule(request):
    form = ScheduleAddForm()
    schedules = Schedule.objects.all()

    context ={
        'form': form,
        'schedules': schedules
    }
    return render(request, 'planner/index_schedule.html', context)


def add_schedule(request):
    if request.method == "POST":
        form = ScheduleAddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('planner:index_schedule')
    else:
        form = ScheduleAddForm()
        return render(request, 'planner/index_schedule.html', {'form': form})

    return render(request, 'planner/index_schedule.html', {'form': form})
