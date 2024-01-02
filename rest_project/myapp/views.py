from django.shortcuts import render
from.models import Book
from .serializers import BookSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
@csrf_exempt
def booklistview(request):
    if request.method == 'GET':
        employees = Book.objects.all()
        serializer = BookSerializer(employees, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = BookSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

@api_view(['DELETE','GET','PUT'])
def bookDetailView(request,pk):
    try:
        
      book_o=Book.objects.get(pk=pk)
      # return JsonResponse("Employee "+str(pk), safe=False) 
      # print(employee) 
    except Book.DoesNotExist:
        return Response(status=404)
      #   return HttpResponse(status=404)

      

    if request.method=="DELETE":
        book_o.delete()
        print('Data Deleted Successfully')
        return Response(status.HTTP_204_NO_CONTENT)
      #   return JsonResponse(status.HTTP_204_NO_CONTENT,safe=False)
    elif request.method=="GET":
        serializer=BookSerializer(book_o)
        return Response(serializer.data) 
      #   return JsonResponse(serializer.data, safe=False) 
    elif request.method=="PUT":
         # jsonData=JSONParser().parse(request)
         serializer=BookSerializer(book_o,data=request.data)
         if serializer.is_valid():
             serializer.save()
         # print(jsonData)
             return Response(serializer.data)
            #  return JsonResponse(serializer.data,safe=False)
         else:
             return Response(serializer.errors)
            #  return JsonResponse(serializer.errors,safe=False)
    
        
