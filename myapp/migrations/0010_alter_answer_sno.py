# Generated by Django 4.0.5 on 2022-07-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='sno',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
