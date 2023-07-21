# 书中的大侠名
from django.db import models

from utils.base_models import BaseModel


class Figures(BaseModel):
    choices = ((1, '男'), (2, '女'), (3, '其他'))
    id = models.AutoField(verbose_name='主键id',primary_key=True,help_text='主键id')
    name = models.CharField(verbose_name='姓名',max_length=20,help_text='姓名',unique=True)
    title = models.ForeignKey('books.Books',on_delete=models.CASCADE,
                              verbose_name='所属图书',help_text='所属图书')
    gender = models.IntegerField(choices=choices,verbose_name='性别',help_text='性别')
    age = models.IntegerField(verbose_name='年龄',help_text='年龄')
    nation = models.CharField(verbose_name='所属国家',max_length=20,help_text='所属国家')
    desc = models.TextField(verbose_name='简要描述',help_text='简要描述')

    class Meta:
        db_table = 'tb_figures'
        verbose_name = '武侠人物表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name