# Generated by Django 4.1.7 on 2023-03-13 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_remove_topic_sub_label_remove_topic_subtopic_name_and_more'),
        ('quiz', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.sub_topic'),
        ),
    ]
