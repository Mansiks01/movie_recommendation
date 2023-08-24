from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_similarity(movie):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movie['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity
