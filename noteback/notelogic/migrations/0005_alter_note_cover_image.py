# Generated by Django 4.1.7 on 2023-03-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notelogic', '0004_alter_note_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]