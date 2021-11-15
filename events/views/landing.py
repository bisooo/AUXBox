from django.shortcuts import render, redirect
from events.services.spotifyHandler import SpotifyHandler
import jsonpickle


def landing(request):
    sp = SpotifyHandler()
    sp.user_authentication()
    request.session['auth'] = jsonpickle.encode(sp.auth)
    request.session.modified = True
    return redirect(sp.auth.url)
