from django.shortcuts import render

from .src.dummyData import *


def index(request):

    context = {
            'people': someData(),
        }

    returnVal = render(
            request, 
            'contract_simulation/simulationHome.html', 
            context
        )

    return returnVal
