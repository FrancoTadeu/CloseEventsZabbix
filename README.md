# CloseEventsZabbix
Python Script to close all events in a specific Host Group.

To use this Script you'll need to set the ZabbixURL within the Script and, since I'm using the **dotenv** module. All you have to do is create and **.env** file in the same repository you're storing the script and change the ***api_token*** inside it, placing your Zabbix API token:

`api_token=7849345d922eeb13349c534a06249e06bb399a60b0dac9d1e1136a2c4540d16b`

Then when executing, you'll need to pass the Group Name as a parameter:

`python close_events.py "Your Host Group Name"`

Changing the ***message*** module content is possible as well. As you wish.

This is the first version and passible of modifications, future features will include filtering specific Triggers via regex.
