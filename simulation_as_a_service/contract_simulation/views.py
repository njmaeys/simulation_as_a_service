from django.shortcuts import render

from .src.dummyData import *


def index(request):

    returnVal = render(
            request, 
            'contract_simulation/simulationHome.html', 
        )

    return returnVal
