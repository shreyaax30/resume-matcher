# Similarity & matching logic

 # TF-IDF + Cosine Similarity = How similar is the resume to the job overall?

 # CountVectorizer = What key skills or terms are missing? → Result: Missing: aws, git, rest

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# loads a pre-trained SBERT model
# 'all-MiniLM-L6-v2' - one of the most popular & lightweight SBERT models provided by the sentence-transformers lib
model = SentenceTransformer('all-MiniLM-L6-v2')

# upgrading from tf-idf to sbert
def calculate_bert_similarity(resume_text, jd_text):
    # Convert both to embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    # Calculate cosine similarity
    similarity_score = util.cos_sim(resume_embedding, jd_embedding).item()

    # Convert to %
    return round(similarity_score * 100, 2)



def calculate_similarity(resume_text, jd_text):
    # Combine the two texts
    documents = [resume_text, jd_text]

    # Create the TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Generate TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compute cosine similarity (result is a 2x2 matrix)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    # Convert to percentage
    match_score = round(similarity[0][0] * 100, 2)
    return match_score


# outputs set of the most frequent keywords
def get_keywords(text, top_n=20):
    # Extract top N keywords using term frequency
    vectorizer = CountVectorizer(stop_words='english')
    vectorizer.fit([text])
    return set(vectorizer.get_feature_names_out())   #convert it into a set() to remove duplicates



def find_keyword_matches(resume_text, jd_text):
    jd_keywords = get_keywords(jd_text)    #get the imp words from the jd
    resume_keywords = get_keywords(resume_text)     #imp words from the resume

    matched = jd_keywords.intersection(resume_keywords)     # Resume words that match JD keywords
    missing = jd_keywords - resume_keywords                 # JD words that are missing in the resume

    return matched, missing
