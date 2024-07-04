from BasketballReferenceLinks import BasketBallReferenceLinks
from datetime import datetime, timedelta
import calendar
from requests import get
from bs4 import BeautifulSoup
import unicodedata
import unidecode
import requests
from bs4 import Comment
import pandas as pd
import lxml
import os

class Scraper:
    def __init__(self):
        self.month_dict = {
            1: "january",
            2: "february",
            3: "march",
            4: "april",
            5: "may",
            6: "june",
            7: "july",
            8: "august",
            9: "september",
            10: "october",
            11: "november",
            12: "december",
        }

    @staticmethod
    def get_team_standings(year):
        stat_link = BasketBallReferenceLinks.team_standings.format(year=year)
        df_east = pd.read_html(stat_link)[0]
        df_west = pd.read_html(stat_link)[1]
        
        # Add a conference column to each DataFrame
        df_east['Conference'] = 'Eastern Conference'
        df_west['Conference'] = 'Western Conference'
        
        # Combine both DataFrames
        combined_df = pd.concat([df_east, df_west], ignore_index=True)
        
        return combined_df

if __name__ == "__main__":
    bs_scraper = Scraper()

    # Create the 'data' folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    paths = {
        'team_roster': f'data/team_roster',
        'player_game_log': f'data/player_game_logs',
        'injuries': 'data/injuries',
        'player_per_game_stats': f'data/player_per_game_stats',
        'player_per_36_stats': f'data/player_per_36_stats',
        'player_per_100_stats': f'data/player_per_100_stats',
        'player_play_by_play_stats': f'data/player_play_by_play_stats',
        'player_advanced_stats': f'data/player_advanced_stats',
        'player_shooting_stats': f'data/player_shooting_stats',
        'team_ratings': f'data/team_ratings',
        'all_games': f'data/all_games',
        'team_standings': f'data/team_standings',
        'player_points_total': f'data/player_points_total',
    }

    # Create subdirectories for each stat type
    for path in paths.values():
        if not os.path.exists(path):
            os.makedirs(path)

    team_standings = bs_scraper.get_team_standings('2022')
    team_standings.to_csv(f'data/team_standings/team_standings_{2022}.csv', index=False)

    print(21)