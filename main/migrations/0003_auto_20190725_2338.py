# Generated by Django 2.2.3 on 2019-07-25 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
