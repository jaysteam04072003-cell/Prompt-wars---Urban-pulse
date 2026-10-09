# UrbanPulse Pune (PromptWars Hackathon MVP)
### *Exploring, Experiencing & Navigating the Chaos We Call Home*

---

## 🌟 Overview
**UrbanPulse Pune** is a smart, interactive city exploration and safety intelligence platform designed for **Pune City Zone**. It solves the problem of fragmented urban information by merging **cultural exploration, legendary street food, accident & hazard intelligence, and smart safe routing** into a single real-time dashboard.

---

## 🗺️ Problem Statement Mapping

| Hackathon Requirement | UrbanPulse Pune Implementation |
| :--- | :--- |
| **Exploration & Hospitality** | Curated iconic spots: FC Road (Vaishali, Goodluck), Kayani Bakery & Camp Burger, Sujata Mastani, Bedekar Misal, Viman Nagar backpacker belt, Deccan student hostels. |
| **History & Culture** | Deep Peshwa heritage: Shaniwar Wada, Lal Mahal, Dagdusheth Temple, Aga Khan Palace, 8th-century Pataleshwar Cave, Sinhagad Fort with **in-browser Voice Audio Guide narration**. |
| **Safety & Security** | Ground-truth Pune accident blackspots (Navale Bridge slope brake-fail corridor, Swargate congestion, Mutha riverbed unlit stretches) + 3 verified safe lit corridors. |
| **Emergency Safe Haven** | **1-Click Police & Hospital Grid**: 6 24/7 Pune Police Stations (Deccan, Shivajinagar, Swargate, Bund Garden, Faraskhana, Katraj) + 6 Trauma Hospitals (Sassoon, Sancheti, Poona Hospital, Ruby Hall, Sahyadri, Navale) with instant call shortcuts (`112`, `108`, `1091`). |
| **Best vs. Worst Comparison** | Interactive radar chart comparing Pune localities (Koregaon Park vs Swargate vs FC Road vs Kothrud) across Safety, Cleanliness, Cost, Walkability, and Vibe. |
| **Smart City Insights** | Pune real-time telemetry (Weather, AQI, Congestion Index) + crowdsourced citizen reports with community upvoting. |
| **AI / NLP Intelligence** | Context-aware AI City Concierge with Pune-specific recommendations and voice note dictation. |

---

## 🚀 Live Access
The platform is currently **LIVE and running** locally at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 💻 Tech Stack
* **Backend:** FastAPI (Python 3.14) + SQLite (`pune_urbanpulse.db`)
* **Frontend:** Responsive SPA with Tailwind CSS + HTML5
* **Maps & GIS:** Leaflet.js with CartoDB Voyager & Dark Matter tiles, GeoJSON coordinates, dynamic polylines, and safety buffer circles
* **Audio & Speech:** HTML5 Web Speech Synthesis (Audio Guide) & Speech Recognition (Voice Notes)
* **Visual Analytics:** Chart.js radar charts for locality comparison

---

## 📂 Project Structure
```
├── server.py              # FastAPI server & REST endpoints
├── pune_data.py           # Authentic Pune datasets (POI, hazards, corridors, routes)
├── database.py            # SQLite database manager for crowdsourced reports & upvotes
├── pune_urbanpulse.db     # SQLite storage file
├── run.bat                # 1-click startup script
└── static/
    ├── index.html         # Responsive UI with 5 functional tabs
    ├── app.js             # Leaflet maps, routing, comparator, voice notes & AI chat
    └── style.css          # Dark-mode styling, hazard pulse animations & glowing paths
```
