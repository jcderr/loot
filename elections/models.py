from django.db import models

# Create your models here.

LOOT_TYPES = [
    ['W', 'Weapon'],
    ['A', 'Armor'],
    ['O', 'Other'],
]


class Player(models.Model):
    name = models.CharField(max_length=45)
    character = models.CharField(max_length=45)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Loot(models.Model):
    name = models.CharField(max_length=45)
    loot_type = models.CharField(max_length=5, choices=LOOT_TYPES)
    bonus = models.IntegerField()
    owner = models.ForeignKey(Player, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Election(models.Model):
    player = models.ForeignKey(Player, null=True, blank=True)
    weight = models.IntegerField()
    loot = models.ForeignKey(Loot)
    awarded = models.BooleanField(default=False)
    comment = models.CharField(max_length=140)

    def __unicode__(self):
        if not self.awarded:
            return '{} request: {} ({})'.format(
                self.player, self.loot.name, self.weight)
        else:
            return '{} received {}'.format(self.player, self.loot.name)
