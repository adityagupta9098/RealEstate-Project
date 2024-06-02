
from django.db import connection
from django.shortcuts import render
from RealEstateapp.models import Property
from .import tuple_to_dict
from django.shortcuts import render,redirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from RealEstateapp.serializers import CitiesSerializer, StatesSerializer
from RealEstateapp.models import Cities
from RealEstateapp.models import States

# ========================= State_List ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def State_List(request):
    if request.method == 'GET':
        state_list = States.objects.all()

        state_serializer = StatesSerializer(state_list, many=True)
        return JsonResponse(state_serializer.data, safe=False)
    return JsonResponse({}, safe=False)

#============================ City_List ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def City_List(request):
    if request.method == 'GET':
        city_list = Cities.objects.raw(
            "select * from realestateapp_cities where stateid={0}".format(request.GET['stateid']))

        city_serializer = CitiesSerializer(city_list, many=True)

        return JsonResponse(city_serializer.data, safe=False)
    return JsonResponse({}, safe=False)


