import streamlit as st
import random

st.title("🔐 BB84 Quantum Game")

BASES = ["Z", "X"]
BITS = [0, 1]

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.round = 0

rounds = st.slider("Number of rounds", 1, 20, 5)
evetron = st.checkbox("Evetron is eavesdropping")

if st.button("Play Round"):

    st.session_state.round += 1

    bit = random.choice(BITS)
    base_real = random.choice(BASES)

    choice = st.radio("Choose a basis", BASES)

    if choice == base_real:
        st.success("Correct basis!")
        st.session_state.score += 1
    else:
        st.warning("Wrong basis!")

    st.write(f"Fotoncio's basis was: {base_real}")

    if evetron:
        st.error("Evetron may have interfered!")

st.write("### Score:", st.session_state.score)
