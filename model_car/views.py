from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cars
from .serialziers import StudentSerializer
class CarsFunction(APIView):

    def get(self, request):
        student = Cars.objects.all()
        serializer = StudentSerializer(student, many=True)
        print(Response("Bracha malumotlar"))
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(Response("Malumoatlar ozgartrish"))
            return Response(serializer.data,status=status.HTTP_201_CREATED)

class CarsView(APIView):

    def get_object(self, request, pk):  # pk parametr qo'shildi
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            return None

    def patch(self, request, pk):
        car = self.get_object(pk)
        serializer = Cars(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)