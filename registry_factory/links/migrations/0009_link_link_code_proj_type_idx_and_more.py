# Generated by Django 5.0.3 on 2024-08-05 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0008_link_link_code_proj_type_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['link_code', 'project_id', 'link_type'], name='link_code_proj_type_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['link_code', 'project_id', 'account_id', 'link_type'], name='link_code_proj_acc_type_idx'),
        ),
    ]
