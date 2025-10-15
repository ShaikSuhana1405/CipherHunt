import matplotlib.pyplot as plt
from collections import Counter
import io
import base64

def plot_frequency(text):
    counter = Counter([ch for ch in text.upper() if ch.isalpha()])
    letters, counts = zip(*sorted(counter.items()))
    fig, ax = plt.subplots()
    ax.bar(letters, counts)
    ax.set_title("Letter Frequency")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
