# Generated by Django 3.1.6 on 2021-02-14 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceCode',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(default=main.models.generate_code, max_length=8, unique=True)),
                ('ip_address', models.GenericIPAddressField(unique=True)),
                ('expire_date', models.DateTimeField(default=main.models.get_expire_date)),
                ('approved_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]