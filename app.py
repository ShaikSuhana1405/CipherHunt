import streamlit as st
from ciphers import caesar, xor_cipher, substitution
from analysis.frequency_analysis import plot_frequency
from utils.scoring import english_score
import base64

# ---------------------------
# Initialize session state
# ---------------------------
if 'level1_done' not in st.session_state:
    st.session_state.level1_done = False
if 'level2_done' not in st.session_state:
    st.session_state.level2_done = False
if 'level3_done' not in st.session_state:
    st.session_state.level3_done = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="CipherHunt", layout="wide", page_icon="🕵️‍♀️")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🕵️‍♀️ CipherHunt</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #FFA500;'>AI-Powered Cryptanalysis Playground</h4>", unsafe_allow_html=True)

st.sidebar.header("⚙️ Game Controls")
mode = st.sidebar.radio("Choose Mode", ["Free Decryptor", "Puzzle Levels"])
st.sidebar.markdown("---")
st.sidebar.info("Solve ciphers, earn points, and climb the leaderboard! Let'sssss Goooo")

# ---------------------------
# PUZZLE LEVELS MODE
# ---------------------------
if mode == "Puzzle Levels":
    st.subheader("🎮 Puzzle Levels")

    # ---------------- Level 1: Caesar Cipher ----------------
    st.markdown("### 🟢 Level 1: The Spy’s Shift (Caesar Cipher)")
    level1_cipher = "Uifsf jt b tfdsfu dpef"
    st.code(level1_cipher, language="text")
    st.info("Hint: Shift the letters backward by 1–25.")

    user_decrypted1 = st.text_input("Enter your decrypted message:", key="decrypt1")

    # Check correctness
    if user_decrypted1.strip().lower() == "there is a secret code":
        if not st.session_state.level1_done:
            st.success("✅ Level 1 cleared! +10 points")
            st.session_state.score += 10
        st.session_state.level1_done = True
    elif user_decrypted1.strip():
        st.warning("❌ Not correct yet. Try again!")

    # Show step-by-step decryption in expander
    with st.expander("How Caesar decryption works"):
        shift = 1  # Example shift
        explanation = ""
        for c in level1_cipher:
            if c.isalpha():
                decrypted_c = chr(((ord(c.upper()) - 65 - shift) % 26) + 65)
                explanation += f"{c} -> {decrypted_c}\n"
            else:
                explanation += f"{c} -> {c}\n"
        st.text(explanation)

    st.progress(33 if st.session_state.level1_done else 0)

    # ---------------- Level 2: XOR Cipher ----------------
    if st.session_state.level1_done:
        st.markdown("### 🟡 Level 2: Hidden Key (XOR Cipher)")
        xor_text = ''.join(chr(ord(c) ^ 11) for c in "MISSION SUCCESS")
        st.code(f"Cipher: {xor_text.encode('utf-8')}", language="text")
        st.info("Hint: Key is a number between 0–255.")

        user_decrypted2 = st.text_input("Enter your decrypted message:", key="decrypt2")

        if user_decrypted2.strip().upper() == "MISSION SUCCESS":
            if not st.session_state.level2_done:
                st.success("🎉 Level 2 complete! +15 points")
                st.session_state.score += 15
            st.session_state.level2_done = True
        elif user_decrypted2.strip():
            st.warning("❌ Not correct yet. Try again!")

        with st.expander("How XOR decryption works"):
            explanation = ""
            key = 11
            for c in xor_text:
                decrypted_c = chr(ord(c) ^ key)
                explanation += f"{c} ({bin(ord(c))}) ^ {key} ({bin(key)}) = {decrypted_c} ({bin(ord(decrypted_c))})\n"
            st.text(explanation)

        st.progress(66 if st.session_state.level2_done else 33)

    # ---------------- Level 3: Substitution Cipher ----------------
    if st.session_state.level2_done:
        st.markdown("### 🔴 Level 3: Master Substitution Cipher")
        key_map = "QWERTYUIOPASDFGHJKLZXCVBNM"
        level3_plain = "FINAL SECRET MESSAGE"
        level3_cipher = substitution.encrypt(level3_plain, key_map)
        st.code(f"Cipher: {level3_cipher}", language="text")

        user_decrypted3 = st.text_input("Enter your decrypted message:", key="decrypt3")

        if user_decrypted3.strip().upper() == level3_plain:
            if not st.session_state.level3_done:
                st.success("🏆 All 3 levels solved! +25 points")
                st.session_state.score += 25
                st.session_state.leaderboard.append(("Player", st.session_state.score))
            st.session_state.level3_done = True
        elif user_decrypted3.strip():
            st.warning("❌ Not correct yet. Try again!")

        with st.expander("How Substitution decryption works"):
            explanation = ""
            cipher_alphabet = key_map
            plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for c in level3_cipher:
                if c.isalpha():
                    decrypted_c = plain_alphabet[cipher_alphabet.index(c.upper())]
                    explanation += f"{c} -> {decrypted_c}\n"
                else:
                    explanation += f"{c} -> {c}\n"
            st.text(explanation)

        st.progress(100 if st.session_state.level3_done else 66)

    # ---------------- Leaderboard ----------------
    st.subheader("📊 Leaderboard (Session Only)")
    leaderboard_sorted = sorted(st.session_state.leaderboard, key=lambda x: x[1], reverse=True)
    for i, (player, pts) in enumerate(leaderboard_sorted, 1):
        st.markdown(f"**{i}. {player}** — {pts} points")

    st.markdown(f"**Current Score:** {st.session_state.score} points")

# ---------------------------
# FREE DECRYPTOR MODE
# ---------------------------
else:
    st.subheader("🧩 Universal Decryptor Mode")
ciphertext = st.text_area("Enter your encrypted text:", height=150)
col1, col2 = st.columns(2)
with col1:
    method = st.selectbox("Choose Cipher", ["Auto Detect", "Caesar", "XOR", "Substitution"])

if st.button("🔓 Decrypt"):
    if not ciphertext.strip():
        st.warning("Enter some text first.")
    else:
        decrypted_result = ""
        explanation_text = ""

        # ---------------- CAESAR ----------------
        if method == "Caesar":
            results = caesar.brute_force(ciphertext)
            st.subheader("🔑 Caesar Cipher Results")
            for shift, plain in results.items():
                st.markdown(f"**Shift {shift}:** {plain}")

            # Example: show HOW a shift works (let's pick shift 1)
            with st.expander("How Caesar decryption works (example with shift 1)"):
                for c in ciphertext:
                    if c.isalpha():
                        decrypted_c = chr(((ord(c.upper()) - 65 - 1) % 26) + 65)
                        explanation_text += f"{c} -> {decrypted_c}\n"
                    else:
                        explanation_text += f"{c} -> {c}\n"
                st.text(explanation_text)

        # ---------------- SUBSTITUTION ----------------
        elif method == "Substitution":
            key = substitution.example_key()
            decrypted_result = substitution.decrypt(ciphertext, key)
            st.subheader("🔑 Substitution Cipher Result")
            st.text_area("Decrypted Text:", decrypted_result, height=150)

            with st.expander("How Substitution decryption works"):
                explanation_text = ""
                cipher_alphabet = key
                plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                for c in ciphertext:
                    if c.isalpha():
                        decrypted_c = plain_alphabet[cipher_alphabet.index(c.upper())]
                        explanation_text += f"{c} -> {decrypted_c}\n"
                    else:
                        explanation_text += f"{c} -> {c}\n"
                st.text(explanation_text)

        # ---------------- XOR ----------------
        elif method == "XOR":
            results = xor_cipher.brute_force(ciphertext)
            best = sorted(results.items(), key=lambda x: english_score(x[1]), reverse=True)[:5]
            st.subheader("🔑 XOR Cipher Results (Top 5 guesses)")
            for k, plain in best:
                st.markdown(f"**Key {k}:** {plain}")

            # Example: show HOW XOR works for key=11 (you can pick best key)
            with st.expander("How XOR decryption works (example with key=11)"):
                explanation_text = ""
                key = 11
                for c in ciphertext:
                    decrypted_c = chr(ord(c) ^ key)
                    explanation_text += f"{c} ({bin(ord(c))}) ^ {key} ({bin(key)}) = {decrypted_c} ({bin(ord(decrypted_c))})\n"
                st.text(explanation_text)

        # ---------------- AUTO DETECT ----------------
        elif method == "Auto Detect":
            best_guess = {"method": None, "score": 0, "plaintext": ""}
            # Try Caesar
            caesar_res = caesar.brute_force(ciphertext)
            for shift, text in caesar_res.items():
                score = english_score(text)
                if score > best_guess["score"]:
                    best_guess = {"method": f"Caesar (Shift {shift})", "score": score, "plaintext": text}
            # Try XOR
            xor_res = xor_cipher.brute_force(ciphertext)
            for key, text in xor_res.items():
                score = english_score(text)
                if score > best_guess["score"]:
                    best_guess = {"method": f"XOR (Key {key})", "score": score, "plaintext": text}

            st.success(f"🧠 Best Guess: {best_guess['method']}")
            st.text_area("Decrypted Result:", best_guess["plaintext"], height=150)

            with st.expander("How decryption was done for best guess"):
                explanation_text = f"Cipher method used: {best_guess['method']}\n"
                explanation_text += "Step-by-step decryption logic shown here is cipher-specific.\n"
                st.text(explanation_text)

        # ---------------- Frequency Graph ----------------
        img_str = plot_frequency(ciphertext)
        st.image(base64.b64decode(img_str))
