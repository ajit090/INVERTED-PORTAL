from django.contrib import admin
from django.urls import path,include
from Model import views
from .views import Complaint,ComplaintAPIView,ComplaintDetail,Battery,BatteryAPIView,BatteryDetail,CustomerList

urlpatterns = [
    path('',views.index,name='index'),
    path('Complaint/',ComplaintAPIView.as_view()),
    path('detail/<int:pk>/',ComplaintDetail.as_view()),
    path('Battery/',BatteryAPIView.as_view()),
    path('detail2/<int:pk>/',BatteryDetail.as_view()),
    path('customerissue/',CustomerList.as_view()),

]
