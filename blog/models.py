from django.db import models
from django.contrib.auth.models import User
from elections.models import Player

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)


class Content(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    permalink = models.CharField(max_length=50, blank=True)

    def teaser(self):
        return self.content.split('\n')[0]


class CampaignJournal(Content):
    character = models.ForeignKey(Player)

    def __unicode__(self):
        return '{} writes: {}'.format(
            self.character.character, self.title)
    

class BlogPost(Content):
    pass