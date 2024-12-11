# Generated by Django 4.2 on 2024-04-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_alter_link_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['link_type'], name='links_link_type_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['object1', 'link_type', 'object2'], name='links_obj1_link_type_obj2_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['created_date'], name='links_created_date_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['modified_date'], name='links_modified_date_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['project_id', 'account_id', 'user_id'], name='links_prj_id_acc_id_usr_id_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['account_id', 'user_id'], name='links_account_id_user_id_idx'),
        ),
        migrations.AddIndex(
            model_name='link',
            index=models.Index(fields=['user_id'], name='links_user_id_idx'),
        ),
    ]
