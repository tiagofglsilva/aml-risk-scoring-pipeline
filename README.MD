# End-to-End AML Risk Scoring & Compliance Pipeline

An automated data pipeline built in Python and SQLite that simulates Anti-Money Laundering (AML) risk evaluation, automated client risk scoring, and reporting visualization.

## 📌 Features
- **Database Setup (`01_setup_db.py`)**: Populates an SQLite database (`aml.db`) with client transaction histories and risk indicators.
- **Risk Analysis Engine (`02_risk_analysis.py`)**: Categorizes high-risk clients based on transaction anomalies, geography, and demographic profiles.
- **Data Visualization (`03_visualizations.py`)**: Generates automated graphical reports for compliance review.
- **Pipeline Automation (`run_pipeline.py`)**: Executes the full ETL and reporting workflow end-to-end.

## 🚀 Execution
To run the complete pipeline from scratch:

```bash
python run_pipeline.py