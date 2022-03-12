# Generated by Django 4.0.1 on 2022-03-12 08:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('lbrry_seq_no', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('lbrry_name', models.CharField(max_length=45)),
                ('gu_code', models.CharField(max_length=10, null=True)),
                ('code_value', models.CharField(max_length=45)),
                ('adres', models.CharField(max_length=45)),
                ('tel_no', models.CharField(max_length=45, null=True)),
                ('hmpg_url', models.CharField(max_length=200, null=True)),
                ('op_time', models.CharField(max_length=200, null=True)),
                ('fdrm_close_date', models.CharField(max_length=200, null=True)),
                ('lbrry_se_name', models.CharField(max_length=45)),
                ('xcnts', models.FloatField(null=True)),
                ('ydnts', models.FloatField(null=True)),
                ('avg', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libsearch.library')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]