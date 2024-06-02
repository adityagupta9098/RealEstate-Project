from django.db import connection
from .import tuple_to_dict
from django.shortcuts import render,redirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
# from .import tuple_to_dict
from django.http.response import JsonResponse

from RealEstateapp.serializers import UserSerializer

@api_view(['GET', 'POST', 'DELETE'])
def Login(request):
    return render(request, "Login.html", {})



def Buyer_Dashboard(request): 
  try:  
    buyer=request.session['BUYER']
    print("Session",BuyerDashboard)
    return render(request, "BuyerDashboard.html", {'user':buyer})
  except:
    return render(request, "Login.html", {})


@api_view(['GET', 'POST', 'DELETE'])
def Register(request):
    return render(request, "Registration.html", {})








@api_view(['GET','POST','DELETE'])
def Registration_submit(request):
   if request.method == 'POST':
      
      user_serializer = UserSerializer(data=request.data)
      if user_serializer.is_valid():
        user_serializer.save()
        return render(request,"Registration.html",{"message":"Registration Successful"})
     
      
      return render(request,"Registration.html",{"message":"Registration Unsuccessful"})
   


def BuyerDashboard(request):
  try:  
    buyer = request.session['BUYER']
    print("Session",buyer)
    return render(request, "Buyer_Dashboard.html", {'buyer':buyer})
  except:
    return render(request, "Login.html", {})

def SellerDashboard(request):
  try:  
    seller = request.session['SELLER']
    print("Session",seller)
    return render(request, "Seller_Dashboard.html", {'seller':seller})
  except:
    return render(request, "Login.html", {})




@api_view(['GET', 'POST', 'DELETE'])
def Check_Buyer_Login(request):
    if request.method == 'GET':
        if 'mobile_no' in request.GET and 'password' in request.GET:
            mobile_no = request.GET['mobile_no']
            password = request.GET['password']
            cursor = connection.cursor()
            q = "select * from realestateapp_user where mobile_no='{0}' and password='{1}'".format(mobile_no,password)
            cursor.execute(q)
        
            data  =  tuple_to_dict.ParseToDictAll(cursor)
            if (len(data)==1):
                request.session['BUYER'] = data
                return JsonResponse({"data":data,"status":True}, safe=False)
            else:
              return JsonResponse({"data":{},"status":False}, safe=False)
        else:
            return JsonResponse({"error": "Missing/incorrect required parameters: mobile_no and/or password"}, status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({}, safe=False)

   
@api_view(['GET', 'POST', 'DELETE'])
def Check_Seller_Login(request):
    if request.method == 'GET':
        if 'mobile_no' in request.GET and 'password' in request.GET:
            cursor = connection.cursor()
            q = "select * from realestateapp_user where mobile_no='{0}' and password='{1}'".format(request.GET['mobile_no'],request.GET['password'])
            cursor.execute(q)
        
            data  =  tuple_to_dict.ParseToDictAll(cursor)
            if (len(data)==1):
              request.session['SELLER'] = data
            return JsonResponse({"data":data,"status":True}, safe=False)
        else:
              return JsonResponse({"data":{},"status":False}, safe=False)
    
    return JsonResponse({}, safe=False)







@api_view(['GET', 'POST', 'DELETE'])
def LogoutBuyer(request):
    del request.session['BUYER']
    return render(request, "Login.html", {})


@api_view(['GET','POST','DELETE'])
def LogoutSeller(request):
    del request.session['SELLER']
    return render(request,"Login.html",{})