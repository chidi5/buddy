# Generated by Django 3.2.6 on 2021-09-18 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210915_2259'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gender',
            new_name='Attribute',
        ),
        migrations.RemoveField(
            model_name='category',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gender',
        ),
        migrations.AddField(
            model_name='category',
            name='attribute',
            field=models.ManyToManyField(blank=True, related_name='attribute', to='product.Attribute'),
        ),
        migrations.AddField(
            model_name='product',
            name='attribute',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='product.attribute'),
        ),
    ]
