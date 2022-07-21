from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.parsers import JSONParser
from .models import Battery,Complaint,Customerissue
from .serializers import BatterySerializer,ComplaintSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import django_filters
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated


def index(request):
    return HttpResponse("WELCOME TO SERVICE")



class BatteryAPIView(APIView):
    model = BatterySerializer
    battery = Battery.objects.all()
    serializer_class = BatterySerializer

    def get(self,request):
        battery = Battery.objects.all()
        serializer = BatterySerializer(battery,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BatterySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BatteryDetail(APIView):
    def get_object(self, pk):
        try:
            return Battery.objects.get(pk=pk)
        except Battery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        battery = self.get_object(pk)
        serializer = BatterySerializer(battery)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        battery = self.get_object(pk)
        serializer = BatterySerializer(battery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        battery = self.get_object(pk)
        Battery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 




class ComplaintAPIView(APIView):
    model = ComplaintSerializer
    complaint = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def get(self,request):
        complaint = Complaint.objects.all()
        serializer = ComplaintSerializer(complaint,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComplaintDetail(APIView):
    def get_object(self, pk):
        try:
            return Complaint.objects.get(pk=pk)
        except Complaint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        complaint = self.get_object(pk)
        Complaint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class CustomerList(APIView):
#    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        customer_issue = request.data['customer_issue']
        additional_info={}
        if customer_issue:
            additionalinfos=Customerissue.objects.get(id=customer_issue).additionalinfos.all()
            additional_info={p.name:p.id for p in additionalinfos}
        return JsonResponse(data=additional_info, safe=False)