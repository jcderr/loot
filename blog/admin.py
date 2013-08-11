from django.contrib import admin
from blog.models import Campaign, CampaignJournal, BlogPost

admin.site.register(Campaign)
admin.site.register(CampaignJournal)
admin.site.register(BlogPost)
