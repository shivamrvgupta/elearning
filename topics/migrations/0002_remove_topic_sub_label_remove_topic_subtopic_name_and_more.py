# Generated by Django 4.1.7 on 2023-03-13 21:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='sub_label',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='subtopic_name',
        ),
        migrations.CreateModel(
            name='Sub_Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.ImageField(blank=True, upload_to='sub-label/%Y/%m/%d/')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.topic')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.sub_topic'),
        ),
    ]
