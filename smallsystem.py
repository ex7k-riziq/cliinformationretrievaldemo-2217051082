import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

folder_path = 'D:/UASTKI/documents'
docs = []
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        doc = file.read()
        docs.append(doc)

preprocessed_docs = []
for doc in docs:
    preprocessed_doc = []
    for line in doc.split('\n'):
        if ':' in line:
            line = line.split(':')[1].strip()
        words = line.split()
        words = [word for word in words if word.lower() not in stop_words]
        words = [stemmer.stem(word) for word in words]
        preprocessed_doc.extend(words)
    preprocessed_doc = ' '.join(preprocessed_doc)
    preprocessed_docs.append(preprocessed_doc)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_docs)

query = ''
query = input('\nEnter your query: ')

preprocessed_query = []
for word in query.split():
  if word.lower() not in stop_words:
    word = stemmer.stem(word)
    preprocessed_query.append(word)
preprocessed_query = ' '.join(preprocessed_query)

cosine_similarities = tfidf_matrix.dot(
  vectorizer.transform([preprocessed_query]).T).toarray().flatten()

most_similar_doc_index = cosine_similarities.argsort()[::-1][0]
most_similar_doc = docs[most_similar_doc_index]
similarity_score = cosine_similarities[most_similar_doc_index]

print(f"\n--- Query Results ---")
print(f"Processed Query: '{preprocessed_query}'")
print(f"Most Similar Document Index: {most_similar_doc_index}")
print(f"Similarity Score: {similarity_score:.4f}")
print(f"Most Similar Document (snippet): {most_similar_doc[:500]}...")

print("\nOccurrences of query words in the most similar document (up to 5 relevant lines):")
query_words_stemmed = preprocessed_query.split()
found_in_lines = []

if query_words_stemmed:
    for i, line in enumerate(most_similar_doc.split('\n')):
        temp_line_words = [stemmer.stem(word) for word in line.lower().split()
                           if word not in stop_words]
        for q_word in query_words_stemmed:
            if q_word in temp_line_words:
                found_in_lines.append(f"Line {i+1}: {line.strip()}")
                break

if found_in_lines:
    for f_line in found_in_lines[:5]:
        print(f"- {f_line}")
    if len(found_in_lines) > 5:
        print(f"... and {len(found_in_lines) - 5} more lines containing query words.")
else:
    print("No direct occurrences of stemmed query words found in the document lines.")

print("---------------------\n")