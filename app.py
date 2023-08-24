import pickle
import helper
import streamlit as st

movie = pickle.load(open('movies.pkl', 'rb'))


def recommend(movie_name):
    similarity = helper.get_similarity(movie)
    try:
        movie_index = movie[movie['title'] == movie_name].index[0]
        distance = similarity[movie_index]
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    except IndexError:
        st.title('No movies found.')
        movie_list = None
    return movie_list
    # for i in movie_list:
    #     print(movie.iloc[i[0]].title)


movie_name = st.text_input('Enter any movie name')
if st.button('Recommend'):
    movies = recommend(movie_name.strip())
    if movies is not None:
        for i in movies:
            st.title(movie.iloc[i[0]].title)
