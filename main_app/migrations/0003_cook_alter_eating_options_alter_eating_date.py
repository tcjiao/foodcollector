# Generated by Django 4.2.3 on 2023-07-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_eating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='eating',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='eating',
            name='date',
            field=models.DateField(verbose_name='eating date'),
        ),
    ]
