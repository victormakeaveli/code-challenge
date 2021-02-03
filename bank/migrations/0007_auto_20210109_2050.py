# Generated by Django 3.1.4 on 2021-01-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_transaction_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='state',
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('paid', 'paid'), ('refunded', 'refunded'), ('dispute', 'dispute'), ('failed', 'failed')], default=None, max_length=64, null=True),
        ),
    ]
