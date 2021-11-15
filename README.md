# Description
AUXBox is a student created application that combines the classic crowd pleasing aspects of the Jukebox with the casualness of handing your friend the AUX cord of your cars stereo. Through the application the Hosts have access to a range of users to whom they can create and promote their events to. The users can then filter these events by genre, location, etc. join and invite their friends to them ; The aim of this project is to allow the users attending an event to influence the music being played. 

The system keeps track of the authorised Users & Hosts that have registered to connect their Spotify accounts through the application. It also keeps record of all the events created by Hosts and their different attributes such as location, time, date, description and genre. The DJs can view the events they are playing at and through the Spotify API link their event playlists. It also keeps track of the users events' comments and their upvotes of songs for an event playlist. 

To increase the chance of a song being played at an event ; a DJ can allow song requests and set a minimum price per request. The Users are limited to a single request per event where they can send a song to be played for a certain price. The DJ can accept the request with possible time slots that are suitable and if the User chooses one of the time slots then a notification is sent to the DJ about the time approval and song ; the transaction is then complete. The application should keep track of all the transactions and their status.

Any User has access via a web app where they can Login or Register by connecting their Spotify accounts ; they can then view all the events and their details or Host an event. The data from the application is backed up on a server to prevent losing information about users, events and transactions.

# System Architecture
`Auxbox:` This has the project settings, please do not play with this directory.

* events/Data:
    * Models: This is where we will store the entity tables (classes)
    * Dao: The dependency injection, ref for django is:
    http://www.programmersought.com/article/2814636229/
* events/Views: Where all of the routing and business logic will be stored
* events/Templates: This is where the html files are listed

We will be using SQLAlchemy for everything to do with the databases. 
Lookup `SQLAlchemy ORM`

`Note:` Whenever you create a new class, you should create a new file for it under the same directory to avoid any merge conflicts.

