# Generated by Django 2.1.2 on 2018-10-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_auto_20181016_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exerciseemailreply',
            options={'verbose_name_plural': 'Exercise email replies '},
        ),
        migrations.AddField(
            model_name='exerciseemail',
            name='sort_order',
            field=models.IntegerField(default=0),
        ),
    ]