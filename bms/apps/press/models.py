# 出版社模板
from django.db import models

from utils.base_models import BaseModel


class Press(BaseModel):
    id = models.AutoField(verbose_name='主键id', primary_key=True, help_text='主键id')
    name = models.CharField(verbose_name='出版社名', max_length=20, help_text='出版社名')
    address = models.CharField(verbose_name='地址', max_length=50, help_text='地址')
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述')

    class Meta:
        db_table = 'tb_press'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
