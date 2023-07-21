from django.db import models


class Projects(models.Model):
    name = models.CharField(verbose_name='项目名称',max_length=200,help_text='项目名称',unique=True)
    leader = models.CharField(verbose_name='负责人',max_length=50,help_text='负责人')
    tester = models.CharField(verbose_name='测试人员',max_length=50,help_text='测试人员')
    programer = models.CharField(verbose_name='开发人员',max_length=50,help_text='开发人员')
    publish_app = models.CharField(verbose_name='发布应用',max_length=50,help_text='发布应用')
    desc = models.TextField(verbose_name='简要描述',help_text='简要描述',default='',null=True,blank=True)

    class Meta:
        db_table = 'tb_project'
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name









