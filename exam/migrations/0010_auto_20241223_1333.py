# Generated by Django 3.0.5 on 2024-12-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20241223_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresult',
            name='marks',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
