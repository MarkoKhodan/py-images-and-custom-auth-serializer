# Generated by Django 4.0.4 on 2022-09-05 14:16

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_username"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", user.models.UserManager()),
            ],
        ),
    ]
