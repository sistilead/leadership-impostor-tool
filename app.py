import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configurazione Pagina
st.set_config(page_title="Scientific Leadership Lab", page_icon="🧬", layout="wide")

st.title("🧬 Identify Your Leadership Impostor")
st.markdown("""
*Based on the Scientific Leadership Framework by Christian Sisti.* Discover which 'Impostor Voice' is influencing your leadership style today.
""")

# Definizioni dallo Spreadsheet
definitions = {
    "The Perfectionist": "I feel like a fraud if the project outcome isn't flawless. Even a 99% success rate feels like a failure because I focus on the 1% that went wrong.",
    "The Natural Genius": "If I have to struggle or work hard to master a new leadership skill, I feel incompetent. I believe it should come to me effortlessly.",
    "The Expert": "I'm terrified of being 'found out' if I don't have the answer to every technical question. I feel I need one more certification before I can lead.",
    "The Soloist": "I believe that asking for help is a sign of weakness. If I didn't achieve the goal entirely on my own, I feel I don't deserve the credit.",
    "The Superhuman": "I feel I must excel in every single role—Director, mentor, parent, athlete—simultaneously. If I fall short in one, I feel like a complete impostor."
}

# Layout a due colonne: Slider a sinistra, Grafico a destra
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Self-Assessment")
    st.caption("Scale: 0 (Silence) to 3 (Loudest)")
    
    scores = []
    categories = list(definitions.keys())
    
    for cat in categories:
        score = st.select_slider(f"**{cat}**", options=[0, 1, 2, 3], key=cat)
        st.caption(f"*{definitions[cat]}*") # Mostra la definizione sotto ogni slider
        scores.append(score)
        st.divider()

with col2:
    st.header("Your Impostor Radar")
    
    # Logica Grafico Radar
    # Per chiudere il cerchio del radar, dobbiamo ripetere il primo valore alla fine
    radar_scores = scores + [scores[0]]
    radar_categories = categories + [categories[0]]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=radar_scores,
        theta=radar_categories,
        fill='toself',
        line=dict(color='#FF4B4B'),
        marker=dict(size=8)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 3])
        ),
        showlegend=False,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Feedback di Leadership
    max_score = max(scores)
    if max_score >= 2:
        st.warning("⚠️ **Coach Insight:** Some