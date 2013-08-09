from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from loot.elections.models import Loot


def election(request):
    if request.method == 'GET':
        loot = Loot.objects.filter(elections__awarded=False)
        return render_to_response('election.html',
                                  {'loot': loot},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        # process elections
        return HttpResponse()
