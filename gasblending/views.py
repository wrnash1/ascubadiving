# gasblending/views.py

from django.shortcuts import render


def gas_blending_view(request):
    if request.method == "POST":
        current_o2 = float(request.POST.get("current_o2", 0))
        current_n2 = float(request.POST.get("current_n2", 0))
        oxygen = float(request.POST.get("oxygen", 0))
        nitrogen = float(request.POST.get("nitrogen", 0))
        helium = float(request.POST.get("helium", 0))
        target_ppo2 = float(request.POST.get("target_ppo2", 0))

        # Calculate the PSI values based on the gas percentages and target ppo2
        total_gas_percentage = current_o2 + current_n2
        oxygen_psi = (oxygen / total_gas_percentage) * target_ppo2
        nitrogen_psi = (nitrogen / total_gas_percentage) * target_ppo2
        helium_psi = (helium / total_gas_percentage) * target_ppo2

        return render(
            request,
            "gasblending/results.html",
            {
                "current_o2": current_o2,
                "current_n2": current_n2,
                "oxygen": oxygen,
                "nitrogen": nitrogen,
                "helium": helium,
                "target_ppo2": target_ppo2,
                "oxygen_psi": oxygen_psi,
                "nitrogen_psi": nitrogen_psi,
                "helium_psi": helium_psi,
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
                "nitrogen": 0,
                "helium": 0,
                "target_ppo2": 0,
            },
        )
