# 书名
from django.db import models

from utils.base_models import BaseModel


class Books(BaseModel):
    id = models.AutoField(verbose_name='主键id',primary_key=True,help_text='主键id')
    name = models.CharField(verbose_name='书名',max_length=20,help_text='书名',unique=True)
    author = models.ForeignKey('editors.Editors',on_delete=models.CASCADE,verbose_name='所属作者',
                               help_text='所属作者')
    publish_house = models.ForeignKey('press.Press',on_delete=models.CASCADE,
                                      verbose_name='所属出版社',help_text='所属出版社')
    press_time = models.CharField(verbose_name='出版时间',max_length=20,help_text='出版时间')
    desc = models.TextField(verbose_name='简要描述',help_text='简要描述')

    class Meta:
        db_table = 'tb_books'
        verbose_name ='图书信息'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name