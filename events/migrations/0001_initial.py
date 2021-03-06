# Generated by Django 3.0.10 on 2020-10-27 18:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The Event's name", max_length=50)),
                ('description', models.CharField(help_text='A short Event description', max_length=100)),
                ('spotify_genre', models.CharField(help_text="The Event's Genre", max_length=50)),
                ('location', models.CharField(help_text="The Event's location", max_length=50)),
                ('min_request_price', models.PositiveIntegerField(help_text='The minimum price per song request')),
                ('date', models.DateField(help_text='The Date of the Event')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='The Time of the Event')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(help_text='The ID of the Event', on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='The first name of the User', max_length=50)),
                ('last_name', models.CharField(help_text='The last name of the User', max_length=50)),
                ('username', models.CharField(help_text='The username of the User', max_length=50, unique=True)),
                ('email', models.EmailField(help_text='The email address of the User', max_length=254, unique=True)),
                ('spotify_id', models.CharField(help_text='The unique Spotify ID of the User', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_song', models.CharField(help_text='The Spotify song to be upvoted', max_length=50)),
                ('date', models.DateTimeField(auto_now=True, help_text='The date & time of the upvoting')),
                ('participation', models.ForeignKey(help_text='The Participation ID of the User in that Event ', on_delete=django.db.models.deletion.CASCADE, to='events.Participation')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(help_text='The price for the song request')),
                ('spotify_song', models.CharField(help_text='The Spotify link of the song requested', max_length=50)),
                ('request_date', models.DateTimeField(auto_now=True, help_text='The date & time when the song was requested')),
                ('state', models.CharField(help_text='The current status of the song request', max_length=50)),
                ('description', models.CharField(help_text='A short description for the song request', max_length=100)),
                ('event', models.ForeignKey(help_text='The ID of the Event where the request was posted', on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('host', models.ForeignKey(help_text='the ID of the Host specified for the song request ', on_delete=django.db.models.deletion.CASCADE, to='events.Host')),
                ('user', models.ForeignKey(help_text='The ID of the User sending the request', on_delete=django.db.models.deletion.CASCADE, to='events.User')),
            ],
        ),
        migrations.AddField(
            model_name='participation',
            name='user',
            field=models.ForeignKey(help_text='The ID of the User', on_delete=django.db.models.deletion.CASCADE, to='events.User'),
        ),
        migrations.AddField(
            model_name='host',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.User'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text="The user's comment", max_length=50)),
                ('date', models.DateTimeField(auto_now=True, help_text='The date & time of posting the comment')),
                ('participation', models.ForeignKey(help_text="The ID for the User's participation in an Event", on_delete=django.db.models.deletion.CASCADE, to='events.Participation')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together={('user', 'event')},
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True, help_text='The data & time of the invitation')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Rejected'), (1, 'Accepted'), (2, 'Pending')])),
                ('event', models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.Event')),
                ('from_user', models.ForeignKey(help_text='The ID of the User that sent the invitation', on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='events.User')),
                ('to_user', models.ForeignKey(help_text='The ID of the User invited', on_delete=django.db.models.deletion.CASCADE, to='events.User')),
            ],
            options={
                'unique_together': {('from_user', 'to_user')},
            },
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Rejected'), (1, 'Accepted'), (2, 'Pending')])),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='events.User')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='events.User')),
            ],
            options={
                'unique_together': {('requester', 'receiver')},
            },
        ),
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_set_time', models.DateTimeField(help_text="The starting time of a DJ's set")),
                ('end_set_time', models.DateTimeField(help_text="The ending time of a DJ's set")),
                ('spotify_playlist', models.CharField(help_text="The link to the DJ's set Spotify playlist", max_length=50)),
                ('event', models.ForeignKey(help_text="The Event's ID as a foreign key", on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('host', models.ForeignKey(help_text="The Host's ID as a foreign key", on_delete=django.db.models.deletion.CASCADE, to='events.Host')),
            ],
            options={
                'unique_together': {('host', 'event')},
            },
        ),
    ]
