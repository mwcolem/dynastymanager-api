from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from player import Player

TEAM_URL = "https://www.fleaflicker.com/nfl/leagues/195647/teams/1318827"

players = []


def get_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    return BeautifulSoup(page, "html.parser")


def get_players_list():
    soup = get_soup(TEAM_URL)
    # roster_soup = soup.find_all('div', attrs={'class': 'player'})
    player_soup = soup.find_all('div', attrs={'class': 'player'})

    # < tr > < td
    # class ="left right" > < div class ="player" >
    # < div class ="player-name" >
    # < a class ="player-text" href="/nfl/leagues/195647/players/james-white-10475" id="ttId21_0" > James White < / a >
    # < / div >
    # < div class ="player-icons" > < i class ="fa fa-thumb-tack right-icon text-green tt-content" id="ttId3_2" > < / i > < / div >
    # < div class ="player-info" > < span class ="position" > RB < / span > < span class ="player-team" > NE < / span > < span class ="player-bye" > (10) < / span > < / div > < / div > < / td > < td class ="horizontal-spacer" > < / td >
    # < td class ="left" > < div class ="pro-opp-matchup" >
    # < div class ="pro-opp-matchup-weather" > < i class ="text-blue-dark fa fa-umbrella tt-content" id="ttId22_0" > < / i > < / div >
    # < a class ="tt-content" href="/nfl/boxscore?gameId=5897" id="ttId23_0" > PIT < span class ="pro-opp-matchup-info" > < span class ="nowrap" > Sun 8:20
    # PM < / span > < / span > < / a > < / div > < / td > < td
    # class ="right" > — < / td > < td class ="horizontal-spacer" > < / td > < td class ="left text-center" > < span class ="text-warning tt-content" id="ttId24_0" > RB31 < / span > < / td >
    # < td class ="text-center" > < i class ="icon-edge-E tt-content" id="ttId5_3" > < i class ="icon-edge" > < / i > < / i > < / td >
    # < td class ="right" > < span class ="text-success tt-content" id="ttId25_0" > 7 < / span > < / td >
    # < td class ="horizontal-spacer" > < / td > < td class ="left" > < span class ="fp" > 16.9 < / span > < / td > < td > < span class ="fp" > 13 < / span > < / td >
    # < td > < span class ="fp" > 12.52 < / span > < / td > < td class ="right" > < span class ="fp" > 17.3 < / span >
    # < div class ="fp-total" id="ttId26_0" > < span class ="fp" > 276.6 < / span > Total < / div > < / td >
    # < td class ="horizontal-spacer" > < / td > < td class ="left" > < span class ="tt-content" id="ttId13_2" >
    # < span class ="btn btn-default btn-xs disabled btn-block" > Locked < / span > < / span > < / td > < td class ="right" > < span class ="label label-success label-block" > RB < / span > < / td > < / tr >
    # for player_row in roster_soup:
    #     player = str(player_row.find('div', attrs={'class': 'player-name'}).getText())

    for player in player_soup:
        print(str(player.find('div').getText()))
        players.append(Player(str(player.find('div').getText())))

        # players.append(player)


    #     players.append(player_name)


# print(get_players_list())
get_players_list()
