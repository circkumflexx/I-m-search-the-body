from django.shortcuts import render
from .models import DeadBody

# Create your views here.


def stranger(request):
    all_bodies = DeadBody.objects.all()
    current_body = 'stranger'
    item = all_bodies[0].random_item()
    return render(request, 'gens/stranger.html', {'all_bodies': all_bodies,
                                                  'current_body': current_body, 'item': item})


def soldier(request):
    all_bodies = DeadBody.objects.all()
    current_body = 'soldier'
    item = all_bodies[1].random_item()
    return render(request, 'gens/stranger.html', {'all_bodies': all_bodies,
                                                  'current_body': current_body, 'item': item})


def trader(request):
    all_bodies = DeadBody.objects.all()
    current_body = 'trader'
    item = all_bodies[2].random_item()
    return render(request, 'gens/stranger.html', {'all_bodies': all_bodies,
                                                  'current_body': current_body, 'item': item})


def bandit(request):
    all_bodies = DeadBody.objects.all()
    current_body = 'bandit'
    item = all_bodies[3].random_item()
    return render(request, 'gens/stranger.html', {'all_bodies': all_bodies,
                                                  'current_body': current_body, 'item': item})


def cultist(request):
    all_bodies = DeadBody.objects.all()
    current_body = 'cultist'
    item = all_bodies[4].random_item()
    return render(request, 'gens/stranger.html', {'all_bodies': all_bodies,
                                                  'current_body': current_body, 'item': item})

def orc(request):
    all_bodies = DeadBody.objects.all()
    current_body = 'orc'
    item = all_bodies[5].random_item()
    return render(request, 'gens/stranger.html', {'all_bodies': all_bodies,
                                                  'current_body': current_body, 'item': item})
