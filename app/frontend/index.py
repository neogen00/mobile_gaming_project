"""
Using Streamlit as front end. Basic functions and exploring different types of plots
"""

import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

API_URL_earnings = "http://127.0.0.1:5000/earnings"
API_URL_games = "http://127.0.0.1:5000/games"
API_URL_ratings = "http://127.0.0.1:5000/ratings"

def get_games():
    response = requests.get(API_URL_games)
    return response.json()

def get_earnings():
    response = requests.get(API_URL_earnings)
    return response.json()

def get_ratings():
    response = requests.get(API_URL_ratings)
    return response.json()

def game_revenue(earnings):
    return [earning['revenue'] for earning in earnings]

def game_downloads(downloads):
    return [download['downloads'] for download in downloads]

st.header('earnings')
earnings = get_earnings()
games_list = get_games()

x = game_downloads(earnings)
st.write("These are your downloads ", x)
y = game_revenue(earnings)
st.write("These are your revenues", y)


dF = pd.DataFrame(earnings)

games=['Among Us Android', 'Roblox Android', 'Candy Crush Saga Android', 'Among Us iOS']

fig = px.scatter(dF,x='downloads',y='revenue',hover_name=games,color="inapp",
    title="Game revenue vs downloads with inapp info")
st.plotly_chart(fig)

fig2 = px.bar(dF,x=games,y='downloads')
st.plotly_chart(fig2)

fig3 = go.Figure([go.Bar(x=games, y=y)])
st.plotly_chart(fig3)

game_df = pd.DataFrame(games_list)

st.table(game_df)

st.table(dF)

st.header('ratings')
ratings = get_ratings()
ratings_df = pd.DataFrame(ratings)

st.table(ratings_df)