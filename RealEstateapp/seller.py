
from django.db import connection

from RealEstateapp.models import Property, User
from .import tuple_to_dict
from django.shortcuts import render,redirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from RealEstateapp.serializers import PropertySerializer




@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def PropertiesInterface(request):
    return render(request,"Add_Properties.html",{})

@xframe_options_exempt
def DisplayAllProperty(request):
    return render(request,"DisplayAllProperty.html",{})

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def PropertySubmit(request):
   if request.method == 'POST':
      
      property_serializer = PropertySerializer(data=request.data)
      if property_serializer.is_valid():
        property_serializer.save()
        return render(request,"Add_Properties.html",{"message":"Record Submitted Successfully"})
     
      
      return render(request,"Add_Properties.html",{"message":"Fail to Submit Record"})
   
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Property_List(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        q = "select P.*,(select S.statename from realestateapp_states S where S.stateid=P.state) as statename,(select C.cityname from realestateapp_cities C where C.cityid=P.city) as cityname from realestateapp_property P"
        cursor.execute(q)
        print(q)
        data=tuple_to_dict.ParseToDictAll(cursor)
        return JsonResponse(data, safe=False)
    return JsonResponse({}, safe=False)


#============================ Property_List_BY_ID ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Property_List_By_Id(request):
   if request.method=='GET':
    propertyid=request.GET['propertyid']
    cursor=connection.cursor() 
    q="select P.*,(select S.statename from realestateapp_states S where S.stateid=P.state) as statename,(select C.cityname from realestateapp_cities C where C.cityid=P.city) as cityname from realestateapp_property P where P.id={0}".format(propertyid)
    
    print(q)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['created_at']=str(data['created_at'])

    if(data['role']=='Buyer'):buyer=True 
    else:seller=False
    
    if(data['role']=='Seller'):seller=True 
    else:buyer=False
    
    return render(request,"Property_By_Id.html",{'record':data,'B_role':buyer,'S_role':seller})
  
   return JsonResponse({},safe=False)  

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Property_Update_Delete(request):
    if request.method == 'GET':
        btn=request.GET['btn']
        if (btn=='Edit'):
            property=Property.objects.get(pk=request.GET['id'])
         
            property.property_name = request.GET['property_name']
            property.description  =  request.GET['description']
            property.area_sq_feet  =  request.GET['area_sq_feet']
            property.num_bedrooms  =  request.GET['num_bedrooms']
            property.num_bathrooms  =  request.GET['num_bathrooms']
            property.hospitals_nearby=request.GET['hospitals_nearby']
            property.colleges_nearby  =  request.GET['colleges_nearby']
            property.created_at  =  request.GET['created_at']
            property.seller_name  =  request.GET['seller_name']
            property.image  =  request.GET['image']
            property.address=request.GET['address']
            property.state=request.GET['state']
            property.city=request.GET['city']
           
            property.save()

        else:
             manager= Property.objects.get(pk=request.GET['id'])
             manager.delete()
    return redirect('/api/displayallproperty') 

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Property_Display_Picture(request):
     if request.method=='GET':
      return render(request,"Property_Picture.html",{"id":request.GET['propertyid'],"property_name":request.GET['property_name'],'image':request.GET['image']})
      
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def UpdatePropertyImage(request):
    
  if request.method == 'POST':
     property=Property.objects.get(pk=request.POST['id']) 
     property.image = request.FILES['image']
     property.save()
     return redirect('/api/displayallproperty')
  


def Seller_Detail(request, pk):
    seller = User.objects.get(pk=pk)
    return render(request, 'seller_detail.html', {'seller': seller})



def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        seller = property.seller_name
        return redirect('seller_detail.html', {'seller' : seller})
    return render(request, 'property_detail.html', {'property': property})



