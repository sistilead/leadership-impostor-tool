from datetime import datetime

import plotly.graph_objects as go
import streamlit as st

# Configurazione Pagina
st.set_page_config(page_title="Scientific Leadership Lab", page_icon="🧬", layout="wide")

st.title("🧬 Identify Your Leadership Impostor")
st.markdown("""
### Digital Assessment Tool
*Developed by **Christian Sisti** | Inspired by the framework by **Dr. Valerie Young***
""")

definitions = {
    "The Perfectionist": "I feel like a fraud if the project outcome isn't 100% flawless. I focus on the 1% that went wrong.",
    "The Natural Genius": "If I have to struggle to master a skill, I feel incompetent. It should come effortlessly.",
    "The Expert": "I'm terrified of being found out. I feel I need one more certification before I can lead.",
    "The Soloist": "Asking for help is a sign of weakness. If I didn't do it alone, I don't deserve credit.",
    "The Superhuman": "I must excel in every role (Director, parent, athlete) or I feel like a complete impostor."
}


coaching_actions = {
    "The Perfectionist": "Ship version 1 at 80% quality, then improve with feedback.",
    "The Natural Genius": "Treat effort as proof of growth, not lack of talent.",
    "The Expert": "Lead with what you know now; learn the next 10% in public.",
    "The Soloist": "Ask for one strategic input early in every project.",
    "The Superhuman": "Choose one role to optimize this week and set limits on the rest.",
}

def build_share_card(categories, scores, dominant_profile, insight_text):
    short_profile = dominant_profile.replace("The ", "")

    chart = go.Figure()
    chart.add_shape(
        type="rect",
        x0=0,
        x1=1,
        y0=0,
        y1=1,
        xref="paper",
        yref="paper",
        fillcolor="#0B1021",
        line=dict(width=0),
        layer="below",
    )
    chart.add_shape(
        type="circle",
        x0=0.62,
        x1=1.22,
        y0=0.66,
        y1=1.26,
        xref="paper",
        yref="paper",
        fillcolor="rgba(20, 184, 166, 0.22)",
        line=dict(width=0),
        layer="below",
    )
    chart.add_shape(
        type="circle",
        x0=-0.3,
        x1=0.38,
        y0=-0.26,
        y1=0.42,
        xref="paper",
        yref="paper",
        fillcolor="rgba(59, 130, 246, 0.22)",
        line=dict(width=0),
        layer="below",
    )
    chart.add_trace(
        go.Scatterpolar(
            r=scores + [scores[0]],
            theta=categories + [categories[0]],
            fill="toself",
            fillcolor="rgba(56, 189, 248, 0.28)",
            line=dict(color="#22D3EE", width=6),
            marker=dict(size=8, color="#67E8F9"),
        )
    )

    chart.update_layout(
        width=1080,
        height=1350,
        paper_bgcolor="#0B1021",
        margin=dict(l=80, r=80, t=80, b=80),
        font=dict(family="Avenir Next, Helvetica, Arial, sans-serif"),
        polar=dict(
            domain=dict(x=[0.12, 0.88], y=[0.14, 0.84]),
            bgcolor="rgba(255,255,255,0.04)",
            radialaxis=dict(
                visible=True,
                range=[0, 3],
                tickfont=dict(size=19, color="#D1D5DB"),
                gridcolor="rgba(255,255,255,0.24)",
                linecolor="rgba(255,255,255,0.25)",
            ),
            angularaxis=dict(
                tickfont=dict(size=18, color="#E5E7EB"),
                gridcolor="rgba(255,255,255,0.14)",
                linecolor="rgba(255,255,255,0.25)",
            ),
        ),
        showlegend=False,
        annotations=[
            dict(
                x=0.01,
                y=0.93,
                text=short_profile.upper(),
                xref="paper",
                yref="paper",
                showarrow=False,
                xanchor="left",
                font=dict(size=68, color="#F8FAFC"),
            ),
            dict(
                x=0.01,
                y=0.865,
                text="Leadership Impostor Pattern",
                xref="paper",
                yref="paper",
                showarrow=False,
                xanchor="left",
                font=dict(size=24, color="#E2E8F0"),
            ),
            dict(
                x=0.5,
                y=0.04,
                text="Scientific Leadership Lab | #LeadershipGrowth",
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(size=20, color="#CBD5E1"),
            ),
        ],
    )
    return chart


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

    radar_scores = scores + [scores[0]]
    radar_categories = categories + [categories[0]]

    fig = go.Figure(
        data=go.Scatterpolar(
            r=radar_scores,
            theta=radar_categories,
            fill="toself",
            line=dict(color="#FF4B4B"),
            marker=dict(size=10),
        )
    )

    fig.update_layout(
        margin=dict(l=70, r=70, t=40, b=40),
        polar=dict(
            domain=dict(x=[0.1, 0.9], y=[0.1, 0.9]),
            radialaxis=dict(visible=True, range=[0, 3]),
            angularaxis=dict(tickfont=dict(size=14)),
        ),
        showlegend=False,
        height=560,
    )

    st.plotly_chart(fig, use_container_width=True)

    max_score = max(scores)
    dominant_index = scores.index(max_score)
    dominant_profile = categories[dominant_index]
    action_text = coaching_actions[dominant_profile]

    if max_score >= 2:
        st.warning("⚠️ **Coach Insight:** Noise levels are high. Recognition is the first step to scientific management.")
    else:
        st.success("✅ **Coach Insight:** Your internal noise is low. You are leading with clarity.")

    st.info(f"**Primary Profile:** {dominant_profile}\n\n**7-Day Action:** {action_text}")

    st.subheader("Share Your Results")
    st.caption("Create and download a social-ready image.")

    share_chart = build_share_card(categories, scores, dominant_profile, action_text)
    share_png = None
    try:
        share_png = share_chart.to_image(format="png", width=1080, height=1350, scale=2)
    except Exception:
        st.warning("PNG export unavailable. Install `kaleido` to enable social image download.")

    if share_png:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        st.download_button(
            label="Download Share Card (PNG)",
            data=share_png,
            file_name=f"leadership-impostor-profile-{timestamp}.png",
            mime="image/png",
            use_container_width=True,
        )
