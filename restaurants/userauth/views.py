from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import User,Favourite
from django.http import Http404
from rest_framework import status
import hashlib
import json

class UserView(APIView):


    def post(self,request):
        #print(request.data.get('email'))
        user = User.objects.filter(email=request.data.get('email address'))
        if(user):
            print(request.data.get('user_id'))
            print("hi")
            if request.data.get('password')!=None and request.data.get('user_id')!=None:
                passw = str(request.data.get('password'))
                passw = hashlib.md5(passw.encode())
                passw = passw.hexdigest()
                if(str(request.data.get('user_id'))==str(user.values_list('id',flat=True).first()) and passw==str(user.values_list('password',flat=True).first())):
                    userdata = {
                        "message" : "login success"
                    }
                else:
                    userdata = {
                        "message" : "login failed"
                    }
            else:
                userdata = {
                    "user_id" : user.values_list('id',flat=True).first(),
                    "login_type" : "sign in"
                }
            return Response(userdata,status=status.HTTP_201_CREATED)
        else:
            userdata = {
                "user_id" : "Not registered",
                "login_type" : "sign up"
            }
            return Response(userdata,status=status.HTTP_400_BAD_REQUEST)

            
class UserRegisterView(APIView):
    def post(self,request):
        email = request.data.get('email address')
        firstname = request.data.get('first name')
        lastname = request.data.get('last name')
        password = request.data.get('password')
        regdata = {
            "email" : email,
            "firstname" : firstname,
            "lastname" : lastname,
            "password" : password,
        }
        message={
            "message" : "User registered"
        }    
        serializer = serializers.UserSerializer(data=regdata)
        if serializer.is_valid():
            serializer.save()
            return Response(message,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

class UserDetailsView(APIView):
    def get(self,request):
        temp = str(request.data.get('user_id'))
        user = User.objects.get(id=temp)
        print(user)
        tempi = []
        for i in user.favourites.all():
            tempi.append(i.favourite)
            #print(i.favourite)
        detail = {
            "email" : user.email,
            "firstname" : user.firstname,
            "lastname" : user.lastname,
           # "lastname" : user.values_list('lastname',flat=True).first(),
            "favourites" : tempi
        }
        return Response(detail)
class AddFavourite(APIView):        
    def post(self,request):
        temp = str(request.data.get('user_id'))
        user = User.objects.get(id=temp)
        if(user):
            favour=request.data.get('favourite')
            addFav = Favourite(favourite=favour,fav=user)
            addFav.save()
            addfavourite = {
                "message" : "Added to list of favourites"
            }
        else:
             addfavourite = {
                "message" : "Enter correct info about user id"
            }   
        return Response(addfavourite)

class DeleteFavourite(APIView):
    def delete(self,request):
        temp = str(request.data.get('user_id'))
        user = User.objects.get(id=temp)
        if(user):
            favour=request.data.get('favourite')
            tempi=user.favourites.get(favourite=favour)
            tempi.delete()

            deletefavourite = {
                "message" : "Removed from list of favourites"
            }
        else:
             deletefavourite = {
                "message" : "Enter correct info about user id"
            }
        return Response(deletefavourite)
