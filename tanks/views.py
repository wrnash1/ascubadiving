from django.shortcuts import render
from diveshopmanagement.models import Tank


def tank_list(request):
    tanks = Tank.objects.all()
    return render(request, "tanks/tank_list.html", {"tanks": tanks})


def tank_detail(request, pk):
    tank = Tank.objects.get(pk=pk)
    return render(request, "tanks/tank_detail.html", {"tank": tank})
