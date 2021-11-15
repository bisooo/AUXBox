# Register:
    1. The User opens the website as they are prompted with a description of the web application.
    2. They find the 'Register' for new users button and click it
    3. The system then redirects them to a form to fill their firstname, lastname, username, email and password.
    4. The User then clicks on 'Authorize Spotify' button.
    5. The system redirects them to spotify's authentication using Spotify's API
    6. The User adds their spotify credentials.
    7. The system will then store the unique spotifyID.
    8. The user clicks on submit.
    9. The system validates the details of the form.
    10. The system then redirects the User to the Welcome page.

### Exception: Missing Mandatory information:
    1. The system detects the missing information and shows an error message to the user by highlighting the missing fields.
    2. The scenario returns to step 3 in the main scenario

### Exception: The username, email, spotifyID, already exist:
    1. The system detects the duplicate data and lets the user know with an error message.
    2. The system returns to step 3 in the main scenario


# Login:
    1. The User opens the website as they are prompted with a description of the web application.
    2. They find the 'Login' button and click it.
    3. The system then redirects them to a form to fill their username and password.
    4. The user clicks on submit.
    5. The system then validates to see if the information is correct or not.
    6. The system then redirects the User to the Home page.

### Exception: The user fills in wrong username/email or password:
    1. The system prompts the user of the error and asks them to double check their information and then click submit.
    2. After filling the new data, if the information is correct the scenario returns to step 6 in the main scenario.


# Request song:
    1. In the events page, the user finds the 'Request a song' button and clicks it.
    2. The system then opens a form to display to the user.
    3. The user finds an option to either request from all DJs or to send the request to a specific DJ.
    4. They then proceed to fill in the song they would like to have and/or a small description and choose their
    preferred time from the range of available slots if they have a preference.
    5. The system then validates the request.
    6. The system sends a confirmation to the user that the request is processed.

## Alternate Scenario: Step 3 - User chooses specific DJ
    1. The system adds a dropdown list to the form for the User to choose the DJ's name.
    2. The scenario returns to step 4 in the main scenario.

### Exception: Song already exists:
    1. The system detects the duplicate song as it is already in the list of played songs.
    2. The system notifies the user with a small error message and returns to step 2 in the main scenario.

### Exception: Song genre not the same as genres allowed in event:
    1. The system detects the song genre is not the same as the host provided.
    2. The system notifies the user with a small error message and returns to step 2 in the main scenario.

### Exception: Missing Mandatory information:
    1. The system detects the missing information and shows an error message to the user by highlighting the missing fields.
    2. The scenario returns to step 3 in the main scenario
    

# Create Event:
    1. A user decides they would like to host an event and clicks on 'Create Event' button on the homepage.
    2. The system redirects the user to a form to fill the event name, location, time period, date, description and minimum request price for a song.
    3. The user fills in the information and clicks submit.
    4. The system validates the data and redirects the user to their new events page.

### Exception: Mandatory Fields not filled out:
    1. System prompts User to fill out required fields before continuing. 
    2. The scenario returns to step 2 in the main scenario.

### Exception: Duplicate Event:
    1. System detects that event at this location, time, and with this name is already created and notifies the user with this error.
    2. The scenario returns to step 2 in the main scenario.


# Join Event:
    1. The user is on an Event's page that they are interested in and clicks on 'Join Event' button.
    2. The system then adds the user to the list of participants to the current event's page and gives them access to the event's contents.


# List Events:
    1. In the home page the user finds 'View nearby events' view and clicks it.
    2. The system then shows the user the list of events happening nearby by prioritizing events by the 
    date and then by amount of friends.
    3. The user can filter the view by selecting a specific genre, date or location.
    4. The system renders the view accordingly.


# List DJ and his Playlist(s):
    1. The user finds an event they are interested in and clicks on the event page.
    2. The system displays the event's details and renders the list of playlists with their corrosponding DJs.
    3. The user has the option to filter the view based on a certain DJ or all the DJ's.
    4. The system renders the view accordingly.
    

    
