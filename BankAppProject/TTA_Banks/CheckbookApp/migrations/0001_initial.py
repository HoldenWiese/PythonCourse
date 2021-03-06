# Generated by Django 3.0.6 on 2020-06-12 22:59

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('starting_balance', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            managers=[
                ('UserAccounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now=True)),
                ('transaction_type', models.CharField(choices=[('withdrawal', 'Withdrawal'), ('deposit', 'Deposit')], max_length=120)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField(max_length=1000)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheckbookApp.UserAccount')),
            ],
            managers=[
                ('UserTransactions', django.db.models.manager.Manager()),
            ],
        ),
    ]
