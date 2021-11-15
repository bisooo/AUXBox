from django.urls import path
from events.views.homepage import homepage
from events.views.create_event import create_event
from events.views.view_event import view_event
from events.views.aboutpage import aboutpage
from events.views.user_search import user_search
from events.views.add_friend import add_friend
from events.views.landing import landing
from events.views.profile import profile
from events.views.invites import invites
from events.views.invitationresponse import invitation_response


urlpatterns = [
    path('', homepage, name='home_page'),
    path('login/', landing, name='landing'),
    path('about/', aboutpage, name='about'),
    path('profile/', profile, name='profile'),
    path('profile/invites', invites, name='invites'),
    path('events/create', create_event, name='new_event'),
    path('events/<int:event_id>/', view_event, name='view_event'),
    path('events/<int:event_id>/user_search', user_search, name='user_search'),
    path('events/<int:event_id>/user_search/<int:user_id>', add_friend, name='add_friend'),
    path('profile/invites/<int:event_id>/<int:from_user_id>/<int:to_user_id>/<int:response>', invitation_response, name='invitation_response')
]

