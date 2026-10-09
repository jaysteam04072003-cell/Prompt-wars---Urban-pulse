"""
UrbanPulse Pune - Backend Server
FastAPI application delivering real-time city exploration, safety navigation,
crowdsourced intelligence, and AI concierge for Pune City Zone.
"""

import os
import uuid
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from pune_data import (
    PUNE_CENTER,
    PUNE_PLACES,
    PUNE_HAZARDS_AND_ALERTS,
    PUNE_SAFE_CORRIDORS,
    PUNE_NEIGHBORHOODS,
    PUNE_SAMPLE_ROUTES,
    PUNE_TELEMETRY,
    PUNE_EMERGENCY_SERVICES
)
from cities_data import (
    CITIES_CATALOG,
    AHMEDABAD_PLACES, AHMEDABAD_HAZARDS, AHMEDABAD_EMERGENCY,
    MUMBAI_PLACES, MUMBAI_HAZARDS, MUMBAI_EMERGENCY,
    DELHI_PLACES, DELHI_HAZARDS, DELHI_EMERGENCY,
    BANGALORE_PLACES, BANGALORE_HAZARDS, BANGALORE_EMERGENCY
)
import database

# Initialize SQLite Database
database.init_db()

app = FastAPI(
    title="UrbanPulse Pune",
    description="Smart City Exploration & Safety Intelligence Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class NewReportRequest(BaseModel):
    title: str
    category: str
    zone: str
    lat: float
    lng: float
    description: str
    reported_by: Optional[str] = "Anonymous Punekar"
    media_type: Optional[str] = "text"
    photo_url: Optional[str] = None
    voice_transcript: Optional[str] = None
    severity: Optional[str] = "MEDIUM"

class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[dict]] = []

# --- API ENDPOINTS ---

@app.get("/api/meta")
def get_meta():
    return {
        "city": "Pune",
        "center": PUNE_CENTER,
        "total_places": len(PUNE_PLACES),
        "total_hazards": len(PUNE_HAZARDS_AND_ALERTS),
        "total_corridors": len(PUNE_SAFE_CORRIDORS),
        "telemetry": PUNE_TELEMETRY
    }

@app.get("/api/cities")
def get_all_cities():
    return CITIES_CATALOG

@app.get("/api/city/{city_id}")
def get_city_profile(city_id: str):
    cid = city_id.lower()
    city_meta = next((c for c in CITIES_CATALOG if c["id"] == cid), None)
    if not city_meta:
        raise HTTPException(status_code=404, detail="City not found")
        
    if cid == "pune":
        return {
            "meta": city_meta,
            "center": PUNE_CENTER,
            "places": PUNE_PLACES,
            "hazards": PUNE_HAZARDS_AND_ALERTS,
            "corridors": PUNE_SAFE_CORRIDORS,
            "emergency": PUNE_EMERGENCY_SERVICES,
            "routes": PUNE_SAMPLE_ROUTES,
            "neighborhoods": PUNE_NEIGHBORHOODS,
            "telemetry": PUNE_TELEMETRY
        }
    elif cid == "ahmedabad":
        return {
            "meta": city_meta,
            "center": city_meta["center"],
            "places": AHMEDABAD_PLACES,
            "hazards": AHMEDABAD_HAZARDS,
            "corridors": [
                {
                    "id": "ahm-corridor-1",
                    "name": "Sabarmati Riverfront Promenade",
                    "zone": "Sabarmati Riverfront",
                    "start": {"lat": 23.0380, "lng": 72.5780},
                    "end": {"lat": 23.0180, "lng": 72.5700},
                    "safety_rating": 98,
                    "features": ["100% Pedestrian corridor", "Continuous LED security lighting", "Police beat patrol bikes", "CCTV coverage"]
                }
            ],
            "emergency": AHMEDABAD_EMERGENCY,
            "routes": [],
            "neighborhoods": {},
            "telemetry": {
                "city": "Ahmedabad, Gujarat",
                "weather": {"temp": "31°C", "condition": "Sunny & Clear", "humidity": "42%", "wind": "10 km/h NW"},
                "air_quality": {"aqi": 92, "status": "Moderate", "recommendation": "Pleasant evening for riverfront walk"},
                "traffic_summary": {"congestion_index": "52/100"}
            }
        }
    elif cid == "mumbai":
        return {
            "meta": city_meta,
            "center": city_meta["center"],
            "places": MUMBAI_PLACES,
            "hazards": MUMBAI_HAZARDS,
            "corridors": [
                {
                    "id": "mum-corridor-1",
                    "name": "Marine Drive Promenade Corridor",
                    "zone": "Churchgate to Nariman Point",
                    "start": {"lat": 18.9480, "lng": 72.8240},
                    "end": {"lat": 18.9260, "lng": 72.8210},
                    "safety_rating": 98,
                    "features": ["24/7 Mumbai Police patrolling", "High footfall until 3 AM", "Continuous sodium & LED illumination"]
                }
            ],
            "emergency": MUMBAI_EMERGENCY,
            "routes": [],
            "neighborhoods": {},
            "telemetry": {
                "city": "Mumbai, Maharashtra",
                "weather": {"temp": "30°C", "condition": "Breezy & Humid", "humidity": "68%", "wind": "16 km/h SW"},
                "air_quality": {"aqi": 88, "status": "Moderate", "recommendation": "Great sea breeze along Marine Drive"},
                "traffic_summary": {"congestion_index": "68/100"}
            }
        }
    elif cid == "delhi":
        return {
            "meta": city_meta,
            "center": city_meta["center"],
            "places": DELHI_PLACES,
            "hazards": DELHI_HAZARDS,
            "corridors": [
                {
                    "id": "del-corridor-1",
                    "name": "Kartavya Path / Central Vista Promenade",
                    "zone": "India Gate to Rashtrapati Bhavan",
                    "start": {"lat": 28.6129, "lng": 77.2295},
                    "end": {"lat": 28.6143, "lng": 77.1990},
                    "safety_rating": 97,
                    "features": ["Heavy PCR van security", "High-luminance bollard lights", "Direct emergency call boxes"]
                }
            ],
            "emergency": DELHI_EMERGENCY,
            "routes": [],
            "neighborhoods": {},
            "telemetry": {
                "city": "New Delhi",
                "weather": {"temp": "27°C", "condition": "Hazy Sunshine", "humidity": "48%", "wind": "8 km/h E"},
                "air_quality": {"aqi": 142, "status": "Sensitive Caution", "recommendation": "Light mask recommended for sensitive groups"},
                "traffic_summary": {"congestion_index": "62/100"}
            }
        }
    elif cid == "bangalore":
        return {
            "meta": city_meta,
            "center": city_meta["center"],
            "places": BANGALORE_PLACES,
            "hazards": BANGALORE_HAZARDS,
            "corridors": [
                {
                    "id": "blr-corridor-1",
                    "name": "Indiranagar 100ft Road Cafe Corridor",
                    "zone": "Indiranagar",
                    "start": {"lat": 12.9800, "lng": 77.6410},
                    "end": {"lat": 12.9650, "lng": 77.6420},
                    "safety_rating": 96,
                    "features": ["Active cafe and dining footfall till 1 AM", "Continuous streetlighting", "Bangalore beat marshals"]
                }
            ],
            "emergency": BANGALORE_EMERGENCY,
            "routes": [],
            "neighborhoods": {},
            "telemetry": {
                "city": "Bangalore, Karnataka",
                "weather": {"temp": "24°C", "condition": "Pleasant Breeze", "humidity": "62%", "wind": "14 km/h W"},
                "air_quality": {"aqi": 58, "status": "Good (Healthy)", "recommendation": "Ideal weather for Cubbon Park walk"},
                "traffic_summary": {"congestion_index": "72/100"}
            }
        }

@app.get("/api/places")
def get_places(
    category: Optional[str] = "all",
    search: Optional[str] = None,
    night_only: Optional[bool] = False,
    min_safety: Optional[int] = 0
):
    results = PUNE_PLACES
    if category and category != "all":
        results = [p for p in results if p["category"] == category]
    if search:
        s = search.lower()
        results = [
            p for p in results 
            if s in p["name"].lower() or s in p["zone"].lower() or s in p["tagline"].lower() or s in p["description"].lower()
        ]
    if night_only:
        results = [p for p in results if p.get("night_safe", False)]
    if min_safety > 0:
        results = [p for p in results if p.get("safety_score", 0) >= min_safety]
        
    return results

@app.get("/api/places/{place_id}")
def get_place_detail(place_id: str):
    for p in PUNE_PLACES:
        if p["id"] == place_id:
            return p
    raise HTTPException(status_code=404, detail="Place not found in Pune database")

@app.get("/api/emergency")
def get_emergency_services():
    return PUNE_EMERGENCY_SERVICES

@app.get("/api/hazards")
def get_hazards():
    return PUNE_HAZARDS_AND_ALERTS

@app.get("/api/corridors")
def get_corridors():
    return PUNE_SAFE_CORRIDORS

@app.get("/api/routes")
def get_routes(route_id: Optional[str] = None):
    if route_id:
        for r in PUNE_SAMPLE_ROUTES:
            if r["id"] == route_id:
                return r
        raise HTTPException(status_code=404, detail="Route not found")
    return PUNE_SAMPLE_ROUTES

@app.get("/api/neighborhoods")
def get_neighborhoods():
    return PUNE_NEIGHBORHOODS

@app.get("/api/compare")
def compare_neighborhoods(
    zone_a: str = Query("koregaon_park", description="First zone id"),
    zone_b: str = Query("swargate", description="Second zone id")
):
    if zone_a not in PUNE_NEIGHBORHOODS or zone_b not in PUNE_NEIGHBORHOODS:
        raise HTTPException(status_code=400, detail="Invalid neighborhood IDs")
    
    a = PUNE_NEIGHBORHOODS[zone_a]
    b = PUNE_NEIGHBORHOODS[zone_b]
    
    # Calculate verdict
    safety_diff = a["scores"]["safety"] - b["scores"]["safety"]
    cost_diff = a["scores"]["affordability"] - b["scores"]["affordability"]
    
    return {
        "zone_a": a,
        "zone_b": b,
        "metrics_keys": ["safety", "cleanliness", "affordability", "accessibility", "greenery_vibe", "night_safety"],
        "insights": {
            "safer": a["name"] if safety_diff > 0 else b["name"] if safety_diff < 0 else "Equal",
            "more_affordable": a["name"] if cost_diff > 0 else b["name"] if cost_diff < 0 else "Equal",
            "summary": f"{a['name']} excels in {a['category_tag']} while {b['name']} is recognized for {b['category_tag']}."
        }
    }

@app.get("/api/reports")
def get_reports(category: Optional[str] = "all"):
    return database.list_reports(category)

@app.post("/api/reports")
def create_report(report: NewReportRequest):
    # Auto AI analysis of severity if not specified
    severity = report.severity
    desc_lower = report.description.lower() + " " + report.title.lower()
    if any(k in desc_lower for k in ["accident", "oil spill", "danger", "brake fail", "fire", "death", "injury"]):
        severity = "CRITICAL"
    elif any(k in desc_lower for k in ["jam", "waterlog", "pothole", "dark", "no light"]):
        severity = "HIGH"
    elif "gem" in desc_lower or "food" in desc_lower:
        severity = "LOW"

    new_id = f"report-{uuid.uuid4().hex[:6]}"
    report_dict = {
        "id": new_id,
        "title": report.title,
        "category": report.category,
        "zone": report.zone,
        "lat": report.lat,
        "lng": report.lng,
        "description": report.description,
        "reported_by": report.reported_by or "Punekar Citizen",
        "timestamp": "Just now",
        "upvotes": 1,
        "verified": False,
        "severity": severity,
        "media_type": report.media_type,
        "photo_url": report.photo_url,
        "voice_transcript": report.voice_transcript
    }
    database.add_report(report_dict)
    return {"status": "success", "report": report_dict}

@app.post("/api/reports/{report_id}/upvote")
def upvote(report_id: str):
    votes = database.upvote_report(report_id)
    return {"status": "success", "report_id": report_id, "upvotes": votes}

@app.get("/api/telemetry")
def get_telemetry():
    return PUNE_TELEMETRY

# --- AI CITY CONCIERGE (NLP / Smart Logic Engine) ---
@app.post("/api/ai-concierge")
def ai_concierge(payload: ChatRequest):
    query = payload.message.strip().lower()
    
    # Analyze query intent
    # 1. Navale bridge / accident / danger query
    if any(k in query for k in ["navale", "accident", "danger", "bypass", "blackspot", "safe route"]):
        reply = (
            "⚠️ **Navale Bridge Caution Alert:** The 6-km downward slope on the Mumbai-Bangalore bypass "
            "near Navale Bridge is Pune's highest accident blackspot due to heavy trucks suffering brake failure.\n\n"
            "🛡️ **Recommended Safer Action:** If traveling south or towards Katraj during peak or late-night hours (10 PM - 5 AM), "
            "avoid the outer high-speed truck lanes or use the internal Sinhagad Road through Dhayari. Stay alert!"
        )
        suggested_pins = ["hazard-1"]
    
    # 2. Food / Misal / Vaishali / Street Food
    elif any(k in query for k in ["food", "misal", "vaishali", "shrewsbury", "burger", "mastani", "eat", "hungry", "chai", "coffee"]):
        reply = (
            "🍴 **Pune Gastronomic Recommendations:**\n"
            "1. **FC Road Strip:** Try the legendary SPDP (Sev Potato Dahi Puri) and filter coffee at *Vaishali*, or bun maska at *Goodluck Cafe*.\n"
            "2. **Heritage Misal:** Head to *Bedekar Misal* in Narayan Peth for authentic Puneri sweet-and-spicy rassa.\n"
            "3. **Camp Classics:** Don't miss *Kayani Bakery* for Shrewsbury biscuits and the mammoth *Camp King Burger*.\n"
            "4. **Royal Dessert:** Savor *Sujata Mastani* in Sadashiv Peth!"
        )
        suggested_pins = ["pune-food-1", "pune-food-2", "pune-food-3", "pune-food-5"]

    # 3. History / Heritage / Shaniwar Wada / Fort
    elif any(k in query for k in ["heritage", "history", "wada", "shaniwar", "fort", "sinhagad", "aga khan", "dagdusheth", "culture"]):
        reply = (
            "🏛️ **Pune's Living Heritage & Maratha Legacy:**\n"
            "• **Shaniwar Wada (1732):** The royal seat of the Peshwas featuring the formidable Dilli Darwaza.\n"
            "• **Aga Khan Palace (1892):** Monument where Mahatma Gandhi was detained during the 1942 Quit India movement; houses Kasturba Gandhi's memorial.\n"
            "• **Pataleshwar Cave:** 8th-century monolithic rock-cut cave temple hidden beneath modern JM Road!\n"
            "• **Sinhagad Fort:** 1670 battle site of Tanaji Malusare — perfect for an early morning climb with piping hot Pithla Bhakri."
        )
        suggested_pins = ["pune-heritage-1", "pune-heritage-2", "pune-heritage-3", "pune-heritage-4", "pune-heritage-5"]

    # 4. Night Safety / Women Safety / Late Night
    elif any(k in query for k in ["night", "late", "dark", "women", "safe", "midnight", "walk"]):
        reply = (
            "🛡️ **Pune Night Safety & Lit Corridors:**\n"
            "• **High-Safety Zones:** *FC Road*, *JM Road*, and *Koregaon Park North Main Road* have 24/7 CCTV, active pedestrian footfall, and frequent police patrolling till past midnight.\n"
            "• **Caution Zones:** Avoid the unlit Mutha riverbed pedestrian paths after 10:30 PM and deserted railway siding stretches near Ghorpadi.\n"
            "• **Live Tip:** Use our *SafePath Route Planner* to lock your journey through smart lit corridors!"
        )
        suggested_pins = ["safe-corridor-1", "safe-corridor-2", "safe-corridor-3", "hazard-4"]

    # 5. Budget / Student areas / Accommodation
    elif any(k in query for k in ["budget", "student", "cheap", "stay", "hostel", "pg"]):
        reply = (
            "🎒 **Budget & Student Havens in Pune:**\n"
            "• **Deccan Gymkhana & FC Road:** The ultimate student hub with shared PGs, ₹100 meal thalis, and quick Metro access.\n"
            "• **Viman Nagar:** Clean, walkable student and young professional area near Symbiosis with 24-hour food joints.\n"
            "• **Kothrud:** Great balance of affordable family stays and traditional Puneri safety."
        )
        suggested_pins = ["pune-stay-1", "pune-stay-2", "fc_road_deccan"]

    # Default general assistant
    else:
        reply = (
            f"Namaskar! I'm your **UrbanPulse AI Guide for Pune**. You can ask me about:\n"
            "• 🍛 *'Where to get the best street food safely at night?'*\n"
            "• 🏛️ *'Tell me the history of Shaniwar Wada and Aga Khan Palace'*\n"
            "• ⚠️ *'What are the dangerous traffic blackspots like Navale Bridge?'*\n"
            "• 🚶 *'Show me the safest route from Shaniwar Wada to FC Road'*\n"
            "• ⚖️ *'Compare Koregaon Park vs Swargate on safety and cost'*"
        )
        suggested_pins = ["pune-heritage-1", "pune-food-1"]

    return {
        "reply": reply,
        "suggested_pins": suggested_pins,
        "city": "Pune"
    }

# Mount static folder for frontend files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def serve_root():
    return FileResponse(os.path.join(static_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
