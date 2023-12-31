# Generated by Django 3.2.18 on 2023-04-24 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='接口名称', max_length=200, unique=True, verbose_name='接口名称')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('desc', models.TextField(blank=True, default='', help_text='简要描述', null=True, verbose_name='简要描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projects', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '接口',
                'verbose_name_plural': '接口',
                'db_table': 'tb_interface',
            },
        ),
    ]
