from django.shortcuts import render_to_response
from one.thoughts.models import Thought


def index(request):
    """homepage view"""
    thoughts = Thought.objects.all()
    return render_to_response('index.html', {
        'thoughts': thoughts,
    })