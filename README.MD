# End-to-End AML Risk Scoring & Compliance Pipeline

An automated data pipeline built in Python and SQLite that evaluates client profile data, identifies financial risk indicators (such as wealth-to-income mismatches), and generates automated compliance reports.

## 📌 Features
- **Database Setup (`01_setup_db.py`)**: Populates an SQLite database (`aml.db`) with client demographic profiles and risk indicators.
- **Risk Analysis Engine (`02_risk_analysis.py`)**: Categorizes high-risk clients based on multi-factor heuristics, geography, and profile anomalies.
- **Data Visualization (`03_visualizations.py`)**: Generates automated graphical reports for compliance review.
- **Pipeline Automation (`run_pipeline.py`)**: Executes the full ETL and reporting workflow end-to-end.

## 🚀 Execution
To run the complete pipeline from scratch:

```bash
python run_pipeline.py
'''

##📬 Connect

    Author: Tiago Frederico

    LinkedIn: tiagofrederico2001

    GitHub: @tiagofglsilva
