"""
UrbanPulse - 5 City Database
Curated datasets for:
1. Pune: "Kasa Kay Pune"
2. Ahmedabad: "Kem Cho Amdavad"
3. Mumbai: "Ram Ram Maharashtra"
4. Delhi: "Namaste Dilli"
5. Bangalore: "Gothilla Bengaluru"
"""

CITIES_CATALOG = [
    {
        "id": "pune",
        "name": "Pune",
        "greeting": "Kasa Kay Pune",
        "tagline": "The cultural cradle of Maharashtra, Oxford of the East & IT innovation hub",
        "state": "Maharashtra",
        "center": {"lat": 18.5204, "lng": 73.8567, "zoom": 13},
        "safety_index": 92,
        "cleanliness_index": 88,
        "food_fame": "SPDP, Puneri Misal & Shrewsbury Biscuits",
        "landmarks_count": 12,
        "emergency_count": "6 Police • 6 Hospitals",
        "image": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?w=800&auto=format&fit=crop&q=60",
        "badge": "Heritage & Student Capital",
        "traffic_hotspot": "Navale Bridge Slope"
    },
    {
        "id": "ahmedabad",
        "name": "Ahmedabad",
        "greeting": "Kem Cho Amdavad",
        "tagline": "UNESCO World Heritage City, vibrant street gastronomy & Sabarmati Riverfront",
        "state": "Gujarat",
        "center": {"lat": 23.0225, "lng": 72.5714, "zoom": 13},
        "safety_index": 95,
        "cleanliness_index": 91,
        "food_fame": "Manek Chowk Pav Bhaji, Khaman Dhokla & Fafda Jalebi",
        "landmarks_count": 10,
        "emergency_count": "5 Police • 5 Hospitals",
        "image": "https://images.unsplash.com/photo-1584824486509-112e4181ff6b?w=800&auto=format&fit=crop&q=60",
        "badge": "Heritage & Safe Nightlife",
        "traffic_hotspot": "Kalupur Station & SG Highway"
    },
    {
        "id": "mumbai",
        "name": "Mumbai",
        "greeting": "Ram Ram Maharashtra",
        "tagline": "The Maximum City, coastal promenades, colonial architecture & 24/7 energy",
        "state": "Maharashtra",
        "center": {"lat": 18.9220, "lng": 72.8347, "zoom": 13},
        "safety_index": 90,
        "cleanliness_index": 82,
        "food_fame": "Vada Pav, Irani Maska Chai & Bombay Sandwich",
        "landmarks_count": 11,
        "emergency_count": "6 Police • 6 Hospitals",
        "image": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&auto=format&fit=crop&q=60",
        "badge": "Coastal Megacity & Financial Capital",
        "traffic_hotspot": "WEH Kalanagar & Saki Naka"
    },
    {
        "id": "delhi",
        "name": "Delhi",
        "greeting": "Namaste Dilli",
        "tagline": "Heart of the nation, Mughal forts, culinary gallis & grand boulevards",
        "state": "National Capital Region",
        "center": {"lat": 28.6139, "lng": 77.2090, "zoom": 13},
        "safety_index": 81,
        "cleanliness_index": 76,
        "food_fame": "Paranthe Wali Gali, Chole Bhature & Butter Chicken",
        "landmarks_count": 10,
        "emergency_count": "5 Police • 5 Hospitals",
        "image": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format&fit=crop&q=60",
        "badge": "Imperial Monuments & Food Gallis",
        "traffic_hotspot": "Ashram Flyover & Kashmere Gate"
    },
    {
        "id": "bangalore",
        "name": "Bangalore",
        "greeting": "Gothilla Bengaluru",
        "tagline": "India's Silicon Valley, leafy canopies, specialty cafes & pub culture",
        "state": "Karnataka",
        "center": {"lat": 12.9716, "lng": 77.5946, "zoom": 13},
        "safety_index": 91,
        "cleanliness_index": 87,
        "food_fame": "Benne Dosa, Filter Kaapi & VV Puram Street Food",
        "landmarks_count": 10,
        "emergency_count": "5 Police • 5 Hospitals",
        "image": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?w=800&auto=format&fit=crop&q=60",
        "badge": "Tech Capital & Garden City",
        "traffic_hotspot": "Silk Board Junction & Tin Factory"
    }
]

# --- AHMEDABAD DATASET ("Kem Cho Amdavad") ---
AHMEDABAD_PLACES = [
    {
        "id": "ahm-1",
        "name": "Sabarmati Ashram (Gandhi Ashram)",
        "category": "heritage",
        "zone": "Ashram Road, Sabarmati",
        "lat": 23.0605,
        "lng": 72.5802,
        "rating": 4.8,
        "reviews_count": 42000,
        "budget": "Free Entry",
        "safety_score": 98,
        "lighting_score": 94,
        "cleanliness_score": 96,
        "image": "https://images.unsplash.com/photo-1584824486509-112e4181ff6b?w=800&auto=format&fit=crop&q=60",
        "tagline": "Epicenter of India's non-violent freedom struggle and Dandi March",
        "description": "Established by Mahatma Gandhi in 1917 on the tranquil banks of river Sabarmati. Preserves Hriday Kunj, Gandhi's spinning wheel, and original letters.",
        "cultural_significance": "Sanctuary of peace and the launch point of the historic 1930 Salt Satyagraha.",
        "best_time_to_visit": "8:30 AM - 6:30 PM",
        "night_safe": True,
        "audio_guide_text": "Kem Cho! Welcome to Sabarmati Ashram, the spiritual cradle of India's non-violent movement led by Mahatma Gandhi."
    },
    {
        "id": "ahm-2",
        "name": "Manek Chowk Midnight Street Food Bazaar",
        "category": "food",
        "zone": "Old Walled City, Mandvi Ni Pol",
        "lat": 23.0232,
        "lng": 72.5898,
        "rating": 4.7,
        "reviews_count": 38000,
        "budget": "₹150 - ₹300 per person",
        "safety_score": 93,
        "lighting_score": 95,
        "cleanliness_score": 84,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop&q=60",
        "tagline": "Jewelry market by day, world-famous midnight street food wonderland by night",
        "description": "Transforms after 9 PM into a bustling open-air dining spectacle serving Gwalior butter dosa, gigantic cheese pav bhaji, chocolate pineapple sandwiches, and Jamun shots.",
        "cultural_significance": "Quintessential Amdavadi night culture where families dine till 2 AM safely.",
        "best_time_to_visit": "9:30 PM - 1:30 AM",
        "night_safe": True,
        "audio_guide_text": "Step into Manek Chowk! Nowhere else on earth does a bullion market transform into an aromatic midnight feast of molten butter and fiery pav bhaji."
    },
    {
        "id": "ahm-3",
        "name": "Atal Pedestrian Bridge (Sabarmati Riverfront)",
        "category": "heritage",
        "zone": "Sabarmati Riverfront West",
        "lat": 23.0258,
        "lng": 72.5695,
        "rating": 4.8,
        "reviews_count": 29000,
        "budget": "₹30 entry",
        "safety_score": 97,
        "lighting_score": 98,
        "cleanliness_score": 97,
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&auto=format&fit=crop&q=60",
        "tagline": "Kite-inspired architectural footbridge with multi-level river vistas",
        "description": "Spectacular 300-meter footbridge connecting the flower garden to the event grounds. Illuminated with brilliant color-changing LEDs reflecting on the river.",
        "cultural_significance": "Modern architectural icon symbolizing Ahmedabad's International Kite Festival spirit.",
        "best_time_to_visit": "5:30 PM - 10:00 PM for sunset breezes",
        "night_safe": True,
        "audio_guide_text": "Walking across the Atal Bridge, you see the Sabarmati Riverfront stretching under radiant architectural canopies."
    },
    {
        "id": "ahm-4",
        "name": "Sidi Saiyyed Mosque (Tree of Life)",
        "category": "heritage",
        "zone": "Lal Darwaja",
        "lat": 23.0270,
        "lng": 72.5815,
        "rating": 4.6,
        "reviews_count": 19000,
        "budget": "Free",
        "safety_score": 92,
        "lighting_score": 90,
        "cleanliness_score": 91,
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&auto=format&fit=crop&q=60",
        "tagline": "Intricate 1573 marble stone lattice window depicting intertwining tree boughs",
        "description": "Built during the Gujarat Sultanate, world-renowned for its stone jali carvings which serve as the design inspiration for the IIM Ahmedabad logo.",
        "cultural_significance": "Masterpiece of Indo-Islamic stone craftsmanship.",
        "best_time_to_visit": "Morning 9:00 AM - 12:00 PM",
        "night_safe": True,
        "audio_guide_text": "Look closely at the Sidi Saiyyed Jali — delicate marble branches carved so finely they resemble lace against the Gujarat sky."
    },
    {
        "id": "ahm-5",
        "name": "Law Garden Khau Gali & Handicraft Market",
        "category": "food",
        "zone": "Ellisbridge / CG Road",
        "lat": 23.0245,
        "lng": 72.5590,
        "rating": 4.7,
        "reviews_count": 31000,
        "budget": "₹100 - ₹250 per person",
        "safety_score": 96,
        "lighting_score": 95,
        "cleanliness_score": 89,
        "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800&auto=format&fit=crop&q=60",
        "tagline": "Traditional Kutch embroidery market, ice-dish golas & hot dabeli",
        "description": "Vibrant night street lined with stalls selling authentic Kutchi chaniya cholis and opposite it, food stalls dishing out buttery pav bhaji, dabeli, and kulfi.",
        "cultural_significance": "Hub of Gujarati festive shopping and lively street socializing.",
        "best_time_to_visit": "6:00 PM - 11:30 PM",
        "night_safe": True,
        "audio_guide_text": "Law Garden bursts with color, mirrored textiles, and sizzling hot snacks right in the heart of west Ahmedabad."
    }
]

AHMEDABAD_HAZARDS = [
    {
        "id": "ahm-haz-1",
        "name": "Kalupur Railway Station Crossroad",
        "zone": "Old City Gateway",
        "lat": 23.0265,
        "lng": 72.6010,
        "severity": "HIGH",
        "type": "Heavy Auto-Rickshaw Clutter & Pedestrian Congestion",
        "description": "Massive choke point between railway passenger exits, BRTS bus corridors, and three-wheeler lanes.",
        "safer_alternative": "Use Kalupur Metro Station underground skywalks to bypass surface road chaos."
    },
    {
        "id": "ahm-haz-2",
        "name": "SG Highway Pakwan Crossroad Merge",
        "zone": "Sarkhej-Gandhinagar Highway",
        "lat": 23.0375,
        "lng": 72.5085,
        "severity": "MEDIUM",
        "type": "High Speed Highway Service Lane Merge",
        "description": "Frequent lane collisions during evening rush hours when office commuters merge across fast lanes.",
        "safer_alternative": "Maintain flyover elevated lanes rather than navigating side service cuts."
    }
]

AHMEDABAD_EMERGENCY = {
    "police": [
        {
            "id": "ahm-pol-1",
            "name": "Navrangpura Police Station",
            "zone": "University / CG Road",
            "lat": 23.0360,
            "lng": 72.5570,
            "phone": "079-26442436",
            "alt_phone": "112",
            "address": "Near Commerce Six Roads, Navrangpura",
            "patrol_coverage": "CG Road, Gujarat University, Law Garden",
            "open_24_7": True
        },
        {
            "id": "ahm-pol-2",
            "name": "Ellisbridge Police Station",
            "zone": "Ellisbridge / Riverfront",
            "lat": 23.0210,
            "lng": 72.5680,
            "phone": "079-26578000",
            "alt_phone": "112",
            "address": "Near Town Hall, Ellisbridge",
            "patrol_coverage": "Sabarmati Riverfront Promenade, Paldi, Town Hall",
            "open_24_7": True
        }
    ],
    "hospitals": [
        {
            "id": "ahm-hosp-1",
            "name": "SVP Hospital (Sardar Vallabhbhai Patel Institute)",
            "zone": "Ellisbridge / Riverfront",
            "lat": 23.0205,
            "lng": 72.5710,
            "phone": "079-26577621",
            "ambulance": "108",
            "type": "1500+ Bed Apex Multi-Specialty Hospital",
            "address": "Sabarmati Riverfront, Ellisbridge, Ahmedabad",
            "beds": "1500+ Beds",
            "specialty": "24/7 Level-1 Trauma, Emergency & Critical Care",
            "open_24_7": True
        },
        {
            "id": "ahm-hosp-2",
            "name": "Civil Hospital Asarwa (Asia's Largest Hospital Campus)",
            "zone": "Asarwa / North Ahmedabad",
            "lat": 23.0535,
            "lng": 72.6025,
            "phone": "079-22680074",
            "ambulance": "108",
            "type": "Government Apex Hospital",
            "address": "Asarwa, Ahmedabad",
            "beds": "2800+ Beds",
            "specialty": "24/7 Government Trauma Casualty & Burns Unit",
            "open_24_7": True
        }
    ]
}

# --- MUMBAI DATASET ("Ram Ram Maharashtra") ---
MUMBAI_PLACES = [
    {
        "id": "mum-1",
        "name": "Gateway of India & Taj Mahal Palace",
        "category": "heritage",
        "zone": "Colaba / South Mumbai",
        "lat": 18.9220,
        "lng": 72.8347,
        "rating": 4.8,
        "reviews_count": 92000,
        "budget": "Free Entry",
        "safety_score": 96,
        "lighting_score": 98,
        "cleanliness_score": 90,
        "image": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&auto=format&fit=crop&q=60",
        "tagline": "Iconic 26-meter basalt arch overlooking the Arabian Sea and historic Taj Palace",
        "description": "Erected in 1924 to commemorate King George V's visit, standing beside the resilient 1903 Taj Mahal Palace hotel.",
        "cultural_significance": "Gateway to the subcontinent and enduring symbol of Mumbai's spirit.",
        "best_time_to_visit": "Sunrise or evening 5:30 PM - 9:30 PM",
        "night_safe": True,
        "audio_guide_text": "Ram Ram! Welcome to the Gateway of India. Gaze across the harbor waters where colonial ships once anchored beside Mumbai's grandest heritage."
    },
    {
        "id": "mum-2",
        "name": "Marine Drive Promenade (Queen's Necklace)",
        "category": "heritage",
        "zone": "Churchgate to Nariman Point",
        "lat": 18.9432,
        "lng": 72.8230,
        "rating": 4.9,
        "reviews_count": 87000,
        "budget": "Free Promenade",
        "safety_score": 97,
        "lighting_score": 98,
        "cleanliness_score": 94,
        "image": "https://images.unsplash.com/photo-1566552881560-0be862a7c445?w=800&auto=format&fit=crop&q=60",
        "tagline": "3.6 km sweeping sea-facing promenade with 1930s Art Deco architecture",
        "description": "World-famous arc of streetlights resembling a pearl necklace at night. Filled with couples, students, and morning joggers enjoying the sea breeze.",
        "cultural_significance": "UNESCO World Heritage Art Deco ensemble; Mumbai's favorite night sanctuary.",
        "best_time_to_visit": "Evening till past midnight (24/7 safe walking)",
        "night_safe": True,
        "audio_guide_text": "Marine Drive is the open-air living room of Mumbai. The waves crash against giant tetrapods while the city sparkles around you."
    },
    {
        "id": "mum-3",
        "name": "Kyani & Co. (Heritage Irani Cafe)",
        "category": "food",
        "zone": "Marine Lines / Kalbadevi",
        "lat": 18.9425,
        "lng": 72.8285,
        "rating": 4.6,
        "reviews_count": 31000,
        "budget": "₹80 - ₹200 per person",
        "safety_score": 93,
        "lighting_score": 90,
        "cleanliness_score": 88,
        "image": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800&auto=format&fit=crop&q=60",
        "tagline": "Mumbai's oldest surviving Irani cafe (1904) serving bun maska and chai",
        "description": "Bentwood chairs, checkered tablecloths, and mirrored walls. Famous for Irani chai, kheema ghotala, mawa cake, and cream rolls.",
        "cultural_significance": "Century-old Parsi-Irani culinary heritage defining Bombay breakfast.",
        "best_time_to_visit": "7:00 AM - 11:30 AM for breakfast",
        "night_safe": True,
        "audio_guide_text": "Dip your crisp bun maska into sweet Irani chai at Kyani & Co. — a tradition Mumbaikars have cherished since 1904."
    },
    {
        "id": "mum-4",
        "name": "Bandra Bandstand & Carter Road",
        "category": "food",
        "zone": "Bandra West",
        "lat": 19.0544,
        "lng": 72.8190,
        "rating": 4.7,
        "reviews_count": 48000,
        "budget": "₹200 - ₹600 per person",
        "safety_score": 96,
        "lighting_score": 96,
        "cleanliness_score": 93,
        "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800&auto=format&fit=crop&q=60",
        "tagline": "Sea-facing Bollywood celebrity boulevard and hip artisan cafes",
        "description": "Walk past Shah Rukh Khan's Mannat bungalow, Bandra Fort ruins, and the coastal cafe belt brimming with avocado toast, specialty coffee, and sunset views.",
        "cultural_significance": "Cosmopolitan, creative hub of modern Mumbai.",
        "best_time_to_visit": "5:00 PM - 10:30 PM",
        "night_safe": True,
        "audio_guide_text": "Bandra is the bohemian soul of Mumbai. Catch the sunset over the Arabian Sea and wander through Portuguese-era village lanes."
    }
]

MUMBAI_HAZARDS = [
    {
        "id": "mum-haz-1",
        "name": "Dadar Central / Western Interchange Station",
        "zone": "Dadar Central",
        "lat": 19.0180,
        "lng": 72.8425,
        "severity": "CRITICAL",
        "type": "Extreme Suburban Train Platform Crowd Surge",
        "description": "India's densest railway pedestrian hub. Massive platform footfall during 8:30 AM - 11 AM and 6 PM - 9 PM.",
        "safer_alternative": "Use overhead connector foot-bridges or travel outside peak office hours."
    },
    {
        "id": "mum-haz-2",
        "name": "Western Express Highway (Kalanagar Junction)",
        "zone": "Bandra East",
        "lat": 19.0610,
        "lng": 72.8490,
        "severity": "HIGH",
        "type": "BKC Connector Traffic Choke",
        "description": "Merging traffic from Bandra-Worli Sea Link into BKC IT district creates 40-minute crawl during rush hours.",
        "safer_alternative": "Utilize Mumbai Metro Line 3 or Line 2B elevated connections."
    }
]

MUMBAI_EMERGENCY = {
    "police": [
        {
            "id": "mum-pol-1",
            "name": "Colaba Police Station",
            "zone": "Colaba / Gateway",
            "lat": 18.9180,
            "lng": 72.8290,
            "phone": "022-22856817",
            "alt_phone": "112",
            "address": "B.K. Boman Behram Marg, Colaba",
            "patrol_coverage": "Gateway of India, Colaba Causeway, Taj Hotel",
            "open_24_7": True
        },
        {
            "id": "mum-pol-2",
            "name": "Marine Drive Police Station",
            "zone": "Churchgate / Promenade",
            "lat": 18.9380,
            "lng": 72.8250,
            "phone": "022-22812242",
            "alt_phone": "112",
            "address": "Veer Nariman Road, Churchgate",
            "patrol_coverage": "Marine Drive Promenade, Wankhede Stadium, Nariman Point",
            "open_24_7": True
        }
    ],
    "hospitals": [
        {
            "id": "mum-hosp-1",
            "name": "KEM Hospital (King Edward Memorial)",
            "zone": "Parel / Central Mumbai",
            "lat": 19.0025,
            "lng": 72.8430,
            "phone": "022-24107000",
            "ambulance": "108",
            "type": "Apex Municipal Teaching Hospital",
            "address": "Acharya Donde Marg, Parel, Mumbai",
            "beds": "1800+ Beds",
            "specialty": "24/7 Level-1 Emergency Trauma & Critical Care",
            "open_24_7": True
        },
        {
            "id": "mum-hosp-2",
            "name": "Lilavati Hospital & Research Centre",
            "zone": "Bandra West",
            "lat": 19.0515,
            "lng": 72.8295,
            "phone": "022-26751000",
            "ambulance": "022-26568000",
            "type": "Multi-Specialty Emergency Hospital",
            "address": "A-791, Bandra Reclamation, Bandra West",
            "beds": "350+ Beds",
            "specialty": "24/7 Cardiac, Neuro & Accident Emergency Casualty",
            "open_24_7": True
        }
    ]
}

# --- DELHI DATASET ("Namaste Dilli") ---
DELHI_PLACES = [
    {
        "id": "del-1",
        "name": "India Gate & Kartavya Path",
        "category": "heritage",
        "zone": "Central Vista, New Delhi",
        "lat": 28.6129,
        "lng": 77.2295,
        "rating": 4.8,
        "reviews_count": 98000,
        "budget": "Free Promenade",
        "safety_score": 96,
        "lighting_score": 98,
        "cleanliness_score": 95,
        "image": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format&fit=crop&q=60",
        "tagline": "War memorial arch, lush lawns, ice cream carts & illuminated night walkways",
        "description": "Commemorates 84,000 soldiers with the Amar Jawan Jyoti. Redesigned with pristine canals, step-seating, and illuminated water fountains.",
        "cultural_significance": "National monument of valor and Delhi's favorite evening family gathering ground.",
        "best_time_to_visit": "Evening 6:00 PM - 10:30 PM",
        "night_safe": True,
        "audio_guide_text": "Namaste! Stand before the monumental arch of India Gate along Kartavya Path, lit brightly against the evening capital sky."
    },
    {
        "id": "del-2",
        "name": "Chandni Chowk & Paranthe Wali Gali",
        "category": "food",
        "zone": "Old Delhi (Purani Dilli)",
        "lat": 28.6560,
        "lng": 77.2300,
        "rating": 4.7,
        "reviews_count": 64000,
        "budget": "₹100 - ₹250 per person",
        "safety_score": 85,
        "lighting_score": 88,
        "cleanliness_score": 78,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop&q=60",
        "tagline": "Mughal-era bazaar serving crispy stuffed deep-fried parathas, jalebi & dahi bhalle",
        "description": "Lanes laid out in 1650 by Mughal Princess Jahanara. Home to legendary 1870s paratha shops, Natraj Dahi Bhalle, and Old Famous Jalebi Wala.",
        "cultural_significance": "Culinary crown of historic Hindustan and living Mughal bazaar heritage.",
        "best_time_to_visit": "11:00 AM - 8:30 PM",
        "night_safe": True,
        "audio_guide_text": "Follow the aromas of sputtering ghee and rabri jalebi down the labyrinth of Chandni Chowk."
    },
    {
        "id": "del-3",
        "name": "Connaught Place (CP Inner Circle)",
        "category": "food",
        "zone": "Connaught Place, New Delhi",
        "lat": 28.6328,
        "lng": 77.2197,
        "rating": 4.7,
        "reviews_count": 78000,
        "budget": "₹300 - ₹800 per person",
        "safety_score": 94,
        "lighting_score": 96,
        "cleanliness_score": 91,
        "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&auto=format&fit=crop&q=60",
        "tagline": "Grand Georgian circular colonnades, heritage bakeries, bars & live street music",
        "description": "Built in 1933, CP's white Palladian colonnades host iconic spots like Wenger's Deli (1926), United Coffee House, and underground Palika Bazaar.",
        "cultural_significance": "Commercial and leisure epicenter of modern New Delhi.",
        "best_time_to_visit": "11:00 AM - 11:00 PM",
        "night_safe": True,
        "audio_guide_text": "The massive white circular colonnades of Connaught Place connect Delhi's past with vibrant cosmopolitan coffee houses."
    }
]

DELHI_HAZARDS = [
    {
        "id": "del-haz-1",
        "name": "Ashram Flyover & Ring Road Merge",
        "zone": "South Delhi",
        "lat": 28.5710,
        "lng": 77.2605,
        "severity": "HIGH",
        "type": "Heavy Bottleneck Junction & Flyover Lane Merges",
        "description": "Notorious traffic jam corridor connecting Noida, South Delhi, and central corridors.",
        "safer_alternative": "Take the Delhi Metro Magenta / Pink Line interchange to skip surface jams entirely."
    }
]

DELHI_EMERGENCY = {
    "police": [
        {
            "id": "del-pol-1",
            "name": "Connaught Place Police Station",
            "zone": "CP / Central Delhi",
            "lat": 28.6315,
            "lng": 77.2185,
            "phone": "011-23363842",
            "alt_phone": "112",
            "address": "Inner Circle, Connaught Place",
            "patrol_coverage": "CP Blocks A to N, Janpath, Shivaji Stadium",
            "open_24_7": True
        }
    ],
    "hospitals": [
        {
            "id": "del-hosp-1",
            "name": "AIIMS New Delhi (Apex Trauma Center)",
            "zone": "Ansari Nagar / Ring Road",
            "lat": 28.5672,
            "lng": 77.2100,
            "phone": "011-26588500",
            "ambulance": "108",
            "type": "National Apex Trauma & Medical Center",
            "address": "Sri Aurobindo Marg, Ansari Nagar",
            "beds": "2500+ Beds",
            "specialty": "Level-1 Apex Trauma & 24/7 National Emergency",
            "open_24_7": True
        }
    ]
}

# --- BANGALORE DATASET ("Gothilla Bengaluru") ---
BANGALORE_PLACES = [
    {
        "id": "blr-1",
        "name": "Cubbon Park & Vidhana Soudha",
        "category": "heritage",
        "zone": "Central Bangalore",
        "lat": 12.9763,
        "lng": 77.5929,
        "rating": 4.8,
        "reviews_count": 68000,
        "budget": "Free Entry",
        "safety_score": 96,
        "lighting_score": 92,
        "cleanliness_score": 95,
        "image": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?w=800&auto=format&fit=crop&q=60",
        "tagline": "300 acres of emerald bamboo groves, red heritage library & Neo-Dravidian palace",
        "description": "Lungs of Bangalore created in 1870. Home to the towering granite Vidhana Soudha, Seshadri Iyer Memorial Hall, and Sunday dog park.",
        "cultural_significance": "Iconic symbol of the Garden City's green heritage and governance.",
        "best_time_to_visit": "Early morning 6:00 AM - 10:00 AM (Traffic-free walking hours)",
        "night_safe": True,
        "audio_guide_text": "Gothilla Bengaluru! Step into the verdant canopies of Cubbon Park, where 300 acres of bamboo and red colonial brick shelter the city."
    },
    {
        "id": "blr-2",
        "name": "Indiranagar 100ft Road Cafe & Craft Beer Strip",
        "category": "food",
        "zone": "Indiranagar",
        "lat": 12.9719,
        "lng": 77.6412,
        "rating": 4.7,
        "reviews_count": 52000,
        "budget": "₹350 - ₹900 per person",
        "safety_score": 95,
        "lighting_score": 97,
        "cleanliness_score": 92,
        "image": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800&auto=format&fit=crop&q=60",
        "tagline": "Epicenter of Bangalore's specialty coffee, microbreweries & tech founder catchups",
        "description": "Bustling cosmopolitan street packed with artisanal sourdough bakes, microbreweries (Toit), third-wave roasters, and lively nightlife.",
        "cultural_significance": "Vibrant epicenter of Bangalore's start-up and social culture.",
        "best_time_to_visit": "5:00 PM - 11:30 PM",
        "night_safe": True,
        "audio_guide_text": "From specialty filter roast aroma in the morning to craft brewing at night, Indiranagar 100ft Road is where Bengaluru's young energy pulses."
    },
    {
        "id": "blr-3",
        "name": "VV Puram Food Street (Thindi Beedi)",
        "category": "food",
        "zone": "V.V. Puram, Old Bangalore",
        "lat": 12.9525,
        "lng": 77.5780,
        "rating": 4.8,
        "reviews_count": 41000,
        "budget": "₹80 - ₹200 per person",
        "safety_score": 94,
        "lighting_score": 94,
        "cleanliness_score": 86,
        "image": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?w=800&auto=format&fit=crop&q=60",
        "tagline": "Bangalore's legendary vegetarian eat street for paddus, dosas & Congress bun",
        "description": "Only 200 meters long, but packed with 20+ legendary street carts serving crispy masala paddus, Davangere benne dosa, curd kodbale, and hot jalebis.",
        "cultural_significance": "Traditional Kannada street gastronomy hub dating back decades.",
        "best_time_to_visit": "Evening 6:30 PM - 11:00 PM",
        "night_safe": True,
        "audio_guide_text": "Dip your piping hot crispy paddu into coconut chutney on VV Puram Food Street — the delicious vegetarian crown of old Bengaluru."
    }
]

BANGALORE_HAZARDS = [
    {
        "id": "blr-haz-1",
        "name": "Silk Board Junction Traffic Choke",
        "zone": "Hosur Road / BTM Layout",
        "lat": 12.9175,
        "lng": 77.6235,
        "severity": "CRITICAL",
        "type": "India's Most Famous Traffic Chokepoint",
        "description": "Massive intersection of Electronic City Expressway, BTM, and Outer Ring Road. Peak hour waits can exceed 45 minutes.",
        "safer_alternative": "Take the elevated Electronic City tollway or internal BTM back-routes during morning rush."
    }
]

BANGALORE_EMERGENCY = {
    "police": [
        {
            "id": "blr-pol-1",
            "name": "Cubbon Park Police Station",
            "zone": "Central Bangalore",
            "lat": 12.9770,
            "lng": 77.5950,
            "phone": "080-22942583",
            "alt_phone": "112",
            "address": "Kasturba Road, Near Cubbon Park",
            "patrol_coverage": "Cubbon Park, MG Road, Vidhana Soudha",
            "open_24_7": True
        }
    ],
    "hospitals": [
        {
            "id": "blr-hosp-1",
            "name": "Manipal Hospital (Old Airport Road)",
            "zone": "Old Airport Road / Indiranagar",
            "lat": 12.9590,
            "lng": 77.6495,
            "phone": "080-25024444",
            "ambulance": "080-25023333",
            "type": "Tertiary Care Hospital",
            "address": "98, HAL Old Airport Rd, Kodihalli",
            "beds": "600+ Beds",
            "specialty": "24/7 Comprehensive Trauma & Emergency Care",
            "open_24_7": True
        }
    ]
}
