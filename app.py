import streamlit as st
import pickle
import requests



def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommened(movie):
    movie_index = movies_list[movies_list['title']== movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] # for top five recommendation

    recommened_movies = []
    recommened_movies_posters = []
    for i in movie_list:
        movie_id = movies_list.iloc[i[0]].movie_id

        recommened_movies.append(movies_list.iloc[i[0]].title)
        recommened_movies_posters.append(fetch_poster(movie_id))
    return recommened_movies,recommened_movies_posters

movies_list = pickle.load(open('movies.pkl','rb'))
movie = movies_list['title'].values


similarity = pickle.load(open("similarity.pkl",'rb'))
st.title("Movie Recommender System")

select_movie_name= st.selectbox(
    'How would you like to be contacted?',
    movie)

if st.button('Recommened'):
    names,poster = recommened(select_movie_name)
    col1, col2, col3,col4,col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])
