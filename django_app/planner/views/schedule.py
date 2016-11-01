from django.shortcuts import render

__all__ = [
    'add_schedule',
    'index_schedule',
]


def index_schedule(request):
    return render(request, 'planner/index_schedule.html', {})


def add_schedule(request):
    pass
