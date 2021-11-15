import tekore as tk
import jsonpickle
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from events.factory.DAOFactory import DaoFactory
from auxbox.settings import client_id, client_secret, redirect_uri


class SpotifyHandler:

    # token request from the API to allow us to query the API for Data
    app_token = tk.request_client_token(client_id, client_secret)
    cred = tk.Credentials(client_id, client_secret, redirect_uri)

    def __init__(self):
        """
            Constructor used initialize the spotify handler instance, creating the spotify class object from tekore
        """
        self.auth: tk.UserAuth = None
        self.user_token: tk.RefreshingToken = None
        self.spotify = tk.Spotify(SpotifyHandler.app_token)

    def user_authentication(self):
        """
            Service method used to login the user through the spotify login page.
        """
        scope = tk.scope.read
        self.auth = tk.UserAuth(self.cred, scope)

    def create_user_token_after_redirect(self, request: WSGIRequest):
        """
            Service method used to create the user token after the redirection from the login

            :param request: the request received by the server after the redirect
        """
        self.auth = jsonpickle.decode(request.session['auth'])
        self.user_token = self.auth.request_token(url=request.get_raw_uri())

    def user_construct_for_creation(self):
        """
            Service method used to change the spotify class object from generic to user specific

            :return: spotify user object, with the user information
        """
        self.spotify.token = self.user_token
        return self.spotify.current_user()

    @staticmethod
    def check_user_authentication(request: WSGIRequest):
        refresh_token = request.session.get('token', False)
        # token does not exist
        if not refresh_token:
            return False

        # token exists but user not saved
        try:
            user = DaoFactory.getUserDao().get_by_spotify_id(refresh_token)
        except ObjectDoesNotExist:
            request.session['token'] = None
            return False

        # token does not match our saved token
        if user.spotify_id != refresh_token:
            request.session['token'] = None
            return False

        return user
