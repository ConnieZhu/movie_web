# Generated by Django 2.1.2 on 2020-08-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]