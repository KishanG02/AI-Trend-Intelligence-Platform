from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="ai_trend_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="*/30 * * * *",
    catchup=False,
    tags=["ai", "trends", "youtube", "news"],
) as dag:

    fetch_news = BashOperator(
        task_id="fetch_news",
        bash_command="""
        cd /opt/airflow/project &&
        python -m streaming.news_producer
        """
    )

    validate_news = BashOperator(
        task_id="validate_news",
        bash_command="""
        cd /opt/airflow/project &&
        python -m processing.news_validator
        """
    )

    sentiment_analysis = BashOperator(
        task_id="sentiment_analysis",
        bash_command="""
        cd /opt/airflow/project &&
        python -m ai.sentiment_analyzer
        """
    )

    sentiment_summary = BashOperator(
        task_id="sentiment_summary",
        bash_command="""
        cd /opt/airflow/project &&
        python -m analytics.sentiment_summary
        """
    )

    trend_scoring = BashOperator(
        task_id="trend_scoring",
        bash_command="""
        cd /opt/airflow/project &&
        python -m analytics.trend_scoring
        """
    )

    leaderboard = BashOperator(
        task_id="leaderboard",
        bash_command="""
        cd /opt/airflow/project &&
        python -m analytics.leaderboard
        """
    )

    unified_trends = BashOperator(
        task_id="unified_trends",
        bash_command="""
        cd /opt/airflow/project &&
        python -m analytics.unified_trend_engine
        """
    )

    (
        fetch_news
        >> validate_news
        >> sentiment_analysis
        >> sentiment_summary
        >> trend_scoring
        >> leaderboard
        >> unified_trends
    )