# Generated by Django 3.0.5 on 2020-05-16 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200516_1446'),
        ('reviews', '0002_auto_20200516_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Book'),
            preserve_default=False,
        ),
    ]
