"""
Using Streamlit as front end
"""

import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

API_URL_earnings = "http://127.0.0.1:5000/earnings"
API_URL_games = "http://127.0.0.1:5000/games"
API_URL_earnings_games = "http://127.0.0.1:5000/earnings/games"
API_URL_ratings = "http://127.0.0.1:5000/ratings"
API_URL_ratings_all = "http://127.0.0.1:5000/ratings/all_data"

def get_games():
    response = requests.get(API_URL_games)
    return response.json()
def get_earnings():
    response = requests.get(API_URL_earnings)
    return response.json()
def get_earnings_games():
    response = requests.get(API_URL_earnings_games)
    return response.json()
def get_ratings():
    response = requests.get(API_URL_ratings)
    return response.json()
def get_ratings_all():
    response = requests.get(API_URL_ratings_all)
    return response.json()


def game_revenue(earnings):
    return [earning['revenue'] for earning in earnings]

def game_downloads(downloads):
    return [download['downloads'] for download in downloads]

st.title("Mobile Gaming Analytics")
st.write("By Christopher Santos")
st.header("Gaming the mobile gaming industry with metrics and stats")
st.write("Different app stores i.e. (Google Play, App Store, etc.) each have their top app lists for users to see which game is trending.")
st.write("Below is a chart containing revenue and download info for the top 10 of each list:")

earnings = get_earnings()
games_list = get_games()

def game_name(games_list):
    return [game['name'] for game in games_list]

ratings_all = get_ratings_all()

def rating_name(ratings_all):
    return [rating['game']['name'] for rating in ratings_all]
def rating_os(ratings_all):
    return [rating['game']['platform'] for rating in ratings_all]
def rating_downloads(ratings_all):
    return [rating['earnings']['downloads'] for rating in ratings_all]
def rating_revenue(ratings_all):
    return [rating['earnings']['revenue'] for rating in ratings_all]
def rating_genre(ratings_all):
    return [rating['game']['genre'] for rating in ratings_all]


ra_df = pd.DataFrame(ratings_all)
ra1_df = ra_df.drop('game',1).assign(**ra_df.game.apply(pd.Series))
ra2_df = ra1_df.drop('earnings',1).assign(**ra1_df.earnings.apply(pd.Series))

fig_all = px.scatter(ra2_df,x='downloads',y='revenue',
    hover_name='name',hover_data=['platform', 'publisher'],
  color='genre', template='plotly_dark',
  title="All game revenue vs downloads with genre colormap")
st.plotly_chart(fig_all)

st.write("From the combined chart above, you can interact with the following chart to focus on the top 10 ranking type and gaming platform:")

left_column, right_column = st.beta_columns(2)
with right_column:
    rank_type = st.sidebar.radio(
        'Sorting rank type',
        ('top free', 'top paid', 'top grossing')
    )
with left_column:
    os_type = st.sidebar.radio(
        'Sorting platform',
        ('android', 'iOS')
    )


ra_search = ra2_df.loc[(ra2_df['rank_type']==rank_type) & (ra2_df['platform']==os_type)]
fig_r = px.scatter(ra_search,x='downloads',y='revenue',hover_name='name',
        hover_data=['platform', 'publisher'],
        color='genre', template='plotly_dark',
        title="Sorted game revenue vs downloads with genre colormap")
st.plotly_chart(fig_r)


st.write("Want to compare how two games do on the rankings? type/select each game (note: the sidebar filters are also attached to the ranking chart)")

games_collection = game_name(games_list)
game_search1 = st.selectbox("game1", games_collection) 
game_search2 = st.selectbox("game2", games_collection)
ra_game1 = ra2_df.loc[(ra2_df['name']==game_search1) & (ra2_df['rank_type']==rank_type)]
ra_game2 = ra_search.loc[(ra2_df['name']==game_search1) | (ra2_df['name']==game_search2)]
ra_game2 = ra_game2.sort_values(by='date_created')

try:
    fig_rankings = px.line(ra_game2, x='date_created', y='ranking', 
        color='name', template='plotly_white', 
        title='Ranking by date')
    fig_rankings.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_rankings)
except KeyError:
    st.error('Plot cannot be found, try another game with correct rank type / platform')


st.write("Roblox is an example of high revenue on both platforms, where Among Us! is high revenue only on iOS and Among Us android has high downloads/low revenue.")
st.write("Another finding in genre analysis: the adventure category has the top earners, with casual following.")
st.write("High counts in downloads does not guarantee high revenue, but it does give good exposure to be added on the top free list.")
st.write("Feel free to explore and see what other insights this data shows and hopefully you can make decisions in your next game dev!")

game_earnings = get_earnings_games()
ge_df = pd.DataFrame(game_earnings)
dF = ge_df.drop('game',1).assign(**ge_df.game.apply(pd.Series))


fig = px.scatter(dF,x='downloads',y='revenue',hover_name='name',
  color='inapp',template='plotly_white',
  title="Game revenue vs downloads with in app purchases info")

st.plotly_chart(fig)

fig_b = px.scatter(dF,x='downloads',y='revenue',hover_name='name',
  color='price',template='plotly_white',
  title="Game revenue vs downloads with price info")
st.plotly_chart(fig_b)

dF['RPD'] = dF['revenue'] / dF['downloads']
dF = dF[dF['RPD']  > 1 ]
dF = dF.sort_values(by='RPD', ascending=False)

fig3 = px.bar(dF,x='name',y='RPD',template='plotly_white',title='Revenue Per Download')
st.plotly_chart(fig3)

st.write("Thanks to TowerSenor, IGDB, and RAWG for all the data used in this project!")
