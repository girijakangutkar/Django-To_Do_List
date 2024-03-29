# Generated by Django 4.0.1 on 2023-06-06 10:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import task.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=task.models.one_week_hence)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.status')),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.todolist')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
