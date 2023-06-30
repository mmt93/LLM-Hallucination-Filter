from difflib import SequenceMatcher

def similar(a, b):
  return SequenceMatcher(None, a, b).ratio()


def compare_sentences(sentences, text):
    sentences_scores = []
    for sentence in sentences:
        single_sentence_score = []
        sentence_words = sentence.split()
        sentence_length = len(sentence_words)
        text_words = text.split()
        for i in range(len(text_words) - sentence_length + 2):
            chunk = ' '.join(text_words[i:i+sentence_length])
            res = similar(sentence, chunk)
            single_sentence_score.append(res)
        sentences_scores.append(max(single_sentence_score))
    return sentences_scores
