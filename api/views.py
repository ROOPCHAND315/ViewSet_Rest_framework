from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=StudentModel.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=StudentModel.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Created'})
        return Response(serializer.errors)
    def update(self , request ,pk=None):
        id=pk
        if id is not None:
            stu= StudentModel.objects.get(id=id)
            serializer=StudentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data Updated ! '})
            return Response(serializer.errors)
    
    def partial_update(self ,request ,pk=None):
        id=pk
        if id is not None:
            stu= StudentModel.objects.get(id=id)
            serializer=StudentSerializer(stu,data=request.data ,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data partial Updated ! '})
            return Response(serializer.errors)
 
    def destroy(self,request ,pk=None):
        id= pk
        if id is not None:
            stu=StudentModel.objects.get(id=id)
            stu.delete()
            return Response({'msg':'Data Deleted !'})