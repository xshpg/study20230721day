from django.db import models


class Interfaces(models.Model):
    name = models.CharField(verbose_name='接口名称',max_length=200,help_text='接口名称',unique=True)
    tester = models.CharField(verbose_name='测试人员',max_length=50,help_text='测试人员')
    desc = models.TextField(verbose_name='简要描述',help_text='简要描述',default='',null=True,blank=True)
    project = models.ForeignKey('projects.Projects',verbose_name='所属项目',on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_interface'
        verbose_name = '接口'
        verbose_name_plural = '接口'

    def __str__(self):
        return self.name




















