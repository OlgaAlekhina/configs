from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Config'.lower(),
            name='object_item',
            field=models.UUIDField(default=None, null=True),
        ),
    ]
