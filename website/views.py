from django.shortcuts import render_to_response
from django.template import RequestContext

from elections.models import Loot, Player, Election
from blog.models import Content


def home(request):
    _content = Content.objects.all().order_by('-date')[:10]
    return render_to_response('base.html', {
        'content': _content,
    }, context_instance=RequestContext(request))
