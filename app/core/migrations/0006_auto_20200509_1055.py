# Generated by Django 2.1.15 on 2020-05-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200508_1842'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vote',
            new_name='Choice',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='is_published',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('1', 'Text answer'), ('2', 'One choice option'), ('3', 'Multiple choice option')], default=1, max_length=1),
        ),
    ]
