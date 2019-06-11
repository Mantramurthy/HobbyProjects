# Generated by Django 2.2.1 on 2019-05-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Name', models.CharField(max_length=20)),
                ('Mobile', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128)),
                ('Timmings', models.CharField(choices=[('10:00-11:00', '10:00-11:00'), ('11:00-12:00', '11:00-12:00'), ('12:00-1:00', '12:00-1:00'), ('2:00-3:00', '2:00-3:00'), ('3:00-4:00', '3:00-4:00'), ('4:00-5:00', '4:00-5:00')], default='Select Timmings', max_length=6)),
            ],
        ),
    ]