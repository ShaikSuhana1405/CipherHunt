import re
from collections import Counter

def english_score(text):
    """Return a rough score of how English-like a string is."""
    text = text.upper()
    freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    count = Counter([c for c in text if c.isalpha()])
    score = 0
    for letter, freq in count.items():
        if letter in freq_order:
            score += (26 - freq_order.index(letter)) * freq
    words = re.findall(r'\b[A-Z]{3,}\b', text)
    score += len(words) * 5
    return score
