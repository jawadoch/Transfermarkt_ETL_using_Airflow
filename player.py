import pandas as pd
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

class Player:
    def __init__(self, player, post, age, market_value, nat, joined, league, fee):
        self.PlayerName = player
        self.Post = post
        self.Age = age
        self.MarketValue = market_value
        self.Nationality= nat
        self.TeamJoined = joined
        self.League = league
        self.Fee = fee

def get_data(page):
    url=f"https://www.transfermarkt.com/statistik/saisontransfers?ajax=yw0&page={page}"
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
                  "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1",
                  "Connection":"close", "Upgrade-Insecure-Requests":"100"}
    page= requests.get(url, headers= headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', class_='items')
    rows = table.find_all('tr', class_=['odd', 'even'])
    players = []
    for row in rows:
        name=row.find_all('td')[1].find('a').text
        post=row.find_all('tr')[1].find('td').text
        age=row.find_all('td')[5].text
        market_value=row.find_all('td')[6].text.replace('€', '').strip()
        nat=row.find_all('td')[7].find('img')['alt']
        joined=row.find_all('td')[8].find_all('a')[0]['title']
        legue=row.find_all('td')[8].find_all('a')[2]['title']
        fee=row.find_all('td')[12].text.replace('€', '').strip()
        player = Player(name, post, age, market_value, nat, joined, legue, fee)
        players.append(player)
    players = [vars(player) for player in players]
    df = pd.DataFrame(players)
    return df

def convertir_valeur(valeur):
    if isinstance(valeur, str):
        if 'k' in valeur and len(valeur) < 10:
            return float(valeur.replace('k', '')) / 1000
        elif 'm' in valeur and len(valeur) < 10:
            return float(valeur.replace('m', ''))
        elif 'Loan fee' in valeur:
            value = valeur.split(":")[1]
            if 'k' in value:
                return float(value.replace('k', '')) / 1000
            elif 'm' in value:
                return float(value.replace('m', ''))
        else:
            try:
                return float(valeur)
            except ValueError:
                return valeur
    else:
        return valeur



def get_trans():
    df = [get_data(i) for i in range(1,2)]
    df=pd.concat(df)
    df.index = range(1, len(df) + 1)
    return df


def transform(dataf):
    dataf['market_value'] = dataf['market_value'].apply(convertir_valeur)
    dataf['fee'] = dataf['fee'].apply(convertir_valeur)
    return dataf

def save_to_mongodb(dataframe):
    mongo_url = 'mongodb://localhost:27017'
    database_name = 'transfers_db'
    collection_name='players'
    client = MongoClient(mongo_url)
    db = client[database_name]
    data_dict = dataframe.to_dict(orient='records')
    db[collection_name].insert_many(data_dict)
    client.close()



def print_done():
    print('done')
