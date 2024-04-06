import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentence = [
    'import tensorflow as tf',
    'from tensorflow import keras',
    'from tensorflow.keras.preprocessing.text aa'
]

# 自然语言处理，词条化，序列化
tokenizer = Tokenizer(num_words=100, oov_token="<00V>")
tokenizer.fit_on_texts(sentence)
word_index = tokenizer.word_index
print('word_index = ', word_index)

sequences = tokenizer.texts_to_sequences(sentence)
print('sequence = ', sequences)

test_sentence = [
    'import tensorflow as tf',
    'accuracy is enough! stopping training'
]
test_sequences = tokenizer.texts_to_sequences(test_sentence)

paded = pad_sequences(test_sequences, padding='post', maxlen=5)
print('pad = ', +paded)
