#  CipherHunt

CipherHunt is an AI-powered interactive cryptography playground where users solve cipher puzzles, learn decryption techniques, and experiment with different classic ciphers. Built with Python and Streamlit, it combines education, gamification, and practical cryptanalysis.

---

##  Project Purpose
CipherHunt allows users to:
- Solve cryptographic puzzles using Caesar, XOR, and Substitution ciphers.
- Explore step-by-step decryption explanations to understand how each cipher works.
- Practice cryptography in a fun, interactive, and educational way.
- Use a Free Decryptor mode for experimenting with custom ciphertexts.

---

##  Features

### Puzzle Levels Mode
- Level 1: Caesar Cipher
  - Decrypt messages by guessing the correct shift.
  - Step-by-step explanation of letter shifts.
- Level 2: XOR Cipher
  - Decrypt messages using numeric keys (0–255).
  - Step-by-step explanation of bitwise XOR.
- Level 3: Substitution Cipher
  - Decrypt messages using a letter substitution key.
  - Step-by-step explanation of letter mappings.
- Progress Tracking & Scoring
  - Earn points for each solved level.
  - Session-only leaderboard included.

### Free Decryptor Mode
- Decrypt any text using:
  - Caesar
  - XOR
  - Substitution
  - Auto Detect mode
- Shows step-by-step decryption logic.
- Generates frequency analysis graphs for better understanding.

---

##  Tech Stack
- Language: Python 3.x
- Framework: Streamlit
- Libraries: NumPy, Matplotlib (for frequency analysis), Base64
- Core Concepts:Caesar Cipher, XOR Cipher, Substitution Cipher, Frequency Analysis

---

##  How to Run Locally
1. Clone the repository:
git clone https://github.com/ShaikSuhana1405/CipherHunt.git
cd CipherHunt
