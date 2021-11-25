# Generated by Django 3.2.8 on 2021-11-25 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
        ('tasks', '0008_auto_20211125_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.taskstatus'),
        ),
        migrations.DeleteModel(
            name='TaskStatus',
        ),
    ]
