from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from elections.models import Election, Loot, Player


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--commit',
                    action="store_true",
                    default=False,
                    dest="commit",
                    help='Commit ownership into the database'),
        make_option('--revert',
                    action="store_true",
                    default=False,
                    dest="revert",
                    help='Revert all ownership'),
    )

    def handle(self, commit, revert, *args, **options):
        if revert:
            for l in Loot.objects.all():
                l.owner = None
                l.save()
            for e in Election.objects.all():
                e.awarded = False
                e.save()
            return

        conflicts = []
        try:
            for i in Loot.objects.all():
                if i.owner or i.conflict:
                    pass
                else:
                    for x in range(1, 4):
                        winner = self._determine_winner(loot=i, weight=x)
                        if winner and len(winner) == 1:
                            if not i.owner:
                                i.owner = winner[0]
                                if commit:
                                    i.save()
                                    e = Election.objects.get(loot=i, player=i.owner)
                                    e.awarded = True
                                    e.save()
                                else:
                                    self.stdout.write('{} to {}'.format(i, winner))
                        elif not winner is None and len(winner) > 1:
                            print 'conflict for {}'.format(i)
                            if not i.owner:
                                if commit:
                                    i.conflict = True
                                    i.save()
                            conflicts.append([i, winner])
        except Exception, e:
            raise CommandError(e)

        if commit:
            self.stdout.write('==== AWARDS ====\n')
            for p in Player.objects.all():
                self.stdout.write('Items for {}'.format(p.name))
                for i in Loot.objects.filter(owner=p):
                    self.stdout.write('    {}'.format(i))

        self.stdout.write('\n\n==== LOSERS ====\n')
        for e in Election.objects.filter(awarded=False):
            self.stdout.write('{}'.format(e))

        self.stdout.write('\n\n==== CONFLICTS ====\n')
        for c in conflicts:
            _i = c[0]
            _p = c[1]
            self.stdout.write('{}'.format(_i))
            self.stdout.write('    {}'.format(_p))

    def _determine_winner(self, *args, **kwargs):
        if not all(k in kwargs for k in ('loot', 'weight')):
            raise CommandError('Missing something')

        _loot = kwargs['loot']
        _weight = kwargs['weight']
        _elections = Election.objects.filter(loot=_loot, weight=_weight)

        if len(_elections) == 1:
            return [_elections[0].player, ]
        elif len(_elections) > 1:
            return [e.player for e in _elections]
        else:
            return None
