"""
Database manager for UrbanPulse Pune
SQLite persistence for Citizen Reports, Safety Hazard submissions, and Community Upvotes.
"""

import sqlite3
import json
import os
from pune_data import PUNE_CITIZEN_REPORTS_INITIAL

DB_PATH = "/tmp/pune_urbanpulse.db" if os.environ.get("VERCEL") else os.path.join(os.path.dirname(__file__), "pune_urbanpulse.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Table for citizen reports & alerts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS citizen_reports (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            zone TEXT NOT NULL,
            lat REAL NOT NULL,
            lng REAL NOT NULL,
            description TEXT NOT NULL,
            reported_by TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            upvotes INTEGER DEFAULT 1,
            verified INTEGER DEFAULT 0,
            severity TEXT DEFAULT 'MEDIUM',
            media_type TEXT DEFAULT 'text',
            photo_url TEXT,
            voice_transcript TEXT
        )
    """)
    
    # Seed initial Pune reports if empty
    cursor.execute("SELECT COUNT(*) FROM citizen_reports")
    count = cursor.fetchone()[0]
    if count == 0:
        for r in PUNE_CITIZEN_REPORTS_INITIAL:
            cursor.execute("""
                INSERT INTO citizen_reports 
                (id, title, category, zone, lat, lng, description, reported_by, timestamp, upvotes, verified, severity, media_type, photo_url, voice_transcript)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                r["id"], r["title"], r["category"], r["zone"], r["lat"], r["lng"],
                r["description"], r["reported_by"], r["timestamp"], r["upvotes"],
                1 if r["verified"] else 0, r["severity"], r["media_type"],
                r["photo_url"], r["voice_transcript"]
            ))
        conn.commit()
    conn.close()

def list_reports(category=None):
    conn = get_connection()
    cursor = conn.cursor()
    if category and category != 'all':
        cursor.execute("SELECT * FROM citizen_reports WHERE category = ? ORDER BY upvotes DESC", (category,))
    else:
        cursor.execute("SELECT * FROM citizen_reports ORDER BY upvotes DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_report(report_dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO citizen_reports 
        (id, title, category, zone, lat, lng, description, reported_by, timestamp, upvotes, verified, severity, media_type, photo_url, voice_transcript)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        report_dict["id"], report_dict["title"], report_dict["category"], report_dict["zone"],
        report_dict["lat"], report_dict["lng"], report_dict["description"], report_dict["reported_by"],
        report_dict["timestamp"], report_dict.get("upvotes", 1),
        1 if report_dict.get("verified", False) else 0,
        report_dict.get("severity", "MEDIUM"),
        report_dict.get("media_type", "text"),
        report_dict.get("photo_url"),
        report_dict.get("voice_transcript")
    ))
    conn.commit()
    conn.close()
    return report_dict

def upvote_report(report_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE citizen_reports SET upvotes = upvotes + 1 WHERE id = ?", (report_id,))
    cursor.execute("SELECT upvotes FROM citizen_reports WHERE id = ?", (report_id,))
    row = cursor.fetchone()
    conn.commit()
    conn.close()
    return row[0] if row else 0
