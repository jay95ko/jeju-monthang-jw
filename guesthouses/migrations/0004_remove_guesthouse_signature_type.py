# Generated by Django 2.2.5 on 2021-07-07 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guesthouses', '0003_guesthouse_signature_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guesthouse',
            name='signature_type',
        ),
    ]
