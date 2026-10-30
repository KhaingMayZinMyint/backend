from django.db import migrations


def create_missing_tables(apps, schema_editor):
    existing_tables = set(
        schema_editor.connection.introspection.table_names()
    )

    model_names = [
        "Tag",
        "Comment",
        "UserProfile",
        "PostTag",
        "PostLike",
    ]

    for model_name in model_names:
        model = apps.get_model("blog", model_name)
        table_name = model._meta.db_table

        if table_name not in existing_tables:
            schema_editor.create_model(model)
            existing_tables.add(table_name)


class Migration(migrations.Migration):

    atomic = False 

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_missing_tables,
            reverse_code=migrations.RunPython.noop,
        ),
    ]