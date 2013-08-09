from django.db import models

# Create your models here.

LOOT_TYPES = [
    ['W', 'Weapon'],
    ['A', 'Armor'],
    ['O', 'Other'],
]


class Loot(models.Model):
    name = models.CharField(max_length=45)
    loot_type = models.CharField(max_length=5, choices=LOOT_TYPES)
    bonus = models.IntegerField()
    owner = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Election(models.Model):
    user = models.EmailField()
    weight = models.IntegerField()
    loot = models.ForeignKey(Loot)
    awarded = models.BooleanField(default=False)
    comment = models.CharField(max_length=140)

    def __unicode__(self):
        if not self.awarded:
            return '{} request: {} ({})'.format(
                self.user, self.loot.name, self.weight)
        else:
            return '{} received {}'.format(self.user, self.loot.name)
