# Generated by Django 3.2.5 on 2021-08-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210726_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='공지사항', max_length=30),
        ),
    ]