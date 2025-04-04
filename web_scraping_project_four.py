print("\033c")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
import pandas as pd
import numpy as np

BASE_URL = "https://www.scrapethissite.com/pages/forms/"

page_number = 1

while True:
    URL = f"{BASE_URL}?page_num={page_number}"
    page = requests.get(URL)
    time.sleep(3)

    if page.status_code != 200:
        print(f"Failed to retrieve page {page_number}. Stopping.")
        break


    soup = BeautifulSoup(page.content, 'html.parser')

    general_info = soup.find_all(class_ = 'table')
    # print(general_info)
    team_stats = soup.find_all(class_ = 'team')
    # print(team_stats)


    for stat in team_stats:
        name = stat.find(class_ = 'name').get_text(strip = True)
        year = stat.find(class_ = 'year').get_text(strip = True)
        wins = stat.find(class_ = 'wins').get_text(strip = True)
        losses = stat.find(class_ = 'losses').get_text(strip = True)
    
        ot_losses = stat.find(class_ = 'ot-losses')        
        if ot_losses:
            ot_losses_text = ot_losses.get_text(strip = True)
        else:
            ot_losses_text = None
    
        win_pct = stat.find(class_ = 'pct text-danger')
        if win_pct:
            win_pct_text = win_pct.get_text(strip = True)
        else:
            win_pct_text = None

        goals_for = stat.find(class_ = 'gf').get_text(strip = True)
        goals_against = stat.find(class_ = 'ga').get_text(strip = True)
    
        diff_success_text = (stat.find(class_ = 'diff text-success') or stat.find(class_ = 'diff text-danger'))
        if diff_success_text:
            diff_success_text = diff_success_text.get_text(strip = True)
        else:
            diff_success_text = None

        name_column = []
        year_column = []
        wins_column = []
        losses_column = []
        ot_losses_column = []
        win_percentage_column = []
        goals_for_column = []
        goals_against_column = []
        difference_column = []

        print(name)
        print(f"{year} Season:")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"OT Losses: {ot_losses_text}")
        print(f"Win Percentage: {win_pct_text}")
        print(f"Goals For: {goals_for}")
        print(f"Goals Against: {goals_against}")        
        print(f"Difference: {diff_success_text}")
        print()

    next_page = soup.find_all('a', {'aria-label': 'Next'})
    if next_page:
        page_number += 1
    else:
        print(f"End of pages. Stopping at page {page_number}")
        break


# Database of base_url: 'https://www.scrapethissite.com/pages/forms/'

columns = [
    'Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win Percentage',
    'Goals For', 'Goals Against', 'Difference']

hockey_df = pd.DataFrame()
