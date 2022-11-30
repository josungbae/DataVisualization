import requests
import pandas as pd
import numpy as np


def top100_games_info():
    """
    100위권 내 게임들의 basic-data 반환
    """
    top100_id_list = requests.get('http://127.0.0.1:5000/game_list?mode=top100')
    top100_id_list = top100_id_list.json()

    top100_basic_data = []
    for id in top100_id_list:
        game_info = requests.get('http://127.0.0.1:5000/api?data-source=basic-data-new&game-id='+id)
        top100_basic_data.append(game_info.json())

    return top100_basic_data

def top100_games_review():
    """
    100위권 내 게임들의 review 반환
    """
    top100_id_list = requests.get('http://127.0.0.1:5000/game_list?mode=top100')
    top100_id_list = top100_id_list.json()

    top100_review_data = []
    for id in top100_id_list:
        review = requests.get('http://127.0.0.1:5000/api?data-source=review-data-new&game-id='+id)
        top100_games_review.append(review.json())
    
    return top100_review_data



if __name__ == '__main__':
    print('basic data of top 100 games')
    print(top100_games_info())
