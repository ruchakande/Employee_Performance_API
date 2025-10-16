from flask import Flask, request, jsonify
import mysql.connector
import pandas as pd
from db import get_connection
from analytics import performance_summary

app = Flask(__name__)

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, department, role, performance_score, hours_worked, date_joined) VALUES (%s,%s,%s,%s,%s,%s)",
        (data['name'], data['department'], data['role'], data['performance_score'], data['hours_worked'], data['date_joined'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Employee added successfully"}), 201

@app.route("/employees", methods=["GET"])
def list_employees():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(employees)

@app.route("/analytics/performance", methods=["GET"])
def get_performance_summary():
    summary = performance_summary()
    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)