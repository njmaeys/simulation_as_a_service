from django.shortcuts import render

from .src.dummyData import *

from .forms import NameForm

def ranSimulation(request):

    ground = float(request.POST.get("ground"))
    express = float(request.POST.get("express"))
    international = float(request.POST.get("international"))

    displayData = someData(ground, express, international)

    returnVal = render(
            request, 
            'contract_simulation/ranSimulation.html', 
            {
                'ground': ground,
                'express': express,
                'international': international,
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
