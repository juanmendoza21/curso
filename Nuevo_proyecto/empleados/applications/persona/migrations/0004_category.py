# Generated by Django 3.2.3 on 2021-06-11 16:06

from django.db import migrations, models
import fontawesome_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleado_hoja_vida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', fontawesome_5.fields.IconField(blank=True, max_length=60)),
            ],
        ),
    ]
