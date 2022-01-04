from django.shortcuts import render
from django.http import HttpResponse

posts = [
        {
            'name': 'Mont Blanc',
            'user': 'Yessica cortez',
        },
        {
            'name': 'Via Láctea',
            'user': 'C.Vander',
        },
        {
            'name': 'Nuevo Auditorio',
            'user': 'Sizass',
        }
    ]

def list_posts(request):
    content = []
    for post in posts:
        content.append(""" 
        <p><strong>{name}</strong></p>
        <p><small>{user}</small></p>
        """.format(**post))

    return HttpResponse('<br>'.join(content))
# Create your views here.
