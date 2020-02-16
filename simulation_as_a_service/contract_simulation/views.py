from django.shortcuts import render

from .src.dummyData import *

from .forms import NameForm

def ranSimulation(request):

    multiplier = int(request.POST.get("multiplier"))

    displayData = someData(multiplier)

    returnVal = render(
            request, 
            'contract_simulation/ranSimulation.html', 
            {
                'multiplier': multiplier,
                'displayData': displayData,
            }
        )

    return returnVal

def index(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
    else:
        form = NameForm()

    returnVal = render(
            request, 
            'contract_simulation/simulationHome.html', 
            {'form': form}
        )

    return returnVal
