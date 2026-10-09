"""
Pune City Zone Database
Accurate geo-coordinates, heritage landmarks, famous food joints, budget hubs,
traffic blackspots, accident-prone areas, and neighborhood comparison profiles.
"""

# Pune Center Coordinate
PUNE_CENTER = {"lat": 18.5204, "lng": 73.8567, "zoom": 13}

# Curated Places across Pune City
PUNE_PLACES = [
    # --- HERITAGE & CULTURE ---
    {
        "id": "pune-heritage-1",
        "name": "Shaniwar Wada",
        "category": "heritage",
        "zone": "Old City (Shaniwar Peth)",
        "lat": 18.5196,
        "lng": 73.8553,
        "rating": 4.6,
        "reviews_count": 48200,
        "budget": "Free - ₹25 entry",
        "price_level": 1,
        "safety_score": 88,
        "lighting_score": 85,
        "cleanliness_score": 82,
        "accessibility_score": 90,
        "image": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?w=800&auto=format&fit=crop&q=60",
        "tagline": "Historic 18th-century fortification of the Maratha Peshwas",
        "description": "Built in 1732 by Peshwa Baji Rao I, this grand seven-story stone palace fortress was the seat of the Peshwa rulers. Known for its imposing Dilli Darwaza, lotus fountains, and tragic tales of Narayana Rao.",
        "cultural_significance": "Epicenter of the Maratha Empire during the 18th century; symbol of Pune's royal heritage.",
        "best_time_to_visit": "9:30 AM - 5:30 PM (Evening Light & Sound Show)",
        "night_safe": True,
        "audio_guide_text": "Welcome to Shaniwar Wada, the grand heart of the Maratha Peshwa empire. As you stand before the massive teak doors spiked with iron elephant-defenders at Dilli Darwaza, you step into 300 years of valor, intrigue, and resilient architecture."
    },
    {
        "id": "pune-heritage-2",
        "name": "Dagdusheth Halwai Ganpati Temple",
        "category": "heritage",
        "zone": "Budhwar Peth",
        "lat": 18.5165,
        "lng": 73.8560,
        "rating": 4.9,
        "reviews_count": 89400,
        "budget": "Free",
        "price_level": 1,
        "safety_score": 92,
        "lighting_score": 98,
        "cleanliness_score": 89,
        "accessibility_score": 86,
        "image": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?w=800&auto=format&fit=crop&q=60",
        "tagline": "Pune's most revered and ornate Ganesh temple",
        "description": "Founded by sweet-maker Dagdusheth Gadve and his wife Lakshmibai in 1893 after the plague. Famous for its dazzling gold ornaments, vibrant aarti, and the massive public Ganeshotsav festival initiated with Lokmanya Tilak.",
        "cultural_significance": "Core of Pune's iconic 10-day Ganesh festival; philanthropic trust funding schools and hospitals.",
        "best_time_to_visit": "Early morning 6:00 AM or late night 10:00 PM for serene darshan",
        "night_safe": True,
        "audio_guide_text": "Dagdusheth Halwai Temple represents the soul of Pune's faith and social unity. Consecrated in 1893, this temple played a pivotal role during India's freedom struggle when Lokmanya Tilak transformed Ganesh Chaturthi into a public rallying celebration."
    },
    {
        "id": "pune-heritage-3",
        "name": "Aga Khan Palace",
        "category": "heritage",
        "zone": "Kalyani Nagar / Nagar Road",
        "lat": 18.5524,
        "lng": 73.9015,
        "rating": 4.5,
        "reviews_count": 31000,
        "budget": "₹25 entry",
        "price_level": 1,
        "safety_score": 95,
        "lighting_score": 90,
        "cleanliness_score": 94,
        "accessibility_score": 88,
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&auto=format&fit=crop&q=60",
        "tagline": "Italian arches and Mahatma Gandhi's memorial sanctuary",
        "description": "Constructed in 1892 by Sultan Muhammed Shah Aga Khan III to aid famine-hit villagers. Served as the prison for Mahatma Gandhi, Kasturba Gandhi, and Mahadev Desai during the 1942 Quit India Movement. Houses their sacred samadhis.",
        "cultural_significance": "Monument of National Importance and pivotal milestone of Indian Independence.",
        "best_time_to_visit": "9:00 AM - 5:00 PM (Lush green lawns and museum)",
        "night_safe": True,
        "audio_guide_text": "The Aga Khan Palace stands amid sprawling Italianate arches and calm gardens. During the Quit India movement of 1942, this monument became Gandhi's sanctuary of resolve, preserving memories of Kasturba Gandhi whose samadhi rests peacefully under the trees."
    },
    {
        "id": "pune-heritage-4",
        "name": "Pataleshwar Cave Temple",
        "category": "heritage",
        "zone": "Shivajinagar (JM Road)",
        "lat": 18.5284,
        "lng": 73.8502,
        "rating": 4.6,
        "reviews_count": 14200,
        "budget": "Free",
        "price_level": 1,
        "safety_score": 91,
        "lighting_score": 88,
        "cleanliness_score": 87,
        "accessibility_score": 94,
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&auto=format&fit=crop&q=60",
        "tagline": "8th-century monolithic rock-cut cave carved from single basalt rock",
        "description": "Carved during the Rashtrakuta period similar to the Elephanta Caves. Dedicated to Lord Shiva, this cave temple sits discreetly beneath the bustling modern asphalt of Jangli Maharaj Road.",
        "cultural_significance": "Oldest surviving architectural monument in metropolitan Pune.",
        "best_time_to_visit": "Morning 8:00 AM - 11:00 AM for cool underground tranquility",
        "night_safe": True,
        "audio_guide_text": "Step down from the modern buzz of JM Road into an 8th-century subterranean marvel. The Rashtrakuta artisans chiseled this entire temple directly out of solid volcanic basalt stone."
    },
    {
        "id": "pune-heritage-5",
        "name": "Sinhagad Fort",
        "category": "heritage",
        "zone": "Sinhagad Hills (South Pune)",
        "lat": 18.3663,
        "lng": 73.7558,
        "rating": 4.7,
        "reviews_count": 62000,
        "budget": "₹50 toll / Free trek",
        "price_level": 1,
        "safety_score": 79,
        "lighting_score": 60,
        "cleanliness_score": 78,
        "accessibility_score": 70,
        "image": "https://images.unsplash.com/photo-1600100397608-f010f443a055?w=800&auto=format&fit=crop&q=60",
        "tagline": "Legendary hill fortress of Tanaji Malusare's battle",
        "description": "Perched atop a 1,312-meter cliff overlooking Pune. Immortalized by the 1670 Battle of Sinhagad where Chhatrapati Shivaji Maharaj lamented 'Gad aala, pan Sinha gela' (The fort is won, but the Lion is lost). Famous for piping hot pithla bhakri and kanda bhaji.",
        "cultural_significance": "Icon of Maratha military fortitude and Pune's favorite weekend monsoon trek.",
        "best_time_to_visit": "Early morning 6:00 AM to 11:00 AM (Avoid foggy cliffs past sunset)",
        "night_safe": False,
        "audio_guide_text": "Sinhagad, the Lion's Fort, commands the Sahyadri mountains. Echoes of Tanaji Malusare's legendary night climb in 1670 linger across the wind-swept stone bastions."
    },

    # --- FOOD & HOSPITALITY ---
    {
        "id": "pune-food-1",
        "name": "FC Road Street Food Strip & Vaishali",
        "category": "food",
        "zone": "Fergusson College Road, Shivajinagar",
        "lat": 18.5236,
        "lng": 73.8415,
        "rating": 4.8,
        "reviews_count": 52000,
        "budget": "₹100 - ₹250 per person",
        "price_level": 1,
        "safety_score": 96,
        "lighting_score": 96,
        "cleanliness_score": 88,
        "accessibility_score": 98,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop&q=60",
        "tagline": "Epicenter of Pune college culture, SPDP, and filter coffee",
        "description": "From legendary Vaishali's Mysore Masala Dosa and SPDP (Sev Potato Dahi Puri) to Roopali's filter coffee and sidewalk clothing stalls, FC Road is the beating heart of Pune's youth and street gastronomy.",
        "cultural_significance": "Where generations of Pune university students, poets, and entrepreneurs debate over cutting chai.",
        "best_time_to_visit": "Evening 5:00 PM - 10:30 PM",
        "night_safe": True,
        "audio_guide_text": "Fergusson College Road is Pune's living room. Soak in the aromas of roasted filter coffee, crisp dosas, and street-side chat that has nurtured thinkers for over 60 years."
    },
    {
        "id": "pune-food-2",
        "name": "Kayani Bakery & Camp Burger",
        "category": "food",
        "zone": "Pune Camp (East Street)",
        "lat": 18.5135,
        "lng": 73.8785,
        "rating": 4.7,
        "reviews_count": 39000,
        "budget": "₹150 - ₹350 per person",
        "price_level": 1,
        "safety_score": 91,
        "lighting_score": 90,
        "cleanliness_score": 85,
        "accessibility_score": 90,
        "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800&auto=format&fit=crop&q=60",
        "tagline": "World-famous Shrewsbury biscuits and mammoth Camp King burgers",
        "description": "Kayani Bakery has baked melting buttery Shrewsbury biscuits and dense mawa cakes since 1955. Around the corner lies the legendary Burger (formerly Cafe Toons / King Burger) serving iconic jumbo steak and chicken burgers.",
        "cultural_significance": "Heritage Parsi & Anglo-Indian culinary identity of Pune Cantonment.",
        "best_time_to_visit": "3:30 PM - 7:00 PM (Queue forms early for Shrewsbury biscuits)",
        "night_safe": True,
        "audio_guide_text": "Step into Pune Camp's vintage East Street. The butter aroma from Kayani's ovens has made Shrewsbury biscuits a pilgrimage for travelers for seven decades."
    },
    {
        "id": "pune-food-3",
        "name": "Bedekar Misal & Tulsi Baug",
        "category": "food",
        "zone": "Narayan Peth",
        "lat": 18.5170,
        "lng": 73.8504,
        "rating": 4.6,
        "reviews_count": 27000,
        "budget": "₹80 - ₹150 per person",
        "price_level": 1,
        "safety_score": 90,
        "lighting_score": 86,
        "cleanliness_score": 83,
        "accessibility_score": 85,
        "image": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?w=800&auto=format&fit=crop&q=60",
        "tagline": "Traditional Puneri Punekar misal served with fresh white bread slice",
        "description": "Serving since 1948, Bedekar Tea Stall offers Pune's sweetest-spiciest authentic rassa misal topped with crispy farsan, accompanied by sweet jaggery-infused tea.",
        "cultural_significance": "Quintessential Puneri breakfast ritual in the historic Peth lanes.",
        "best_time_to_visit": "Breakfast 8:00 AM - 11:30 AM",
        "night_safe": True,
        "audio_guide_text": "Bedekar Misal in Narayan Peth represents authentic Puneri taste. Unlike Kolhapuri fiery tarri, Puneri misal blends a subtle hint of jaggery with fiery spices."
    },
    {
        "id": "pune-food-4",
        "name": "German Bakery & Koregaon Park Lane 7",
        "category": "food",
        "zone": "Koregaon Park (North Main Road)",
        "lat": 18.5362,
        "lng": 73.8940,
        "rating": 4.5,
        "reviews_count": 34000,
        "budget": "₹400 - ₹900 per person",
        "price_level": 3,
        "safety_score": 94,
        "lighting_score": 95,
        "cleanliness_score": 96,
        "accessibility_score": 92,
        "image": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800&auto=format&fit=crop&q=60",
        "tagline": "Bohemian bakes, keema pav, cold coffee, and leafy al-fresco cafes",
        "description": "Resilient and iconic, German Bakery is the meeting spot of travelers, expats, and creatives. Surrounded by Koregaon Park's lush banyan trees, upscale boutiques, and artisanal patisseries.",
        "cultural_significance": "Cosmopolitan, bohemian face of modern Pune.",
        "best_time_to_visit": "Late afternoon or evening till 11:30 PM",
        "night_safe": True,
        "audio_guide_text": "Nestled under giant banyan canopies, Koregaon Park's German Bakery has stood as a beacon of international cafe culture and bohemian camaraderie since 1988."
    },
    {
        "id": "pune-food-5",
        "name": "Sujata Mastani (Sadashiv Peth)",
        "category": "food",
        "zone": "Sadashiv Peth",
        "lat": 18.5115,
        "lng": 73.8525,
        "rating": 4.7,
        "reviews_count": 21000,
        "budget": "₹80 - ₹160 per glass",
        "price_level": 1,
        "safety_score": 92,
        "lighting_score": 89,
        "cleanliness_score": 90,
        "accessibility_score": 90,
        "image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=800&auto=format&fit=crop&q=60",
        "tagline": "Pune's signature thick milkshake topped with rich ice cream scoops",
        "description": "Named after Peshwa Baji Rao's beloved Mastani, this thick mango and custard apple dessert drink has been perfected by Sujata since 1968.",
        "cultural_significance": "Exclusive Pune dessert invention found nowhere else with such authenticity.",
        "best_time_to_visit": "12:00 PM - 11:00 PM",
        "night_safe": True,
        "audio_guide_text": "Mastani is Pune's regal dessert pride: a velvety, ultra-dense fruit shake crowned with heavy ice cream dollops and dry fruits."
    },

    # --- BUDGET & STUDENT STAYS / HUBS ---
    {
        "id": "pune-stay-1",
        "name": "Viman Nagar Student & Backpacker Belt",
        "category": "budget",
        "zone": "Viman Nagar (Near Airport)",
        "lat": 18.5679,
        "lng": 73.9143,
        "rating": 4.6,
        "reviews_count": 18000,
        "budget": "₹600 - ₹1400 / night",
        "price_level": 1,
        "safety_score": 93,
        "lighting_score": 94,
        "cleanliness_score": 91,
        "accessibility_score": 95,
        "image": "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=800&auto=format&fit=crop&q=60",
        "tagline": "Youthful hostel hub near Symbiosis, Phoenix Mall & Pune Airport",
        "description": "Safe, well-lit area with high student density, shared co-living spaces, and 24-hour food joints like Irani Cafe and Datta Digambar snacks.",
        "cultural_significance": "Modern student cosmopolitan zone with top-tier night walkability.",
        "best_time_to_visit": "Round the clock",
        "night_safe": True,
        "audio_guide_text": "Viman Nagar is vibrant, well-patrolled, and full of cozy coffee shops and budget hostels, making it ideal for solo explorers."
    },
    {
        "id": "pune-stay-2",
        "name": "Deccan Gymkhana & Model Colony",
        "category": "budget",
        "zone": "Deccan, Central Pune",
        "lat": 18.5186,
        "lng": 73.8398,
        "rating": 4.7,
        "reviews_count": 12500,
        "budget": "₹800 - ₹1800 / night",
        "price_level": 2,
        "safety_score": 95,
        "lighting_score": 95,
        "cleanliness_score": 92,
        "accessibility_score": 97,
        "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&auto=format&fit=crop&q=60",
        "tagline": "Safe, cultural heartland with tree-lined avenues and budget lodges",
        "description": "Right between BMCC, Fergusson College, and Prabhat Road. Central transit connectivity, peaceful residential pockets, and immediate access to Pune Metro.",
        "cultural_significance": "Intellectual and sports cradle of Pune with historic clubs and theaters.",
        "best_time_to_visit": "Year round",
        "night_safe": True,
        "audio_guide_text": "Deccan Gymkhana offers the perfect balance: high safety, great pedestrian avenues, and direct Metro access to Pune Railway Station."
    }
]

# --- SAFETY, ACCIDENT BLACKSPOTS & CIVIC HAZARDS ---
PUNE_HAZARDS_AND_ALERTS = [
    {
        "id": "hazard-1",
        "name": "Navale Bridge - Mumbai-Bangalore Bypass",
        "category": "accident_blackspot",
        "zone": "Katraj-Dehu Road Bypass (Vadgaon Budruk)",
        "lat": 18.4578,
        "lng": 73.8188,
        "severity": "CRITICAL",
        "type": "Accident-Prone Slope & Brake-Fail Zone",
        "description": "Known as Pune's most dangerous traffic corridor. A continuous 6 km downward slope causes heavy container trucks to overheat brakes. Multiple rear-end pileups reported.",
        "safer_alternative": "Use internal Sinhagad Road through Dhayari or plan transit during daylight off-peak hours.",
        "caution_time": "10:00 PM - 5:00 AM (Heavy container movement)"
    },
    {
        "id": "hazard-2",
        "name": "Swargate ST Stand Junction & Underpass",
        "category": "traffic_choke",
        "zone": "Swargate",
        "lat": 18.5018,
        "lng": 73.8582,
        "severity": "HIGH",
        "type": "Severe Pedestrian Congestion & Auto-rickshaw Clutter",
        "description": "Massive transit interchange between MSRTC state buses, PMPML city buses, and private cabs. Chaotic crossing points; high pickpocket caution reported during rush hours.",
        "safer_alternative": "Utilize pedestrian skywalks or access Metro entry gates rather than crossing directly at road grade.",
        "caution_time": "5:30 PM - 8:30 PM"
    },
    {
        "id": "hazard-3",
        "name": "University Circle (Ganeshkhind Road Underpass)",
        "category": "construction_bottleneck",
        "zone": "Shivajinagar / Savitribai Phule Pune University",
        "lat": 18.5412,
        "lng": 73.8305,
        "severity": "MEDIUM",
        "type": "Metro Rail Construction & Narrowed Lanes",
        "description": "Ongoing double-decker flyover and metro pillar construction creates lane bottlenecks towards Aundh and Baner. Waterlogging observed during sudden downpours.",
        "safer_alternative": "Take Senapati Bapat Road -> Range Hills bypass road.",
        "caution_time": "9:00 AM - 11:30 AM & 6:00 PM - 9:00 PM"
    },
    {
        "id": "hazard-4",
        "name": "Mutha Riverbed Backstretch (Late Night Caution)",
        "category": "night_safety",
        "zone": "Between Deccan and Shaniwar Peth riverbank",
        "lat": 18.5210,
        "lng": 73.8495,
        "severity": "HIGH",
        "type": "Poorly Lit Stretches Past 11 PM",
        "description": "Low streetlight coverage and isolated riverwalk tracks after market closing. Not recommended for solo pedestrians late at night.",
        "safer_alternative": "Stick to JM Road or Laxmi Road main lit thoroughfares with high police patrol visibility.",
        "caution_time": "11:00 PM - 5:30 AM"
    },
    {
        "id": "hazard-5",
        "name": "Chandani Chowk Highway Merge",
        "category": "traffic_choke",
        "zone": "Bavdhan / Kothrud Bypass",
        "lat": 18.5085,
        "lng": 73.7845,
        "severity": "MEDIUM",
        "type": "Complex Multi-Ramp Highway Merge",
        "description": "Multi-tier flyover complex can confuse first-time drivers. High speed merging lanes require alert driving.",
        "safer_alternative": "Follow lane markings carefully into Paud Road slip lane.",
        "caution_time": "All day"
    }
]

# --- SAFE CORRIDORS (High Lighting, CCTV, Police Presence) ---
PUNE_SAFE_CORRIDORS = [
    {
        "id": "safe-corridor-1",
        "name": "Fergusson College Road (FC Road)",
        "zone": "Shivajinagar",
        "start": {"lat": 18.5290, "lng": 73.8440},
        "end": {"lat": 18.5180, "lng": 73.8390},
        "safety_rating": 98,
        "features": ["24/7 CCTV surveillance", "Heavy pedestrian activity till midnight", "Frequent beat marshals", "Continuous LED streetlights"]
    },
    {
        "id": "safe-corridor-2",
        "name": "Koregaon Park North Main Road",
        "zone": "Koregaon Park",
        "start": {"lat": 18.5390, "lng": 73.8890},
        "end": {"lat": 18.5350, "lng": 73.9050},
        "safety_rating": 95,
        "features": ["Private & municipal security patrols", "Tree-canopied, well-lit pavements", "Active late-night cafes"]
    },
    {
        "id": "safe-corridor-3",
        "name": "Jangli Maharaj Road (JM Road)",
        "zone": "Shivajinagar",
        "start": {"lat": 18.5305, "lng": 73.8510},
        "end": {"lat": 18.5215, "lng": 73.8445},
        "safety_rating": 96,
        "features": ["Wide smart-city pedestrian sidewalks", "High police presence", "Continuous food and business storefronts"]
    }
]

# --- NEIGHBORHOOD COMPARISON PROFILES (Best vs Worst) ---
PUNE_NEIGHBORHOODS = {
    "koregaon_park": {
        "id": "koregaon_park",
        "name": "Koregaon Park (KP)",
        "category_tag": "Cosmopolitan & Nightlife",
        "description": "Pune's premier upscale neighbourhood known for banyan tree lanes, fine dining, international cafes, and calm greenery.",
        "scores": {
            "safety": 94,
            "cleanliness": 96,
            "affordability": 38,  # Premium / high cost of living
            "accessibility": 88,
            "greenery_vibe": 95,
            "night_safety": 92
        },
        "pros": ["Extremely safe, upscale environment", "Lush green canopy & walkable inner lanes", "Best global dining and boutique cafes"],
        "cons": ["Expensive food & stay rates", "Weekend traffic on North Main Road bottleneck"],
        "ideal_for": "Expats, luxury tourists, evening cafe dates"
    },
    "fc_road_deccan": {
        "id": "fc_road_deccan",
        "name": "FC Road & Deccan Gymkhana",
        "category_tag": "Student Hub & Culture",
        "description": "Vibrant heart of central Pune with heritage educational institutions, iconic eateries, and bustling shopping strips.",
        "scores": {
            "safety": 95,
            "cleanliness": 86,
            "affordability": 90,  # Highly budget friendly for students
            "accessibility": 96,
            "greenery_vibe": 89,
            "night_safety": 93
        },
        "pros": ["Unbeatable budget food & street shopping", "Excellent public transport & Metro access", "High footfall makes it extremely safe"],
        "cons": ["Parking is very difficult", "Crowded pavements on weekends"],
        "ideal_for": "Students, solo backpackers, foodies on a budget"
    },
    "viman_nagar": {
        "id": "viman_nagar",
        "name": "Viman Nagar",
        "category_tag": "Airport & Co-Living Belt",
        "description": "Modern urban suburb housing universities, IT professionals, modern shopping malls, and student housing.",
        "scores": {
            "safety": 93,
            "cleanliness": 91,
            "affordability": 74,
            "accessibility": 92,
            "greenery_vibe": 82,
            "night_safety": 91
        },
        "pros": ["Proximity to Airport & Phoenix Marketcity", "Safe 24/7 cafes and co-working spaces", "Clean planned street grid"],
        "cons": ["Distance from Pune's historic old city / Peth areas", "Airport road traffic during peak hours"],
        "ideal_for": "Business travelers, airport transit, student rentals"
    },
    "swargate": {
        "id": "swargate",
        "name": "Swargate & Sarasbaug",
        "category_tag": "Transit Nexus & High Density",
        "description": "Massive transit interchange connecting old Pune to southern highways; high commercial and bus activity.",
        "scores": {
            "safety": 78,
            "cleanliness": 68,
            "affordability": 94,  # Cheap transit and lodgings
            "accessibility": 95,
            "greenery_vibe": 64,
            "night_safety": 72
        },
        "pros": ["Instant bus connections to everywhere in Maharashtra", "Direct Metro terminal point", "Very cheap lodging and traditional snacks"],
        "cons": ["High vehicular noise and dust pollution", "Crowded pedestrian chaos around the ST terminal", "Lower late-night safety score"],
        "ideal_for": "Inter-city bus commuters, budget travelers catching dawn buses"
    },
    "katraj": {
        "id": "katraj",
        "name": "Katraj & Ambegaon",
        "category_tag": "Southern Highway & Lake Zone",
        "description": "Known for the Rajiv Gandhi Zoological Park, Katraj Lake, and rapid suburban sprawl along the southern bypass.",
        "scores": {
            "safety": 75,
            "cleanliness": 72,
            "affordability": 92,
            "accessibility": 78,
            "greenery_vibe": 80,
            "night_safety": 68
        },
        "pros": ["Budget accommodation & dairy hub", "Famous Katraj Zoo and snake sanctuary"],
        "cons": ["Proximity to Navale Bridge accident blackspot", "Highway congestion and heavy truck traffic", "Far from central cultural core"],
        "ideal_for": "Highway stopovers, zoo excursions"
    },
    "kothrud": {
        "id": "kothrud",
        "name": "Kothrud & Paud Road",
        "category_tag": "Residential & Cultural Pride",
        "description": "Traditional Puneri cultural stronghold, home to classic theaters, educational hubs, and fast-growing Metro links.",
        "scores": {
            "safety": 96,
            "cleanliness": 92,
            "affordability": 82,
            "accessibility": 94,
            "greenery_vibe": 88,
            "night_safety": 92
        },
        "pros": ["Peaceful family neighborhoods with very low crime", "Pune Metro corridor direct to civil court", "Rich Maharashtrian cultural vibe"],
        "cons": ["Peak hour traffic near Paud Phata flyover", "Can feel quiet late at night"],
        "ideal_for": "Cultural exploration, family stays, residential quiet"
    }
}

# --- CURATED ROUTES ---
PUNE_SAMPLE_ROUTES = [
    {
        "id": "route-1",
        "title": "Shaniwar Wada ➔ FC Road Strip",
        "distance": "3.8 km",
        "origin": "Shaniwar Wada (Old City)",
        "destination": "FC Road (Shivajinagar)",
        "modes": {
            "safe": {
                "name": "Smart Safe & Lit Corridor",
                "duration": "14 mins",
                "safety_score": 96,
                "lighting_score": 95,
                "path_description": "Cross Shivaji Bridge ➔ Turn onto Jangli Maharaj (JM) Road (Wide smart sidewalks, 24/7 CCTV, active shops) ➔ Enter FC Road.",
                "highlights": ["Pataleshwar Cave Temple", "Balgandharva Rangmandir", "Vaishali Cafe"],
                "hazards_avoided": ["Avoids unlit Mutha riverbed alleys and deserted late-night causeways."],
                "coordinates": [
                    [18.5196, 73.8553],
                    [18.5230, 73.8540],
                    [18.5265, 73.8510],
                    [18.5280, 73.8475],
                    [18.5250, 73.8430],
                    [18.5236, 73.8415]
                ]
            },
            "fastest": {
                "name": "Shortest Riverbed Cut",
                "duration": "11 mins",
                "safety_score": 68,
                "lighting_score": 52,
                "path_description": "Direct shortcut along the southern Mutha riverbed bypass into Deccan Gymkhana back-lanes.",
                "highlights": ["Riverbed bridge"],
                "hazards_avoided": [],
                "caution_note": "⚠️ Poorly lit after 9:30 PM. Potholes and isolated stretches reported.",
                "coordinates": [
                    [18.5196, 73.8553],
                    [18.5180, 73.8510],
                    [18.5190, 73.8460],
                    [18.5236, 73.8415]
                ]
            },
            "heritage_walk": {
                "name": "Peshwa Heritage Walking Trail",
                "duration": "35 mins (Walk)",
                "safety_score": 92,
                "lighting_score": 88,
                "path_description": "Shaniwar Wada ➔ Lal Mahal ➔ Tulsi Baug ➔ Vishrambaug Wada ➔ Sambhaji Park ➔ FC Road.",
                "highlights": ["Lal Mahal", "Vishrambaug Wada woodwork", "Chhatrapati Sambhaji Park"],
                "hazards_avoided": ["Pedestrian-friendly historical route with verified footpaths."],
                "coordinates": [
                    [18.5196, 73.8553],
                    [18.5185, 73.8562],
                    [18.5165, 73.8540],
                    [18.5152, 73.8510],
                    [18.5210, 73.8460],
                    [18.5236, 73.8415]
                ]
            }
        }
    },
    {
        "id": "route-2",
        "title": "Swargate ➔ Koregaon Park (KP)",
        "distance": "6.2 km",
        "origin": "Swargate Bus Terminus",
        "destination": "German Bakery, Koregaon Park",
        "modes": {
            "safe": {
                "name": "Safe Cantonment Corridor",
                "duration": "22 mins",
                "safety_score": 94,
                "lighting_score": 92,
                "path_description": "Via Nehru Road ➔ Camp MG Road (High security cantonment zone) ➔ Koregaon Park South Main Road.",
                "highlights": ["Kayani Bakery Camp", "Army Sports Institute", "Osho Garden"],
                "hazards_avoided": ["Avoids dimly lit railway siding roads near Ghorpadi yard."],
                "coordinates": [
                    [18.5018, 73.8582],
                    [18.5080, 73.8680],
                    [18.5135, 73.8785],
                    [18.5240, 73.8890],
                    [18.5362, 73.8940]
                ]
            },
            "fastest": {
                "name": "Railway Underpass Cut",
                "duration": "18 mins",
                "safety_score": 72,
                "lighting_score": 60,
                "path_description": "Via Timber Market ➔ Ghorpadi railway gate shortcut.",
                "highlights": ["Timber market"],
                "hazards_avoided": [],
                "caution_note": "⚠️ Railway gate waiting delays and isolated underpasses late night.",
                "coordinates": [
                    [18.5018, 73.8582],
                    [18.5090, 73.8650],
                    [18.5200, 73.8820],
                    [18.5362, 73.8940]
                ]
            }
        }
    }
]

# --- PRE-SEEDED CROWDSOURCED CITIZEN REPORTS ---
PUNE_CITIZEN_REPORTS_INITIAL = [
    {
        "id": "report-101",
        "title": "Heavy truck oil spill near Navale Bridge ramp",
        "category": "safety_hazard",
        "zone": "Vadgaon Budruk / Navale Bridge",
        "lat": 18.4582,
        "lng": 73.8190,
        "description": "Oil slick observed on left service lane going towards Katraj. Two-wheelers skidding. Traffic police deployed sand.",
        "reported_by": "Rohan Deshmukh",
        "timestamp": "12 mins ago",
        "upvotes": 43,
        "verified": True,
        "severity": "CRITICAL",
        "media_type": "photo",
        "photo_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=600&auto=format&fit=crop&q=60",
        "voice_transcript": "Reporting live from Navale bridge underpass. Slippery oil patch right before the signal, bikers please avoid the left lane."
    },
    {
        "id": "report-102",
        "title": "Street lights repaired & bright on JM Road Service Lane",
        "category": "safety_positive",
        "zone": "JM Road (Near Sambhaji Park)",
        "lat": 18.5245,
        "lng": 73.8470,
        "description": "PMC has installed new solar LED poles along the entire park jogger trail. Very bright and safe for women night runners.",
        "reported_by": "Pooja Kulkarni",
        "timestamp": "45 mins ago",
        "upvotes": 29,
        "verified": True,
        "severity": "LOW",
        "media_type": "text",
        "photo_url": None,
        "voice_transcript": None
    },
    {
        "id": "report-103",
        "title": "Hidden Gem: 50-year-old Ukadiche Modak stall discovered",
        "category": "hidden_gem",
        "zone": "Appa Balwant Chowk (ABC)",
        "lat": 18.5178,
        "lng": 73.8535,
        "description": "Steamy, authentic handmade modaks with warm ghee served in banana leaves behind the old book shops. Only ₹30 each!",
        "reported_by": "Chinmay Joshi",
        "timestamp": "2 hours ago",
        "upvotes": 58,
        "verified": True,
        "severity": "LOW",
        "media_type": "photo",
        "photo_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&auto=format&fit=crop&q=60",
        "voice_transcript": "Found this small family spot in ABC. Authentic coconut and jaggery filling, melts in your mouth."
    },
    {
        "id": "report-104",
        "title": "Sudden waterlogging at Alka Talkies Chowk",
        "category": "traffic_choke",
        "zone": "Alka Talkies / Sambhaji Bridge",
        "lat": 18.5140,
        "lng": 73.8465,
        "description": "Post 4 PM showers created 1-foot puddle near the bridge ramp. Traffic crawling towards Deccan.",
        "reported_by": "Ajit Pawar",
        "timestamp": "3 hours ago",
        "upvotes": 36,
        "verified": True,
        "severity": "MEDIUM",
        "media_type": "text",
        "photo_url": None,
        "voice_transcript": None
    }
]

# --- PUNE LIVE CITY TELEMETRY (Weather, Traffic, Air Quality) ---
PUNE_TELEMETRY = {
    "city": "Pune, Maharashtra",
    "weather": {
        "temp": "28°C",
        "condition": "Partly Cloudy",
        "humidity": "54%",
        "wind": "12 km/h WNW",
        "forecast": "Mild evening breeze, no rain expected tonight"
    },
    "air_quality": {
        "aqi": 84,
        "status": "Moderate (Satisfactory)",
        "recommendation": "Great for outdoor evening walks on FC Road and gardens."
    },
    "traffic_summary": {
        "overall_status": "Moderate Evening Flow",
        "congestion_index": "58/100",
        "major_hotspots": ["Navale Bridge (Bypass)", "University Circle", "Swargate ST Depot"],
        "clear_corridors": ["FC Road", "JM Road", "Kalyani Nagar Bridge"]
    }
}

# --- PUNE 24/7 EMERGENCY GRID (POLICE & HOSPITALS) ---
PUNE_EMERGENCY_SERVICES = {
    "police": [
        {
            "id": "police-1",
            "name": "Deccan Gymkhana Police Station",
            "zone": "FC Road / Deccan",
            "lat": 18.5188,
            "lng": 73.8395,
            "phone": "020-25674333",
            "alt_phone": "112",
            "type": "Police Station",
            "address": "Prabhat Road, Near Goodluck Cafe, Deccan",
            "patrol_coverage": "FC Road, BMCC, Fergusson College, Law College Rd",
            "open_24_7": True,
            "badge": "24/7 Beat Marshal Station"
        },
        {
            "id": "police-2",
            "name": "Shivajinagar Police Station",
            "zone": "Shivajinagar / JM Road",
            "lat": 18.5312,
            "lng": 73.8505,
            "phone": "020-25536263",
            "alt_phone": "112",
            "type": "Police Station",
            "address": "Opp. Sancheti Hospital, Jangli Maharaj Road",
            "patrol_coverage": "JM Road, Shivajinagar Railway Station, Sancheti Chowk",
            "open_24_7": True,
            "badge": "24/7 Smart City Control Node"
        },
        {
            "id": "police-3",
            "name": "Swargate Police Station",
            "zone": "Swargate",
            "lat": 18.5025,
            "lng": 73.8590,
            "phone": "020-24440232",
            "alt_phone": "112",
            "type": "Police Station",
            "address": "Satara Road, Swargate Bus Stand Compound",
            "patrol_coverage": "Swargate ST Stand, Sarasbaug, Mukundnagar",
            "open_24_7": True,
            "badge": "24/7 Transit Security Depot"
        },
        {
            "id": "police-4",
            "name": "Faraskhana Police Station",
            "zone": "Budhwar Peth / Dagdusheth",
            "lat": 18.5175,
            "lng": 73.8565,
            "phone": "020-24452233",
            "alt_phone": "112",
            "type": "Police Station",
            "address": "Budhwar Peth, near Shaniwar Wada & Dagdusheth Temple",
            "patrol_coverage": "Old Peth areas, Heritage walking routes, Laxmi Road",
            "open_24_7": True,
            "badge": "24/7 Heritage Quarter Unit"
        },
        {
            "id": "police-5",
            "name": "Bund Garden Police Station",
            "zone": "Bund Garden / Koregaon Park",
            "lat": 18.5370,
            "lng": 73.8820,
            "phone": "020-26123821",
            "alt_phone": "112",
            "type": "Police Station",
            "address": "Raja Bahadur Mill Road, Near Pune Station",
            "patrol_coverage": "Koregaon Park lanes, Pune Railway Station, Dhole Patil Rd",
            "open_24_7": True,
            "badge": "24/7 Night Corridor Unit"
        },
        {
            "id": "police-6",
            "name": "Bharati Vidyapeeth Police Station",
            "zone": "Katraj / Ambegaon (Navale Corridor)",
            "lat": 18.4550,
            "lng": 73.8500,
            "phone": "020-24372233",
            "alt_phone": "112",
            "type": "Police Station",
            "address": "Pune-Satara Highway, near Katraj Lake",
            "patrol_coverage": "Navale Bridge Bypass, Katraj Chowk, Ambegaon",
            "open_24_7": True,
            "badge": "24/7 Highway Patrol Base"
        }
    ],
    "hospitals": [
        {
            "id": "hosp-1",
            "name": "Sassoon General Hospital & Trauma Center",
            "zone": "Central Pune (Near Station)",
            "lat": 18.5255,
            "lng": 73.8745,
            "phone": "020-26128000",
            "ambulance": "108",
            "type": "24/7 Govt Trauma Center",
            "address": "Near Pune Railway Station, Sassoon Road",
            "beds": "1200+ Beds",
            "specialty": "Level-1 Apex Trauma & Emergency Casualty",
            "open_24_7": True,
            "free_service": "Government Emergency Casualty Available"
        },
        {
            "id": "hosp-2",
            "name": "Sancheti Hospital & Joint Disease Centre",
            "zone": "Shivajinagar (Sancheti Chowk)",
            "lat": 18.5325,
            "lng": 73.8495,
            "phone": "020-28999999",
            "ambulance": "020-28999100",
            "type": "Specialty Trauma Care",
            "address": "16, Shivaji Nagar, Sancheti Chowk, Pune",
            "beds": "200+ Beds",
            "specialty": "Accident, Orthopedic & Polytrauma Emergency",
            "open_24_7": True,
            "free_service": "24/7 Emergency ICU & Ambulance"
        },
        {
            "id": "hosp-3",
            "name": "Poona Hospital & Research Centre",
            "zone": "Deccan / Sadashiv Peth",
            "lat": 18.5135,
            "lng": 73.8445,
            "phone": "020-24331707",
            "ambulance": "020-24331708",
            "type": "Multi-Speciality Hospital",
            "address": "27, Sadashiv Peth, Near Alka Talkies",
            "beds": "300+ Beds",
            "specialty": "24/7 Cardiac & Critical Care Unit",
            "open_24_7": True,
            "free_service": "24/7 Emergency Blood Bank & Cath Lab"
        },
        {
            "id": "hosp-4",
            "name": "Ruby Hall Clinic (Sasoon Road)",
            "zone": "Dhole Patil Road / Koregaon Park",
            "lat": 18.5330,
            "lng": 73.8790,
            "phone": "020-66455100",
            "ambulance": "020-66455500",
            "type": "Tertiary Care Hospital",
            "address": "40, Sassoon Road, Pune",
            "beds": "600+ Beds",
            "specialty": "NABH-Accredited 24/7 Emergency & Air Ambulance",
            "open_24_7": True,
            "free_service": "24/7 Emergency Casualty"
        },
        {
            "id": "hosp-5",
            "name": "Sahyadri Super Speciality Hospital",
            "zone": "Deccan Gymkhana",
            "lat": 18.5150,
            "lng": 73.8340,
            "phone": "020-67213000",
            "ambulance": "020-67213100",
            "type": "Super Speciality Hospital",
            "address": "Plot No. 30 C, Erandwane, Karve Road",
            "beds": "250+ Beds",
            "specialty": "Neuro, Trauma, Burns & 24/7 Emergency",
            "open_24_7": True,
            "free_service": "24/7 Emergency Department"
        },
        {
            "id": "hosp-6",
            "name": "Smt. Kashibai Navale General Hospital",
            "zone": "Vadgaon Budruk (Navale Bridge Bypass)",
            "lat": 18.4610,
            "lng": 73.8160,
            "phone": "020-24107000",
            "ambulance": "108",
            "type": "Highway Emergency Hospital",
            "address": "Near Navale Bridge, Mumbai-Bangalore Highway",
            "beds": "500+ Beds",
            "specialty": "Immediate Highway Accident & Polytrauma Casualty",
            "open_24_7": True,
            "free_service": "Dedicated Accident Response Team"
        }
    ],
    "helplines": {
        "police_national": {"number": "112", "label": "All Emergency Dispatch"},
        "police_pune": {"number": "100", "label": "Pune City Police"},
        "women_safety": {"number": "1091", "label": "Women in Distress Helpline"},
        "ambulance": {"number": "108", "label": "National Ambulance Emergency"},
        "traffic_control": {"number": "020-26685000", "label": "Pune Traffic Police Helpline"},
        "senior_citizen": {"number": "1090", "label": "Elderly Support Helpline"}
    }
}

