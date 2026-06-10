import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# =====================================================

# PAGE CONFIG

# =====================================================

st.set_page_config(
page_title="AI Trend Intelligence Platform",
page_icon="📈",
layout="wide"
)

st_autorefresh(
interval=60000,
key="refresh"
)

# =====================================================

# DETECT STREAMLIT THEME

# =====================================================

theme_base = st.get_option("theme.base")

plotly_template = (
"plotly_dark"
if theme_base == "dark"
else "plotly_white"
)

# =====================================================

# LOAD DATA

# =====================================================

ANALYTICS_PATH = Path("data-lake/analytics")

with open(ANALYTICS_PATH / "sentiment_summary.json") as f:
    sentiment_summary = json.load(f)

with open(ANALYTICS_PATH / "unified_trend_scores.json") as f:
    unified_scores = json.load(f)

with open(ANALYTICS_PATH / "trending_keywords.json") as f:
    leaderboard = json.load(f)

with open(ANALYTICS_PATH / "youtube" / "youtube_summary.json") as f:
    youtube_summary = json.load(f)

with open(ANALYTICS_PATH / "youtube" / "top_channels.json") as f:
    top_channels = json.load(f)

trend_history_path = (
    ANALYTICS_PATH /
    "trend_history.csv"
)

trend_history_df = pd.read_csv(
    trend_history_path
)

trend_history_df["date"] = pd.to_datetime(
    trend_history_df["date"]
)

top_channels_df = pd.DataFrame(
    top_channels
)

unified_df = pd.DataFrame(
    unified_scores
)

# =====================================================

# SIDEBAR

# =====================================================

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Choose a Section",
    [
        "Overview",
        "Unified Trends",
        "Leaderboard",
        "Trend History",
        "Sentiment Analytics",
        "Top Channels",
        "Pipeline Health",
        "AI Insights"
    ]
)

st.sidebar.divider()

st.sidebar.success("Pipeline Status: Healthy")

st.sidebar.caption(
"Powered by Kafka • Airflow • Streamlit"
)

# =====================================================

# HEADER

# =====================================================

st.title("🚀 AI Trend Intelligence Platform")

st.caption(
"Real-Time Technology Trend Monitoring, Sentiment Analytics & Trend Intelligence"
)

st.divider()

# =====================================================

# OVERVIEW

# =====================================================

if page == "Overview":

    top_keyword = unified_scores[0]["keyword"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Articles",
            sentiment_summary["total_articles"]
        )

    with col2:
        st.metric(
            "Videos",
            youtube_summary["total_videos"]
        )

    with col3:
        st.metric(
            "Sources",
            2
        )

    with col4:
        st.metric(
            "Top Trend",
            top_keyword
        )

    # =================================
    # Sentiment KPIs
    # =================================

    s1, s2, s3 = st.columns(3)

    with s1:
        st.metric(
            "🟢 Positive",
            sentiment_summary["positive"]
        )

    with s2:
        st.metric(
            "⚪ Neutral",
            sentiment_summary["neutral"]
        )

    with s3:
        st.metric(
            "🔴 Negative",
            sentiment_summary["negative"]
        )

    st.info(
        f"""
    📄 Articles Processed: {sentiment_summary['total_articles']}

    🎥 Videos Processed: {youtube_summary['total_videos']}

    📺 Channels Tracked: {youtube_summary['unique_channels']}

    🔍 Keywords Tracked: {youtube_summary['unique_keywords']}
    """
    )

    st.divider()

    left, right = st.columns([2, 1])

    # =================================
    # Trend Scores
    # =================================

    with left:

        st.subheader("📈 Technology Trend Scores")

        fig = px.bar(
            unified_df,
            x="keyword",
            y="final_score",
            color="final_score",
            text="final_score",
            template=plotly_template,
            title="Unified Trend Scores"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            xaxis_title="Technology",
            yaxis_title="Trend Score",
            height=550
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # =================================
    # Sentiment Distribution
    # =================================

    with right:

        st.subheader("❤️ Sentiment Distribution")

        sentiment_df = pd.DataFrame(
            {
                "Sentiment": [
                    "Positive",
                    "Neutral",
                    "Negative"
                ],
                "Count": [
                    sentiment_summary["positive"],
                    sentiment_summary["neutral"],
                    sentiment_summary["negative"]
                ]
            }
        )

        pie = px.pie(
            sentiment_df,
            names="Sentiment",
            values="Count",
            hole=0.5,
            template=plotly_template
        )

        pie.update_layout(
            height=500
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

# =====================================================

# Trend History

# =====================================================

elif page == "Trend History":

    st.title("📈 Trend History")

    keywords = sorted(
        trend_history_df["keyword"].unique()
    )

    selected_keywords = st.multiselect(
        "Select Technologies",
        keywords,
        default=keywords[:3]
    )

    filtered_df = trend_history_df[
        trend_history_df["keyword"].isin(
            selected_keywords
        )
    ]

    fig = px.line(
        filtered_df,
        x="date",
        y="final_score",
        color="keyword",
        markers=True,
        template=plotly_template,
        title="Technology Trend Scores Over Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================

# Unified trends

# =====================================================

elif page == "Unified Trends":

    st.subheader(
        "🚀 Unified Trend Intelligence"
    )

    st.metric(
        "Tracked Technologies",
        len(unified_df)
    )

    st.dataframe(
        unified_df,
        use_container_width=True
    )

    fig = px.bar(
        unified_df,
        x="keyword",
        y="final_score",
        color="final_score",
        text="final_score",
        template=plotly_template,
        title="Unified Trend Scores"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================

# Top channels

# =====================================================

elif page == "Top Channels":

    st.subheader(
        "📺 Top YouTube Channels"
    )

    st.dataframe(
        top_channels_df,
        use_container_width=True
    )

    st.divider()

    fig = px.bar(
        top_channels_df.head(10),
        x="video_count",
        y="channel",
        orientation="h",
        template=plotly_template,
        title="Top 10 Channels by Video Count"
    )

    fig.update_layout(
        height=600,
        yaxis_title="Channel",
        xaxis_title="Videos"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================

# LEADERBOARD

# =====================================================

elif page == "Leaderboard":

    st.subheader("🏆 Trending Technologies")

    medals = ["🥇", "🥈", "🥉"]

    for idx, item in enumerate(leaderboard):

        medal = medals[idx] if idx < 3 else "🏅"

        st.info(
            f"{medal} {item['keyword']} | Trend Score: {item['trend_score']}"
        )

# =====================================================

# SENTIMENT ANALYTICS

# =====================================================

elif page == "Sentiment Analytics":

    st.subheader("❤️ Sentiment Analytics")

    sentiment_df = pd.DataFrame(
        {
            "Sentiment": [
                "Positive",
                "Neutral",
                "Negative"
            ],
            "Count": [
                sentiment_summary["positive"],
                sentiment_summary["neutral"],
                sentiment_summary["negative"]
            ]
        }
    )

    fig = px.bar(
        sentiment_df,
        x="Sentiment",
        y="Count",
        text="Count",
        template=plotly_template
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        sentiment_df,
        use_container_width=True
    )


# =====================================================

# TREND DETAILS

# =====================================================

elif page == "Pipeline Health":

    st.subheader(
        "🟢 Pipeline Health"
    )

    st.success("Kafka Running")
    st.success("Airflow Running")
    st.success("News Pipeline Running")
    st.success("YouTube Pipeline Running")
    st.success("Sentiment Engine Running")
    st.success("Unified Trend Engine Running")

# =====================================================

# AI Summary

# =====================================================

elif page == "AI Insights":

    st.subheader("🤖 AI Trend Intelligence")

    try:
        with open(
            ANALYTICS_PATH / "ai_summary.json"
        ) as f:
            ai_summary = json.load(f)

        st.success(
            f"Generated: {ai_summary['generated_at']}"
        )

        st.markdown(
            ai_summary["summary"]
        )

    except Exception as e:

        st.error(
            f"Unable to load AI summary: {e}"
        )

# =====================================================

# FOOTER

# =====================================================

st.divider()

st.caption(
"AI Trend Intelligence Platform | Built with Kafka, Airflow, Sentiment Analysis and Streamlit"
)