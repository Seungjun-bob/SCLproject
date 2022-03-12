# Generated by Django 4.0.1 on 2022-03-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libname', models.CharField(max_length=45, null=True)),
                ('callno', models.CharField(max_length=45, null=True)),
                ('title', models.CharField(max_length=45, null=True)),
                ('author', models.CharField(max_length=45, null=True)),
                ('publisher', models.CharField(max_length=45, null=True)),
                ('pubyear', models.CharField(max_length=45, null=True)),
                ('isbn', models.CharField(max_length=45, null=True)),
            ],
        ),
    ]
