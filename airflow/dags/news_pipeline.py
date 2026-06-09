from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="news_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["news", "etl"],
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

    generate_metrics = BashOperator(
        task_id="generate_metrics",
        bash_command="""
        cd /opt/airflow/project &&
        python -m analytics.news_metrics
        """
    )

    sentiment_analysis = BashOperator(
        task_id = "sentiment_analysis",
        bash_command="""
        cd /opt/airflow/project &&
        pyhton -m ai.sentiment_analyzer
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
        task_id = "leaderboard",
        bash_command="""
        cd /opt/airflow/project &&
        python -m analytics.leaderboard
        """
    )

    fetch_news >> validate_news >> generate_metrics >> sentiment_analysis >> trend_scoring >> leaderboard