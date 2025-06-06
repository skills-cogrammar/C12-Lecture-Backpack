# workout_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from .forms import WorkoutForm

# Create your views here.
def get_all(request):
    workouts = Workout.objects.all()
    context = {
        'workouts': workouts,
        'page_title': 'Workouts'
    }
    return render(request, 'workouts_app/index.html', context)

def get(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts_app/detail.html', {'workout': workout})

def create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        
        if form.is_valid():
            workout = form.save(commit=False)
            workout.save()
            return redirect('show_workouts')
    else:
        form = WorkoutForm()
        
    return render(request, 'workouts_app/workout_form.html', {'form':form})

def update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)

    if (request.method == 'POST'):
        form = WorkoutForm(request.POST, instance=workout)

        if form.is_valid():
            workout = form.save(commit=False)
            workout.save()
            return redirect('show_workouts')
        
    else:
        form = WorkoutForm(instance=workout)

    return render(request, 'workouts_app/workout_form.html', {'form': form})

def delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    workout.delete()
    return redirect('show_workouts')

