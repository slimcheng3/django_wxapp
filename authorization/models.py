from django.db import models
from apis.models import App

# Create your models here.
class User(models.Model):
    #微信用户openid
    openid = models.CharField(max_length=32, unique=True)
    #用户昵称
    nickname = models.CharField(max_length=256)
    #关注的城市
    focus_cities = models.TextField(default='[]')
    #关注的股票
    focus_stocks = models.TextField(default='[]')
    #关注的星座
    focus_constellations = models.TextField(default='[]')
    menu = models.ManyToManyField(App)

    class Meta:
        db_table = 'user';
        indexes = [
            models.Index(fields=['openid','nickname'])
        ]

    def __str__(self):
        return "%s(%s)" % (self.nickname, self.openid)
