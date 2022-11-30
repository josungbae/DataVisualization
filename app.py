from flask import Flask, request
from flask import render_template
import csv
from csv import DictReader

app = Flask(__name__)
# with open('./data/2020-08-19.csv', 'r') as f:
#     dict_reader = DictReader(f)
#     basic_data_old = list(dict_reader)
with open('./data/2022-01-08.csv', 'r') as f:
    dict_reader = DictReader(f)
    basic_data_new = list(dict_reader)
with open('./data/games_detailed_info.csv', 'r') as f:
    dict_reader = DictReader(f)
    detailed_data = list(dict_reader)
with open('./data/bgg-15m-reviews.csv', 'r') as f:
    dict_reader = DictReader(f)
    review_data_old = list(dict_reader)
# with open('./data/bgg-19m-reviews.csv', 'r') as f:
#     dict_reader = DictReader(f)
#     review_data_new = list(dict_reader)


@app.route("/")
def init():
    return "DataVisualization Project (Team 2) - API"

@app.route('/api')
def get_data():
    args = request.args
    source = args.get('data-source')
    
    if source == 'basic-data-old':
        game_id = args.get('game-id')
        content = args.get('content')
        data = [item for item in basic_data_old if item['ID']==game_id]
        if content == None:
            return data
        else:
            return [item[content] for item in data] 

    if source == 'basic-data-new':
        game_id = args.get('game-id')
        content = args.get('content')
        data = [item for item in basic_data_new if item['ID']==game_id]
        if content == None:
            return data
        else:
            return [item[content] for item in data]

    elif source == 'detailed-data':
        game_id = args.get('game-id')
        content = args.get('content')
        data = [item for item in detailed_data if item['id']==game_id]
        if content == None:
            return data
        else:
            return [item[content] for item in data]
    
    elif source == 'review-data-old':
        game_id = args.get('game-id')
        content = args.get('content')
        if content == None:
            return [item for item in review_data_old if item['ID']==game_id]  
        else:
            return [item[content] for item in review_data_old if item['ID']==game_id]

    # elif source == 'review-data-new':
    #     game_id = args.get('game-id')
    #     content = args.get('content')
    #     if content == None:
    #         return [item for item in review_data_new if item['ID']==game_id]
    #     else:
    #         return [item[content] for item in review_data_new if item['ID']==game_id]
    
    else:
        raise Exception('Error: wrong data source')

@app.route('/game_list')
def get_game_list():
    args = request.args
    mode = args.get('mode')

    if mode == 'all':
        return [item['id'] for item in detailed_data]
    if mode == 'top100':
        sorted_list = sorted(detailed_data, key = lambda x: int(x['Board Game Rank']) if x['Board Game Rank'].isdigit() else 1000000)
        return [item['id'] for item in sorted_list[:10]]
