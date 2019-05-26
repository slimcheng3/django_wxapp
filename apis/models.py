from django.db import models

# Create your models here.
# 功能清单
class App(models.Model):
    appid = models.CharField(max_length=128, primary_key=True) # 唯一ID
    category = models.CharField(max_length=128) # 类别
    application = models.CharField(max_length=128) # 功能名字
    name = models.CharField(max_length=128) # 中文名字
    publish_date = models.DateField() # 发布日期
    url = models.CharField(max_length=128) # 请求链接
    desc = models.CharField(max_length=128) # 描述

    def to_dict(self):
        return {
            'appid': self.appid,
            'category': self.category,
            'application': self.application,
            'name': self.name,
            'publish_date': self.publish_date,
            'url': self.url,
            'desc': self.desc
        }

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.to_dict())
