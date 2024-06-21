# Generated by Django 5.0.4 on 2024-06-21 00:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("boards", "0002_initial"),
        ("likes", "0001_initial"),
        ("songs", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="boardlike",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_likes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="bookmark",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="board_bookmarks",
                to="boards.board",
            ),
        ),
        migrations.AddField(
            model_name="bookmark",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_bookmarks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="like",
            name="song",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="songs.song"
            ),
        ),
        migrations.AddField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddConstraint(
            model_name="boardlike",
            constraint=models.UniqueConstraint(
                fields=("user", "board"), name="unique_user_board_like"
            ),
        ),
        migrations.AddConstraint(
            model_name="bookmark",
            constraint=models.UniqueConstraint(
                fields=("user", "board"), name="unique_user_board_bookmark"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("song", "user")},
        ),
    ]
