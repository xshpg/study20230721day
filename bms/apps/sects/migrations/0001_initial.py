# Generated by Django 3.2.19 on 2023-06-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sects',
            fields=[
                ('id', models.AutoField(help_text='主键id', primary_key=True, serialize=False, verbose_name='主键id')),
                ('name', models.CharField(help_text='组织名称', max_length=50, unique=True, verbose_name='组织名称')),
                ('creat_user', models.CharField(help_text='创建者', max_length=20, verbose_name='创建者')),
                ('desc', models.TextField(help_text='宗派 简介', verbose_name='宗派简介')),
            ],
            options={
                'verbose_name': '宗派名称',
                'verbose_name_plural': '宗派名称',
                'db_table': 'tb_sects',
            },
        ),
    ]