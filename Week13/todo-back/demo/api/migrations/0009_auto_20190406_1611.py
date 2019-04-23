# Generated by Django 2.2 on 2019-04-06 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tassk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TaskList')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
