import nltk

# Verifica si los recursos están instalados
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Descargando recursos de NLTK...")
    nltk.download('punkt')
    nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

def analyze_text(text):
    # Tokenización
    tokens = word_tokenize(text.lower())
    
    # Limpieza: eliminar stopwords y puntuación
    stop_words = set(stopwords.words('spanish'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    
    # Conteo de palabras
    word_count = Counter(filtered_tokens)
    
    return word_count

def print_results(word_count):
    print("Conteo de palabras:")
    for word, count in word_count.most_common(10):  # Muestra las 10 palabras más comunes
        print(f"{word}: {count}")

# Ejemplo de uso
if __name__ == "__main__":
    text = input("Ingresa el texto que deseas analizar: ")
    result = analyze_text(text)
    print_results(result)