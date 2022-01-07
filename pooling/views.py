import time
import os
import threading
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import views, response


User = get_user_model()


class HomeView(views.APIView):

    def get(self, request, *args, **kwargs):
        print("START PID", os.getpid(), "TID", threading.get_native_id())
        print("STOP  PID", os.getpid(), "TID", threading.get_native_id())
        print(User.objects.all())
        time.sleep(10)
        return response.Response({'pid':os.getpid(), 'tid':threading.get_native_id()})


class HomeNew(views.APIView):

    def get(self, request, *args, **kwargs):
        print("START PID", os.getpid(), "TID", threading.get_native_id())
        print("STOP  PID", os.getpid(), "TID", threading.get_native_id())
        print(User.objects.all())
        # time.sleep(10)
        return response.Response({'pid':os.getpid(), 'tid':threading.get_native_id()})
