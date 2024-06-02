from django.http import JsonResponse
from django.shortcuts import render
from.models import Property



def Dashboard(request):
    properties = Property.objects.all()
    return render(request, 'Dashboard.html', {'properties': properties})



def filtersubmit(request):
    properties = Property.objects.all()
    if request.GET.get('bedrooms'):
        properties = properties.filter(bedrooms=request.GET.get('bedrooms'))
    if request.GET.get('state'):
        properties = properties.filter(state=request.GET.get('state'))
    if request.GET.get('city'):
        properties = properties.filter(city=request.GET.get('city'))
    if request.GET.get('area'):
        properties = properties.filter(area=request.GET.get('area'))
    return render(request, 'dashboard.html', {'properties': properties})




def like_property(request, id):
    property = Property.objects.get(id=id)
    property.likes += 1
    property.save()
    return JsonResponse({'likes': property.likes})


