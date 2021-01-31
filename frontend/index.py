import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import streamlit as st


API_URL_games = "http://127.0.0.1:5000/games"
API_URL_earnings_search = "http://127.0.0.1:5000/games/earnings/search"
API_URL_RPD = "http://127.0.0.1:5000/games/earnings/RPD"
API_URL_ratings_all = "http://127.0.0.1:5000/games/all_data"


def get_games():
    response = requests.get(API_URL_games)
    return response.json()

def get_earnings_games():
    response = requests.get(API_URL_earnings_search)
    return response.json()

def get_RPD():
    response = requests.get(API_URL_RPD)
    return response.json()

def get_ratings_all():
    response = requests.get(API_URL_ratings_all)
    return response.json()


st.title("Mobile Gaming Analytics")
st.write("By Christopher Santos")
st.header("Gaming the mobile gaming industry with metrics and stats")
st.write("Different app stores i.e. (Google Play, App Store, etc.) each have their top app lists for users to see which game is trending.")
st.write("Below is a chart containing revenue and download info for the top 10 of each list:")


ratings_all = get_ratings_all()
ratings_df = pd.DataFrame(ratings_all)
ratings_df = ratings_df.drop('game',1).assign(**ratings_df.game.apply(pd.Series))
ratings_df = ratings_df.drop('earnings',1).assign(**ratings_df.earnings.apply(pd.Series))

fig_all = px.scatter(ratings_df,x='downloads',y='revenue',
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

ra_search = ratings_df.loc[(ratings_df['rank_type']==rank_type) & (ratings_df['platform']==os_type)]
fig_r = px.scatter(ra_search,x='downloads',y='revenue',hover_name='name',
        hover_data=['platform', 'publisher'],
        color='genre', template='plotly_dark',
        title="Sorted game revenue vs downloads with genre colormap")
st.plotly_chart(fig_r)


games_list = get_games()

def game_name(games_list):
    return [game['name'] for game in games_list]

st.write("Want to compare how two games do on the rankings? type/select each game (note: the sidebar filters are also attached to the ranking chart)")

games_collection = game_name(games_list)
game_search1 = st.selectbox("game1", games_collection) 
game_search2 = st.selectbox("game2", games_collection)

top_10_rank = ra_search.loc[(ra_search['name']==game_search1) | (ra_search['name']==game_search2)]
top_10_rank = top_10_rank.sort_values(by='date_created')

try:
    fig_rankings = px.line(top_10_rank, x='date_created', y='ranking', 
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
  hover_data=['inapp','platform', 'publisher'],
  color='shows_ads',template='plotly_white',
  title="Game revenue vs downloads with showing ads data")

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
