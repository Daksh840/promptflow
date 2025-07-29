from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity_metric(response1, response2):
    vec = TfidfVectorizer().fit_transform([response1, response2])
    return cosine_similarity(vec[0:1], vec[1:2])[0][0]

def tone_match(response, desired_tone="formal"):
    return desired_tone in response.lower()  # crude example
