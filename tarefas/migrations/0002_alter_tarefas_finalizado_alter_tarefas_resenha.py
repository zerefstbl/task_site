# Generated by Django 4.0.4 on 2022-05-26 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='resenha',
            field=models.TextField(max_length=300),
        ),
    ]