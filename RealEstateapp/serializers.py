from rest_framework import serializers
from .models import User, Property, Cities, States

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'role', 'email_id', 'mobile_no','password']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'property_name', 'description', 'area_sq_feet', 'num_bedrooms', 'num_bathrooms', 'hospitals_nearby', 'colleges_nearby', 'created_at', 'seller_name', 'image','address', 'city', 'state']

 
class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'stateid', 'cityid', 'cityname']

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ['id', 'stateid', 'statename']

 