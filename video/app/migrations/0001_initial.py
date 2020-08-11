# Generated by Django 2.1.2 on 2020-07-14 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('avatar', models.CharField(default='', max_length=500)),
                ('gender', models.CharField(default='', max_length=10)),
                ('birthday', models.DateTimeField(blank=True, default=None, null=True)),
                ('status', models.BooleanField(db_index=True, default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(default='', max_length=500)),
                ('video_type', models.CharField(default='other', max_length=50)),
                ('from_to', models.CharField(default='custom', max_length=20)),
                ('nationality', models.CharField(default='other', max_length=20)),
                ('info', models.TextField()),
                ('status', models.BooleanField(db_index=True, default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('identity', models.CharField(default='', max_length=50)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_star', to='app.Video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('number', models.IntegerField(default=1)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_sub', to='app.Video')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together={('name', 'video_type', 'from_to', 'nationality')},
        ),
        migrations.AlterUniqueTogether(
            name='videosub',
            unique_together={('video', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='videostar',
            unique_together={('video', 'name', 'identity')},
        ),
    ]
