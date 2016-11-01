from django.shortcuts import redirect, render

from planner.forms import ScheduleAddForm

__all__ = [
    'add_schedule',
]

def add_schedule(request):
    if request.method == "POST":
        form = ScheduleAddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('planner:index_schedule')
    else:
        form = ScheduleAddForm()
        return render(request, 'planner/add_schedule.html', {'form': form})

    return render(request, 'planner/add_schedule.html', {'form': form})
