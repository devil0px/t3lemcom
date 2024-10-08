# Generated by Django 3.2.25 on 2024-09-15 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='teachers/')),
                ('rating', models.FloatField()),
                ('likes', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_valid_until', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='grades/'),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.TextField()),
                ('seats_available', models.IntegerField()),
                ('total_seats', models.IntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teacher')),
            ],
        ),
    ]
