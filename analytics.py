from db import get_connection
import pandas as pd

def performance_summary():
    conn = get_connection()
    df = pd.read_sql("SELECT department, performance_score, hours_worked FROM employees", conn)
    conn.close()
    summary = df.groupby("department").agg({
        "performance_score": "mean",
        "hours_worked": "sum"
    }).reset_index()
    return summary.to_dict(orient="records")