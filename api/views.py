from django.shortcuts import render
from itsdangerous import Serializer

from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse #for jsonresponse only 

# Create your views here.

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    Serializer = StudentSerializer(stu)
    # jason_data = JSONRenderer().render(Serializer.data)                 [can use in comments also]
    # return HttpResponse(jason_data, content_type='application/jason')
    return JsonResponse(Serializer.data)


def student_list(request,):
    stu = Student.objects.all()
    Serializer = StudentSerializer(stu,many=True)
    # jason_data = JSONRenderer().render(Serializer.data)                   [  [can use in comments also]]
    # return HttpResponse(jason_data, content_type='application/jason')
    return JsonResponse(Serializer.data, safe=False)
