"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from RealEstateapp import seller
from RealEstateapp import login
from RealEstateapp import view
from RealEstateapp import dashboard



urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^api/login',login.Login), 
    url(r'^api/register',login.Register),
    url(r'^api/dashboard',dashboard.Dashboard),
    url(r'^api/filterproperties',dashboard.filtersubmit),
    url(r'^api/likeproperty',dashboard.like_property),



    url(r'^api/registration_submit',login.Registration_submit),
    
    url(r'^api/checkbuyerlogin',login.Check_Buyer_Login),
    url(r'^api/checksellerlogin',login.Check_Seller_Login),

    url(r'^api/buyerdashboard',login.BuyerDashboard),
    url(r'^api/sellerdashboard',login.SellerDashboard),

    url(r'^api/logoutbuyer',login.LogoutBuyer), 
    url(r'^api/logoutseller',login.LogoutSeller), 

    
    
    url(r'^api/propertyinterface',seller.PropertiesInterface),
    url(r'^api/displayallproperty',seller.DisplayAllProperty), 
    url(r'^api/addproperty',seller.PropertySubmit), 
    url(r'^api/property_list',seller.Property_List), 
    url(r'^api/propertybyid',seller.Property_List_By_Id), 
    url(r'^api/propertyupdatedelete',seller.Property_Update_Delete), 
    url(r'^api/displaypropertyimage',seller.Property_Display_Picture), 
    url(r'^api/updatepropertyimage',seller.UpdatePropertyImage),
    url(r'^api/sellerdetail',seller.Seller_Detail),
    url(r'^api/propertydetail',seller.property_detail),


    url(r'^api/statelist',view.State_List), 
    url(r'^api/citylist',view.City_List) 

]


