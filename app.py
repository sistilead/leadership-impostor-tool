import streamlit as st
import pandas as pd
import plotly.express as px

# Configurazione Pagina
st.set_page_config(page_title="Scientific Leadership Lab", page_icon="🧬")

st.title("🧬 Leadership Impostor Assessment")
st.markdown("""
*Based on the Scientific Leadership Framework by Christian Sisti.* Identify which 'Impostor Voice' is loudest in your head today. 
**Scale: 0 (Silence) to 3 (Loudest).**
""")

# Sidebar per gli Input
st.sidebar.header("Assess Your Noise Levels")
perf = st.sidebar.select_slider("The Perfectionist", options=[0, 1, 2, 3])
geni = st.sidebar.select_slider("The Natural Genius", options=[0, 1, 2, 3])
expe = st.sidebar.select_slider("The Expert", options=[0, 1, 2, 3])
solo = st.sidebar.select_slider("The Soloist", options=[0, 1, 2, 3])
supe = st.sidebar.select_slider("The Superhuman", options=[0, 1, 2, 3])

# Preparazione Dati
data = {
    'Type': ['Perfectionist', 'Natural Genius', 'Expert', 'Soloist', 'Superhuman'],
    'Score': [perf, geni, expe, solo, supe],
    'Definition': [
        "I feel like a fraud if the project outcome isn't 100% flawless.",
        "I feel I should have all the answers immediately without struggling.",
        "I need 'one more certification' before I feel qualified to lead.",
        "Asking for help feels like a sign of weakness to me.",
        "I feel I must excel in every role (Director, parent, athlete) simultaneously."
    ]
}
df = pd.DataFrame(data)

# Visualizzazione Grafico
fig = px.bar(df, x='Type', y='Score', color='Score', 
             color_continuous_scale='Reds', range_y=[0,3])
st.plotly_chart(fig, use_container_width=True)

# Feedback Dinamico
st.subheader("Your Leadership Insights")
high_scores = df[df['Score'] >= 2]

if not high_scores.empty:
    for index, row in high_scores.iterrows():
        st.error(f"**{row['Type']}**: {row['Definition']}")
else:
    st.success("Your impostor noise levels are low! You are leading with high clarity today.")

st.info("💡 **Coach Tip:** Use this data in your next 1:1 to build vulnerability and trust with your team.")