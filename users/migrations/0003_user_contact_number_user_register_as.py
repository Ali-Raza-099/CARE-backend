# Generated by Django 4.1.7 on 2023-03-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_name_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="contact_number",
            field=models.CharField(default="00000000000", max_length=255),
        ),
        migrations.AddField(
            model_name="user",
            name="register_as",
            field=models.CharField(default="individual", max_length=255),
        ),
    ]