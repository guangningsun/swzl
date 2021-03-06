# Generated by Django 2.2.3 on 2019-10-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0003_paymentinfo_merorderid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_line_id', models.CharField(max_length=20)),
                ('bus_line_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lost_id', models.CharField(max_length=200)),
                ('pick_up_time', models.CharField(max_length=200)),
                ('bus_line_name', models.CharField(max_length=200)),
                ('lost_type_name', models.CharField(max_length=200)),
                ('receive_address', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=200)),
                ('is_received', models.CharField(max_length=200)),
                ('received_name', models.CharField(max_length=200)),
                ('received_id_card', models.CharField(max_length=200)),
                ('received_phone_number', models.CharField(max_length=200)),
                ('received_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lost_type_id', models.CharField(max_length=200)),
                ('lost_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='ClassInfo',
        ),
        migrations.DeleteModel(
            name='PaymentClassInfo',
        ),
        migrations.DeleteModel(
            name='PaymentInfo',
        ),
        migrations.DeleteModel(
            name='StudentInfo',
        ),
    ]
