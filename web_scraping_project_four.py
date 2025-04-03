print("\033c")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

URL = "https://www.scrapethissite.com/pages/forms/"
page = requests.get(URL)
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
    
    
    # ot_losses = while True stat.find(class_ = 'ot-losses').get_text(strip = True) else: print('NA')        
    # print(ot_losses)
    
    # win_pct = stat.find(class_ = 'pct text-danger').get_text(strip = True)
    goals_for = stat.find(class_ = 'gf').get_text(strip = True)
    goals_against = stat.find(class_ = 'ga').get_text(strip = True)
    
    
    

    print(name)
    print(f"{year} Season:")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    
    # print(f"Win Percentage: {win_pct}"")
    print(f"Goals For: {goals_for}")
    print(f"Goals Against: {goals_against}")

    diff_success = stat.find(class_ = 'diff text-success')
    if diff_success:
        diff_success_text = diff_success.get_text(strip = True)
    else:
        diff_success_text = None
        
    print(f"Difference: {diff_success}")
    print()