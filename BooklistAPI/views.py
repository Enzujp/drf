from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
#pass in methods in an array into the api_view function
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)


#you can map a method from a class, you need to declare that method as a static method


class Orders():
    @staticmethod
    @api_view()

    def listOrders(request):
        return Response({'message': 'list of orders'}, 200)
    

#Routing class-based views

