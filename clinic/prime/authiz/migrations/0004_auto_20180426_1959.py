# Generated by Django 2.0.4 on 2018-04-26 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authiz', '0003_client_public_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='is_staff',
            new_name='confirmed',
        ),
    ]
