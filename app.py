import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    #Api
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                 '}?api_key=8265bd1679663a7ea12ac168da84d2e8&languageen-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = dataset[dataset["title"] == movie].index[0]
    distance = simi[index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]

    reco = []
    reco_poster = []
    for i in movie_list:
        movie_id = dataset.iloc[i[0]].id
        reco.append(dataset.iloc[i[0]].title)
        reco_poster.append(fetch_poster(movie_id))
    return reco, reco_poster


dataset = pickle.load(open("movie predicter.pkl", "rb"))
simi = pickle.load(open("similarity.pkl", "rb"))
m_list = dataset["title"].values
#dataset = pd.read_pickle("movie predicter.pkl")


st.title('Movie Recommender')

selected_movie = st.selectbox("Seach your movie",m_list)
if st.button("Recommend"):
    names,posters = recommend(selected_movie)

    col0, col1, col2, col3,col4= st.columns(5)

    with col0:
        st.text(names[0])
        st.image(posters[0])
    with col1:
        st.text(names[1])
        st.image(posters[1])
    with col2:
        st.text(names[2])
        st.image(posters[2])
    with col3:
        st.text(names[3])
        st.image(posters[3])
    with col4:
        st.text(names[4])
        st.image(posters[4])
