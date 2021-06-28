from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def query(request):
    return JsonResponse({"status": True}, safe = True)