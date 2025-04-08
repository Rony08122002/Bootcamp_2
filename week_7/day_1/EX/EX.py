#1
import pandas as pd
import string
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")

data = {
    "Reviews": [
        "I don’t like the food here and the service was bad.",
        "I would not recommend this Japanese restaurant to anyone.",
        "The food this restaurant offers is related to Thailand, not Japan.",
        "The staff are friendly and helpful at Gyojin.",
        "The service is slow and the quality of Gyojin’s employees inconsistent.",
        "The authentic Thai food makes it intriguing, not the pasta dishes the children.",
        "I like the ramen options at Ramen Tatsu-ya. The miso ramen and the service was also nice.",
        "The staff at Sapporo Ramen are nice. The pork buns are delicious.",
        "The ramen selection at Ramen Tatsu-ya is very abundant and excellent snacks.",
        "The dessert selection at Sweet Treats is to die for!"
    ]
}

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [word for word in tokens if word not in STOP_WORDS]
    return " ".join(tokens)

df = pd.DataFrame(data)
df["Cleaned_Review"] = df["Reviews"].apply(preprocess_text)

def perform_ner(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def perform_pos_tagging(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

df["NER"] = df["Reviews"].apply(perform_ner)
df["POS"] = df["Reviews"].apply(perform_pos_tagging)

print(df.to_string())

#2
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

tokenized_sentences = [text.split() for text in df["Cleaned_Review"]]

model = Word2Vec(tokenized_sentences, vector_size=50, window=3, min_count=1, workers=1)

def plot_word_embeddings(model):
    words = list(model.wv.index_to_key)
    vectors = [model.wv[word] for word in words]
    pca = PCA(n_components=2)
    result = pca.fit_transform(vectors)
    plt.figure(figsize=(12, 8))
    plt.scatter(result[:, 0], result[:, 1])
    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))
    plt.title("Word2Vec Word Embeddings (2D PCA Projection)")
    plt.grid(True)
    plt.show()

plot_word_embeddings(model)
