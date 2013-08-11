from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from elections.models import Loot, Player, Election, Hoard


def results(request, hoard):
    hoard = hoard.replace(' ', '')
    _hoard = get_object_or_404(Hoard, name__icontains=hoard)
    _loot = Loot.objects.filter(hoard=_hoard).order_by('owner')
    return render_to_response('hoard_results.html',
                              {'loot': _loot, 'hoard': _hoard},
                              context_instance=RequestContext(request))


def election(request):
    if request.method == 'GET':
        loot = Loot.objects.filter(owner__isnull=True).order_by('name')
        return render_to_response('election.html',
                                  {'loot': loot},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        player = None
        email = request.POST['email']
        try:
            player = Player.objects.get(email=email)
        except:
            player = Player(email=email, name=email, character=email)
            player.save()

        for i in range(1, 4):
            if request.POST[str(i)] == '0':
                pass
            else:
                loot_chosen = Loot.objects.get(pk=request.POST[str(i)])
                if (len(Election.objects.filter(
                        player=player,
                        loot=loot_chosen)) > 0 or
                    len(Election.objects.filter(
                        player=player,
                        weight=i)) > 0):
                    pass
                else:
                    Election(
                        player=player,
                        weight=i,
                        comment=request.POST['comment-{}'.format(i)],
                        loot=loot_chosen).save()
        return render_to_response('thanks.html',
                                  {},
                                  context_instance=RequestContext(request))
