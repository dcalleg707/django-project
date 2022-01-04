from django.http import HttpResponse

from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi!, current server time is {now}'.format(now=now))

def hi(request):
    #import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(",")]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        return HttpResponse('Sorry, you are not allowed here')
    return HttpResponse('Oh hi!, {name} welcome to platzi'.format(name=name))

