from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Student
import logging

logger = logging.getLogger(__name__)

from rest_framework.views import APIView
# Create your views here.


class StudentView(APIView):
    """
    The purpose of this view is to get all data of student
    """
    def get(self, request):
        logger_user_id = request.META['REMOTE_ADDR']
        logger.debug("[" + logger_user_id + "][StudentView][POST]Entered" + f'Request Parameter:{request.data}')
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response({"message": "Data Retrieved Successfully", "status": status.HTTP_200_OK, "result": serializer.data})

    def post(self, request):
        logger_user_id = request.META['REMOTE_ADDR']
        logger.debug("[" + logger_user_id + "][StudentView][POST]Entered" + f'Request Parameter:{request.data}')
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully", "status": status.HTTP_201_CREATED, "result": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

