from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rip_services.models import Ripcreationrequest
from rip_services.serializers import RipcreationrequestSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def ripcreationrequest_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ripcreationrequests = Ripcreationrequest.objects.all()
        serializer = RipcreationrequestSerializer(ripcreationrequests, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RipcreationrequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def ripcreationrequest_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        ripcreationrequest = Ripcreationrequest.objects.get(pk=pk)
    except Ripcreationrequest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RipcreationrequestSerializer(ripcreationrequest)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RipcreationrequestSerializer(ripcreationrequest, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ripcreationrequest.delete()
        return HttpResponse(status=204)