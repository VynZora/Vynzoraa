# Generated manually (no Django installed in this environment)

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vynzora_app", "0008_alter_candidate_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="LegacyService",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("legacy_website_id", models.BigIntegerField()),
                ("legacy_website_slug", models.SlugField(blank=True, max_length=255, null=True)),
                ("legacy_website_name", models.CharField(blank=True, max_length=200, null=True)),
                ("heading", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("imported_at", models.DateTimeField(auto_now_add=True)),
                (
                    "website",
                    models.ForeignKey(
                        blank=True,
                        help_text="Optional mapping to current Website row (matched by legacy slug when possible).",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="legacy_services",
                        to="vynzora_app.website",
                    ),
                ),
            ],
            options={
                "db_table": "vynzora_app_legacyservice",
            },
        ),
        migrations.AddConstraint(
            model_name="legacyservice",
            constraint=models.UniqueConstraint(
                fields=("legacy_website_id", "heading"),
                name="uniq_legacyservice_site_heading",
            ),
        ),
    ]

