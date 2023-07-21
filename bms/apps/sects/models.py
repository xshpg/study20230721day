# 大侠属于的宗派
from django.db import models


class Sects(models.Model):
    id = models.AutoField(verbose_name='主键id',primary_key=True,help_text='主键id')
    name = models.CharField(verbose_name='组织名称',unique=True,max_length=50,help_text='组织名称')
    creat_user = models.CharField(verbose_name='创建者',max_length=20,help_text='创建者')
    desc = models.TextField(verbose_name='宗派简介',help_text='宗派 简介')

    class Meta:
        db_table = 'tb_sects'
        verbose_name = '宗派名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name