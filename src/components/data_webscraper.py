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
import time
import html5lib

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

    # TEAM STANDINGS FUNCTION
    @staticmethod
    def get_team_standings(year):
        stat_link = BasketBallReferenceLinks.team_standings.format(year=year)
        df_east = pd.read_html(stat_link)[0]
        df_west = pd.read_html(stat_link)[1]
        
        # Rename "Eastern/Western Conference" column to "Team"
        df_east.rename(columns={'Eastern Conference': 'Team'}, inplace=True)
        df_west.rename(columns={'Western Conference': 'Team'}, inplace=True)

        # Adding the new column "Conference"
        df_east['Conference'] = 'E'
        df_west['Conference'] = 'W'

        # Combine both DataFrames
        combined_df = pd.concat([df_east, df_west], ignore_index=True)
        
        return combined_df
    
    # PLAYER TOTAL STATS FUNCTION
    @staticmethod
    def get_player_points_total(year):
        stat_link = BasketBallReferenceLinks.player_point_totals.format(year=year)
        return pd.read_html(stat_link)[0]
    
    # PLAYER PER GAME STATS FUNCTION
    @staticmethod
    def get_player_per_game_stats(year):
        stat_link = BasketBallReferenceLinks.player_per_game_stats.format(year=year)
        return pd.read_html(stat_link)[0]
    
    # PLAYER PER 36 FUNCTION
    @staticmethod
    def get_player_36_stats(year):
        stat_link = BasketBallReferenceLinks.player_per_36_stats.format(year=year)
        return pd.read_html(stat_link)[0]

    # PLAYER PER 100 POSS FUNCTION
    @staticmethod
    def get_player_100_stats(year):
        stat_link = BasketBallReferenceLinks.player_per_100_stats.format(year=year)
        return pd.read_html(stat_link)[0]

    # PLAYER PLAY BY PLAY FUNCTION
    @staticmethod
    def get_player_play_by_play_stats(year):
        stat_link = BasketBallReferenceLinks.player_play_by_play_stats.format(year=year)
        return pd.read_html(stat_link)[0]

    # PLAYER ADVANCED STATS FUNCTION
    @staticmethod
    def get_player_advanced_stats(year):
        stat_link = BasketBallReferenceLinks.player_advanced_stats.format(year=year)
        return pd.read_html(stat_link)[0]

    # PLAYER SHOOTING STATS FUNCTION
    @staticmethod
    def get_player_shooting_stats(year):
        stat_link = BasketBallReferenceLinks.player_shooting.format(year=year)
        return pd.read_html(stat_link)[0]

    # PLAYER ADJUSTED SHOOTING FUNCTION
    @staticmethod
    def get_player_adjusted_shooting_stats(year):
        stat_link = BasketBallReferenceLinks.player_adjusted_shooting.format(year=year)
        return pd.read_html(stat_link)[2]

    # TEAM RATINGS FUNCTION
    @staticmethod
    def get_team_ratings(year):
        stat_link = BasketBallReferenceLinks.team_ratings.format(year=year)
        return pd.read_html(stat_link)[0]
    
    # TEAM ROSTER FUNCTION
    @staticmethod
    def get_team_roster(year, team_abv):
        stat_link = BasketBallReferenceLinks.team_roster.format(
            year=year, team_abv=team_abv
        )
        return pd.read_html(stat_link)[0]

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
        'player_adjusted_shooting_stats': f'data/player_adjusted_shooting_stats',
        'team_ratings': f'data/team_ratings',
        'all_games': f'data/all_games',
        'team_standings': f'data/team_standings',
        'player_points_total': f'data/player_points_total',
    }

    # Create subdirectories for each stat type
    for path in paths.values():
        if not os.path.exists(path):
            os.makedirs(path)

    # Year range variable
    year_range = range(2000,2025)

    # Team Standings
    # for year in year_range:
    #     try:
    #         team_standings = bs_scraper.get_team_standings(str(year))
    #         team_standings.to_csv(f'data/team_standings/team_standings_{year}.csv', index=False)
    #         print(f"Data for Team Standings {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Team Standings {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Per Game Stats
    # for year in year_range:
    #     try:
    #         player_per_game_stats = bs_scraper.get_player_per_game_stats(str(year))
    #         player_per_game_stats.to_csv(f'data/player_per_game_stats/player_per_game_stats_{year}.csv', index=False)
    #         print(f"Data for Player Per Game Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Per Game Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Total Stats
    # for year in year_range:
    #     try:
    #         player_points_total = bs_scraper.get_player_points_total(str(year))
    #         player_points_total.to_csv(f'data/player_points_total/player_points_total_{year}.csv', index=False)
    #         print(f"Data for Player Total Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Total Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Per 36 Stats
    # for year in year_range:
    #     try:
    #         player_per_36_stats = bs_scraper.get_player_36_stats(str(year))
    #         player_per_36_stats.to_csv(f'data/player_per_36_stats/player_per_36_stats_{year}.csv', index=False)
    #         print(f"Data for Player Per 36 Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Per 36 Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Per 100 Stats
    # for year in year_range:
    #     try:
    #         player_per_100_stats = bs_scraper.get_player_100_stats(str(year))
    #         player_per_100_stats.to_csv(f'data/player_per_100_stats/player_per_100_stats_{year}.csv', index=False)
    #         print(f"Data for Player Per 100 Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Per 100 Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Play By Play Stats
    # for year in year_range:
    #     try:
    #         player_play_by_play_stats = bs_scraper.get_player_play_by_play_stats(str(year))
    #         player_play_by_play_stats.to_csv(f'data/player_play_by_play_stats/player_play_by_play_stats_{year}.csv', index=False)
    #         print(f"Data for Player Play By Play Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Play By Play Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Advanced Stats
    # for year in year_range:
    #     try:
    #         player_advanced_stats = bs_scraper.get_player_advanced_stats(str(year))
    #         player_advanced_stats.to_csv(f'data/player_advanced_stats/player_advanced_stats_{year}.csv', index=False)
    #         print(f"Data for Player Advanced Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Advanced Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Shooting Stats
    # for year in year_range:
    #     try:
    #         player_shooting_stats = bs_scraper.get_player_shooting_stats(str(year))
    #         player_shooting_stats.to_csv(f'data/player_shooting_stats/player_shooting_stats_{year}.csv', index=False)
    #         print(f"Data for Player Shooting Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Shooting Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Player Adjusted Shooting Stats - DEPRECIATED: NEEDS FIX
    # for year in year_range:
    #     try:
    #         player_adjusted_shooting_stats = bs_scraper.get_player_adjusted_shooting_stats(str(year))
    #         player_adjusted_shooting_stats.to_csv(f'data/player_adjusted_shooting_stats/player_adjusted_shooting_stats_{year}.csv', index=False)
    #         print(f"Data for Player Adjusted Shooting Stats {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Player Adjusted Shooting Stats {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Team Ratings
    # for year in year_range:
    #     try:
    #         team_ratings = bs_scraper.get_team_ratings(str(year))
    #         team_ratings.to_csv(f'data/team_ratings/team_ratings_{year}.csv', index=False)
    #         print(f"Data for Team Ratings {year} saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to retrieve data for Team Ratings {year}: {e}")
        
    #     # Pause for 5 seconds between requests to avoid hitting the request limit
    #     time.sleep(5)

    # Team Roster
    # Creating directories for year then team
    for year in year_range:
        year_dir = os.path.join('data/team_roster', str(year))  # Path for the year directory
        os.makedirs(year_dir, exist_ok=True)  # Create the year directory if it doesn't exist

    # Scraping Team Roster
    for team in BasketBallReferenceLinks.team_names:
        for year in year_range:
            try:
                team_roster = bs_scraper.get_team_roster(str(year), team_abv=team.upper())
                team_roster.to_csv(f'data/team_roster/{year}/{team.upper()}_{year}.csv', index=False)
                print(f"Data for Team Roster {year} saved successfully.")
            except Exception as e:
                print(f"Failed to retrieve data for Team Roster {year}: {e}")
            
            # Pause for 5 seconds between requests to avoid hitting the request limit
            time.sleep(5)

    # player_adjusted_shooting_stats = bs_scraper.get_player_adjusted_shooting_stats(str(2024))
    # player_adjusted_shooting_stats.to_csv(f'data/player_adjusted_shooting_stats/player_adjusted_shooting_stats_{2024}.csv', index=False)

    print(21)