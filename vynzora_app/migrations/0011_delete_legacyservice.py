# Generated manually.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vynzora_app", "0010_websiteservice"),
    ]

    operations = [
        migrations.DeleteModel(
            name="LegacyService",
        ),
    ]

