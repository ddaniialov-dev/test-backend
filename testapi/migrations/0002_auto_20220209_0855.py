# Generated by Django 3.2 on 2022-02-09 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('cvv', models.CharField(max_length=3)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_expire', models.DateTimeField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='testapi.account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('Invoice', 'invoice'), ('Transfer', 'transfer'), ('Letter of Credit', 'letter_of_credit')], max_length=16)),
                ('from_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_from', to='testapi.card')),
                ('to_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_to', to='testapi.card')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='AirportsData',
        ),
        migrations.RemoveField(
            model_name='boardingpasses',
            name='ticket_no',
        ),
        migrations.DeleteModel(
            name='Flights',
        ),
        migrations.DeleteModel(
            name='Public',
        ),
        migrations.RemoveField(
            model_name='seats',
            name='aircraft_code',
        ),
        migrations.RemoveField(
            model_name='ticketflights',
            name='ticket_no',
        ),
        migrations.DeleteModel(
            name='AircraftsData',
        ),
        migrations.DeleteModel(
            name='BoardingPasses',
        ),
        migrations.DeleteModel(
            name='Seats',
        ),
        migrations.DeleteModel(
            name='TicketFlights',
        ),
        migrations.DeleteModel(
            name='Tickets',
        ),
    ]
