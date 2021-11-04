# Generated by Django 3.2.8 on 2021-11-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='task',
            name='lables',
            field=models.ManyToManyField(blank=True, to='tasks.TaskLable'),
        ),
    ]
