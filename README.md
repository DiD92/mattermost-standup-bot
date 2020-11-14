# mattermost-standup-bot

This repo contains a basic standup bot that connects to a given mattermost instance and fetches the members of a configured channel in order to determine the participants in a standup meeting. The script itself is very simple and may be changed or improved at any point in time.

## Configuration values

This values need to be set in the `config.json` file in order for the script to work properly.

* **server_url**: This is your mattermost server URL, e.g: `mattermost.server.com` 

* **team_name**: The specific team in the server.

* **channel_name**: The channel within the team in which to look for the standup participants.

* **acess_token**: Your acces token used by the script to interact with the server.
