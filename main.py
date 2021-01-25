import requests
import config
import json


class League:
    api_key = False

    def __init__(self):
        self.api_key = config.creds['api']['riot']

    def get_request(self, url, headers=False):
        r = requests.get(url, headers=headers)

        return r.json()

    def get_matchlist(self, region):
        url = 'https://canisback.com/matchId/matchlist_{}.json'.format(
            region.lower())
        data = self.get_request(url)

        return data

    def get_champion_name_by_id(self, id):
        with open('champion.json') as f:
            champion_data = json.load(f)

        return [name for name in champion_data['data'] if champion_data['data'][name]['key'] == id]

    def get_champion_id_by_name(self, name):
        with open('champion.json') as f:
            champion_data = json.load(f)

        return ''.join([key for key in champion_data['data'][name]['key'] if champion_data['data'][name]['name'] == name])


league = League()
print(league.get_champion_id_by_name('Aatrox'))
