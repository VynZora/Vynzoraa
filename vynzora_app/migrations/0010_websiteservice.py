# Generated manually (no Django installed in this environment)

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vynzora_app", "0009_legacy_service_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebsiteService",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("heading", models.CharField(max_length=200, verbose_name="Service Heading")),
                ("description", models.TextField(verbose_name="Service Description")),
                ("imported_at", models.DateTimeField(auto_now_add=True)),
                (
                    "website",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="vynzora_app.website",
                    ),
                ),
            ],
            options={
                "verbose_name": "Website Service",
                "verbose_name_plural": "Website Services",
            },
        ),
    ]

