# 学习的技能的人
from django.db import models


class Scholars(models.Model):
    id = models.AutoField(verbose_name='主键id',primary_key=True,help_text='主键id')
    name = models.CharField(verbose_name='姓名',max_length=20,help_text='姓名')
    choices = ((1,'男'),(2,'女'),(3,'保密'))
    gender = models.IntegerField(choices=choices,verbose_name='性别',help_text='性别')
    age = models.IntegerField(verbose_name='年龄',help_text='年龄')
    address = models.CharField(verbose_name='祖籍',max_length=50,help_text='祖籍')
    choices_level = ((1, '博士'), (2, '研究生'), (3, '本科'),(4,'大专'),(5,'高中'),(6,'初中'),(7,'小学'),(8,'其他'))
    education_level = models.IntegerField(choices=choices_level,verbose_name='学历',help_text='学历')
    choices_type = ((1,'全日制'),(2,'非全日制'),(3,'国外留学'))
    edu_type = models.IntegerField(choices=choices_type,verbose_name='学历类型',help_text='学历类型')
    personal_experience = models.TextField(verbose_name='个人经历',help_text='个人经历')

    class Meta:
        db_table = 'tb_scholars'
        verbose_name = '学技能的人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


