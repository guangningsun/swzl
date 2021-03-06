# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=200)),
                ('class_num', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_class_id', models.CharField(max_length=200)),
                ('payment_class_name', models.CharField(max_length=200)),
                ('payment_class_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200)),
                ('payment_class_name', models.CharField(max_length=200)),
                ('payment_create_time', models.CharField(max_length=200)),
                ('stu_payment_time', models.CharField(max_length=200)),
                ('payment_amount', models.CharField(max_length=200)),
                ('payment_status', models.CharField(max_length=200)),
                ('stu_id', models.CharField(max_length=200)),
                ('create_user_id', models.CharField(max_length=200)),
                ('payment_res_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=200)),
                ('stu_num_id', models.CharField(max_length=200)),
                ('stu_name', models.CharField(max_length=200)),
                ('stu_id_card', models.CharField(max_length=200)),
                ('stu_sexy', models.CharField(max_length=200)),
                ('stu_phone_num', models.CharField(max_length=200)),
                ('stu_desc', models.CharField(max_length=200)),
                ('class_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('login_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('user_permission', models.CharField(max_length=200)),
                ('create_time', models.CharField(max_length=200)),
                ('is_deleted', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('class_id', models.CharField(max_length=200)),
            ],
        ),
    ]
