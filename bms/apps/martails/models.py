# 书中的技能
from django.db import models

from utils.base_models import BaseModel


class Martails(BaseModel):
    id = models.AutoField(verbose_name='主键id',primary_key=True,help_text='主键id')
    name = models.CharField(verbose_name='技能名',max_length=20,help_text='技能名')
    people = models.ForeignKey('figures.Figures',on_delete=models.CASCADE,
                               verbose_name='大侠名',help_text='大侠名')
    learn_time = models.IntegerField(verbose_name='修炼时间',help_text='修炼时间')
    power_value = models.IntegerField(verbose_name='武力值',help_text='武力值')
    desc = models.TextField(verbose_name='简要描述',help_text='简要描述')

    class Meta:
        db_table = 'tb_martails'
        verbose_name = '技能信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name