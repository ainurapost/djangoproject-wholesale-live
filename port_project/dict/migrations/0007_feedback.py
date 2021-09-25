# Generated by Django 3.2.6 on 2021-09-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0006_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True, null=True, verbose_name='Feedback')),
                ('owner', models.CharField(blank=True, max_length=200, null=True, verbose_name='Feedback owner')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Feedback date')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
