from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from app_1.models import Student
from app_1.serializers import StudentSerializer


# Create your views here.
@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        query = Student.objects.all()
        serializer = StudentSerializer(query, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def student_detail(request, pk):
    try:
        s = Student.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(s)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(s, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        s.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)




# def add_student(request):
#     form = Student(request.POST)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             student_name = form.cleaned_data['name']
#             students.append(student_name)
#         else:
#             raise Exception('No valid student')
#
#     return render(request, 'form.html', {'form': form})
