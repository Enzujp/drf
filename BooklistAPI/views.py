from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
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

# class BookView(Orders):
#     def get(self, request, pk):
#         return Response({"message": "single book with id" + str(pk)}, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         return Response({"title": request.data.get('title')}, status=status.HTTP_200_OK)


class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "All books"}, status.HTTP_200_OK)
    
    def create(self, request):
        return Response({"message": "creating a book"}, status.HTTP_201_CREATED)


    def update(self, request, pk=None):
        return Response({"message": "updating a book"}, status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        return Response({"message": "Displaying a book"}, status.HTTP_200_OK)
    
    def partial_update(self, request, pk=None):
        return Response({"message": "Partially updating a book"}, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({"message": "Deleting a book"}, status.HTTP_200_OK)