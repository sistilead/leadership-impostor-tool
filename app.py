import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configurazione Pagina
st.set_page_config(page_title="Scientific Leadership Lab", page_icon="🧬", layout="wide")

st.title("🧬 Identify Your Leadership Impostor")
st.markdown("""
### Digital Assessment Tool
*Developed by **Christian Sisti** | Inspired by the framework by **Dr. Valerie Young***
""")

# Definizioni esatte dal tuo spreadsheet
definitions = {
    "The Perfectionist": "I feel like a fraud if the project outcome isn't 100% flawless. I focus on the 1% that went wrong.",
    "The Natural Genius": "If I have to struggle to master a skill, I feel incompetent. It should come effortlessly.",
    "The Expert": "I'm terrified of being found out. I feel I need one more certification before I can lead.",
    "The Soloist": "Asking for help is a sign of weakness. If I didn't do it alone, I don't deserve credit.",
    "The Superhuman": "I must excel in every role (Director, parent, athlete) or I feel like a complete impostor."
}

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Self-Assessment")
    st.caption("Scale: 0 (Silence) to 3 (Loudest)")
    
    scores = []
    categories = list(definitions.keys())
    
    for cat in categories:
        score = st.select_slider(f"**{cat}**", options=[0, 1, 2, 3], key=cat)
        st.caption(f"_{definitions[cat]}_")
        scores.append(score)
        st.write("---")

with col2:
    st.header("Your Impostor Radar")
    
    # Preparazione dati radar
    radar_scores = scores + [scores[0]]
    radar_categories = categories + [categories[0]]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=radar_scores,
        theta=radar_categories,
        fill='toself',
        line=dict(color='#FF4B4B'),
        marker=dict(size=10)
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 3])),
        showlegend=False,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Feedback di Leadership
    max_score = max(scores)
    if max_score >= 2:
        st.warning("⚠️ **Coach Insight:** Noise levels are high. Recognition is the first step to scientific management.")
    else:
        st.success("✅ **Coach Insight:** Your internal noise is low. You are leading with clarity.")