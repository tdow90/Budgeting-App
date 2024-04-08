# Generated by Django 5.0.3 on 2024-04-08 22:42

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('type', models.CharField(choices=[('Sal', 'Salary'), ('Var', 'Variable')], max_length=3)),
                ('frequncy', models.CharField(choices=[('MON', 'Monthly'), ('BW', 'Bi-weekly'), ('SM', 'Semimonthly'), ('W', 'Weekly'), ('AN', 'Annually')], max_length=3)),
                ('pay_date_one', models.IntegerField(validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('pay_date_two', models.IntegerField(validators=[django.core.validators.MaxValueValidator(28), django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]