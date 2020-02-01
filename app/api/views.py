import logging
import os
import time
import json
from builtins import int
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from worker.tasks import get_equally_separated_points


logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def index(request, format=None):
    # if request.method == 'POST':
    #     fetch_data_from_quandl.s(
    #         database_code=request.data['database_code'],
    #         dataset_code=request.data['dataset_code']).delay()
    #     return Response('', status=status.HTTP_201_CREATED)
    # files = [] if not os.path.exists(settings.DATA_PATH) else os.listdir(settings.DATA_PATH)
    return Response(files)

@api_view(['GET'])
def get(request, slug, format=None):
    # logger.info(slug)
    # response = predict.s(int(slug)).delay()
    # while not response.ready():
    #     time.sleep(1)
    return Response(response.result)
    # try:
    #     s = json.loads(s)
    #     logger.info(f
    #     '{path}: content is json')
    # except:
    #     logger.info(f'{path}: content is not json')
    # return Response(s)

@api_view(['POST'])
def post(request, format=None):
    wkt = request.POST.get("wkt")
    area = int(request.POST.get("area"))
    print(wkt)
    response = get_equally_separated_points.s(wkt, area, 4326).delay()
    while not response.ready():
        time.sleep(1)
    return Response(response.result)
    # try:
    #     s = json.loads(s)
    #     logger.info(f
    #     '{path}: content is json')
    # except:
    #     logger.info(f'{path}: content is not json')
    # return Response(s)
