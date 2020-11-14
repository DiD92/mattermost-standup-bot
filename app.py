import json
from typing import List, Dict, Optional

from mattermostdriver import Driver

if __name__ == "__main__":

    config_data = get_server_config('config.json')

    if not config_data:
        print('Invalid config file!')
        exit(1)

    server_config = {
        'url': config_data['url'],
        'token': config_data['access_token']
    }

    channel_members = get_standup_members(server_config)

    for member in channel_members:
        print(f"Member turn {member}")
        _ = input()
    
    print("Bye bye!")

    exit(0)


def get_server_config(config_file_path: str) -> Optional[Dict]:
    try:
        config_data = None
        with open('config.json', 'r') as cfg:
            config_data = json.load(cfg)
        return config_data
    except IOError:
        return None


def get_standup_members(server_config: Dict) -> List[str]: 
    d = Driver(server_config)

    d.login()

    channel_id = d.channels.get_channel_by_name_and_team_name('team_name', 'channel')['id']

    channel_members = d.channels.get_channel_members(channel_id)

    d.logout()

    return channel_members
