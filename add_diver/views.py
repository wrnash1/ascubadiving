from django.shortcuts import render


def add_diver(request):
    # Code to handle the admin/add_divers URL goes here
    return render(request, "add_diver.html")
