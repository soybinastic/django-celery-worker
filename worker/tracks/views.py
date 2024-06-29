from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# import tasks
from .tasks import process_track
# Create your views here.


@api_view(['GET'])
def get_request(request):

    result = process_track.delay()
    return Response({ 'message' : 'Processed successfully', 'task' : result.id })