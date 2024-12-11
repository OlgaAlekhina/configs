import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0002_alter_object_item'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='Config'.lower(),
            index=django.contrib.postgres.indexes.GinIndex(fields=['data'], name='configs_data_gin'),
        ),
        migrations.AddIndex(
            model_name='Config'.lower(),
            index=models.Index(fields=['object_item'], name='configs_object_item_idx'),
        ),
    ]
