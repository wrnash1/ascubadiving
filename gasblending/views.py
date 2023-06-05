# gasblending/views.py

from django.shortcuts import render


def gas_blending_view(request):
    if request.method == "POST":
        current_o2 = float(request.POST.get("current_o2", 0))
        current_n2 = float(request.POST.get("current_n2", 0))
        oxygen = float(request.POST.get("oxygen", 0))
        helium = float(request.POST.get("helium", 0))
        target_ppo2 = float(request.POST.get("target_ppo2", 0))

        # Perform gas blending calculations here

        return render(
            request,
            "gasblending/results.html",
            {
                "current_o2": current_o2,
                "current_n2": current_n2,
                "oxygen": oxygen,
                "helium": helium,
                "target_ppo2": target_ppo2,
                # Pass other calculated values to the template context
            },
        )
    else:
        return render(
            request,
            "gasblending/form.html",
            {
                "current_o2": 0,
                "current_n2": 0,
                "oxygen": 0,
                "helium": 0,
                "target_ppo2": 0,
            },
        )
