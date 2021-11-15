# Functional Requirements:
	1. Keep record of Users:
        * Priority: High
        * The system keeps record of the registered users by authorising their Spotify accounts through the Spotify API. Each User has a unique username. The users also have the option of linking their payment card and billing address for making or receiving payments. Each user has access to their personal data through their profile where they can modify their details.

	2. Keep record of tokens in each User account:
        * Priority: High
        * The system keeps a record of how many tokens are present in each user account.
        * The user can top-up tokens by making payments.
        * The user has the option to convert the tokens back into real money in their bank account, after reaching a minimum of 1000 tokens.

	3. Hosts create event:
        * Priority: High
        * Each user has the option to host an event on a certain date and time, where they can specify the location and set restrictions for the genres being played. Hosts mention a short description of the event. Hosts have the option to limit the number of upvotes per user. Hosts set the minimum token price for a song request from the user.

        3.1. Hosts link event playlists:
            * Priority: High
            * Hosts can link the playlist being played at the event by linking their pre-existing Spotify playlist using the Spotify API.

	4. Keep record of users attending for each event:
		*	Priority: Medium
		*	The system will keep a record of the users who have registered for an event. Each user can be registered for multiple events.

		4-1. Keep record of user interaction per event:
			* Priority: Medium
			* The system will keep track of the user’s upvotes and comments for each event.
		      The system keeps track of the limitations of the upvotes (if any) and will not allow
		      the user to upvote more if they have exceeded their upvote count.

	5. Requesting a song:
		* Priority: High
		* User send song requests to host within event genre restrictions. A user can use the token balance available. They can pay more tokens than the minimum amount specified in order to increases their chances of the host accepting their request. They have the option to add a short message to the host.

		* Host can view all the song requests for each event:
			* Priority: High
			* Host has the option to accept a song request, by responding with possible time periods where the song can be played. The user then can choose a time slot or decline the request within 48 hours of Host’s response.  If the user accepts the time slot, the Host needs to provide proof by recording a video of the song being played and using Shazam API we can verify if the song was played or not. If the song was not played, the user gets his money back.
	
    6. Keep record of user/host song transactions:
		* Priority: High
		* Keep records of all of the user/host transactions and their status which specifies whether the transactions were declined, accepted or in process.

# Non – Functional requirements:
	1. Web Application:
		* The client side (hosts and users) will have a web application interface accessible on a web browser.
		* The web application will be running on a third party server.
		* The application must be running in Microsoft Edge, Safari, FF 12+ and Chrome.

	2. Backup:
		* There needs to be a daily backup of the data stored in a separate database on FIT servers. The backup is to be executed at 6 am where the website generates the least amount of traffic.

	3. Server:
		* The backend of the web application will be stored on a third party server running Linux.

	4. Web application availability:
		* The web application needs to be available at least 90% of the time from 12 pm till 6 am. The rest of the time can be used for maintenance if need be.

	5. Server availability:
		* The server needs to be available at least 90% of the time from 12 pm till 6 am. The rest of the time can be used for maintenance if need be.

	6. Application colour theme:
		* The application interface will be dark themed with themes of sea-foam green and grey.
