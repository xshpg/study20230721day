# 作者
from django.db import models

from utils.base_models import BaseModel


class Editors(BaseModel):
    choices = ((1,'男'),(2,'女'),(3,'其他'))
    id = models.AutoField(verbose_name='主键id',primary_key=True,help_text='主键id')
    name = models.CharField(verbose_name='作者名',max_length=10,help_text='作者名')
    gender = models.IntegerField(choices=choices)
    age = models.IntegerField(verbose_name='年龄',help_text='年龄')
    address = models.CharField(verbose_name='出生地',max_length=20,help_text='出生地')
    desc = models.TextField(verbose_name='个人简介',help_text='个人简介')

    class Meta:
        db_table = 'tb_editors'
        verbose_name = '作者表信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
