from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from elections.models import Player
from blog.models import CampaignJournal


def post(request):
    pass

def listview(request, character):
    _player = get_object_or_404(Player, character__iexact=character)
    _character = _player.character
    _posts = CampaignJournal.objects.filter(
        character__character=character).order_by('-date')
    return render_to_response('listview.html',
        {'posts': _posts,
         'character': _character, },
        context_instance=RequestContext(request))

