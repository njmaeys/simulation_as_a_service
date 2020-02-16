from django.shortcuts import render


def index(request):

    returnVal = render(request, 'simulation_as_a_service/simulationAsAServiceHome.html')

    return returnVal
