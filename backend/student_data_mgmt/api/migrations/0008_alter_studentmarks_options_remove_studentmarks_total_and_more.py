# Generated by Django 5.1.6 on 2025-02-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_studentmarks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentmarks',
            options={},
        ),
        migrations.RemoveField(
            model_name='studentmarks',
            name='total',
        ),
        migrations.AddField(
            model_name='studentmarks',
            name='total_marks',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='DSA',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='Java',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='Prob_and_Stats',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='Sad',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='Web_technology',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='percentage',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=5),
        ),
    ]
