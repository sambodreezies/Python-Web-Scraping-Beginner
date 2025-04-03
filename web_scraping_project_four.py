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
