/**
 * UrbanPulse Pune - Frontend Logic
 * Complete map controller, safe routing, locality comparator,
 * crowdsourced reports, audio guide synthesis, and AI concierge.
 */

// Global State
let map;
let markersLayer;
let hazardsLayer;
let corridorsLayer;
let routePolylineLayer;
let policeLayer;
let hospitalsLayer;
let allPlaces = [];
let allHazards = [];
let allCorridors = [];
let allPolice = [];
let allHospitals = [];
let currentCategory = 'all';
let currentPlaceForModal = null;
let comparisonChartInstance = null;
let nightSafetyModeActive = false;
let safeHavenModeActive = false;

// Initialize on Load
document.addEventListener('DOMContentLoaded', async () => {
  lucide.createIcons();
  initMap();
  await loadTelemetry();
  await loadPlaces();
  await loadHazards();
  await loadCorridors();
  await loadEmergencyServices();
  await loadReports();
  initComparator();
  renderSelectedRoute();
});

// 1. MAP INITIALIZATION
function initMap() {
  // Center on Pune (Shaniwar Wada / Deccan core)
  map = L.map('map', {
    zoomControl: false
  }).setView([18.5204, 73.8567], 13);

  // Position Zoom control bottom-right
  L.control.zoom({ position: 'bottomright' }).addTo(map);

  // Use official OpenStreetMap free public tiles (No API key required)
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // Create Layer Groups
  markersLayer = L.layerGroup().addTo(map);
  hazardsLayer = L.layerGroup().addTo(map);
  corridorsLayer = L.layerGroup().addTo(map);
  routePolylineLayer = L.layerGroup().addTo(map);
  policeLayer = L.layerGroup();
  hospitalsLayer = L.layerGroup();

  // Map click listener for quick reporting
  map.on('click', (e) => {
    // Optional click to locate
  });

  // Ensure full container dimension calculation
  setTimeout(() => {
    map.invalidateSize();
  }, 200);
  window.addEventListener('resize', () => {
    if (map) map.invalidateSize();
  });
}

// 2. DATA LOADERS
async function loadTelemetry() {
  try {
    const res = await fetch('/api/telemetry');
    const data = await res.json();
    document.getElementById('tempDisplay').innerText = `${data.weather.temp} Pune (${data.weather.condition})`;
    document.getElementById('aqiDisplay').innerText = `${data.air_quality.aqi} (${data.air_quality.status.split(' ')[0]})`;
    document.getElementById('trafficDisplay').innerText = data.traffic_summary.congestion_index;
  } catch (err) {
    console.warn('Telemetry load fallback', err);
  }
}

async function loadPlaces() {
  try {
    const res = await fetch('/api/places');
    allPlaces = await res.json();
    renderPlacesCards(allPlaces);
    renderPlacesMarkers(allPlaces);
  } catch (err) {
    console.error('Failed to load places', err);
  }
}

async function loadHazards() {
  try {
    const res = await fetch('/api/hazards');
    allHazards = await res.json();
    renderHazardsMarkers(allHazards);
  } catch (err) {
    console.error('Failed to load hazards', err);
  }
}

async function loadCorridors() {
  try {
    const res = await fetch('/api/corridors');
    allCorridors = await res.json();
    renderCorridors(allCorridors);
  } catch (err) {
    console.error('Failed to load corridors', err);
  }
}

async function loadEmergencyServices() {
  try {
    const res = await fetch('/api/emergency');
    const data = await res.json();
    allPolice = data.police || [];
    allHospitals = data.hospitals || [];
    renderPoliceMarkers(allPolice);
    renderHospitalMarkers(allHospitals);
  } catch (err) {
    console.error('Failed to load emergency services', err);
  }
}

function renderPoliceMarkers(policeList) {
  policeLayer.clearLayers();
  policeList.forEach(p => {
    const customIcon = L.divIcon({
      className: 'custom-marker marker-police',
      html: `<span>🚓</span>`,
      iconSize: [34, 34],
      iconAnchor: [17, 17]
    });
    const marker = L.marker([p.lat, p.lng], { icon: customIcon });
    marker.bindPopup(`
      <div class="text-slate-900 p-1 font-sans" style="min-width: 220px;">
        <div class="flex items-center justify-between text-[10px] mb-1">
          <span class="bg-blue-50 text-blue-700 font-bold px-1.5 py-0.5 rounded border border-blue-200">🚓 PUNE POLICE</span>
          <span class="text-emerald-700 font-semibold">● 24/7 Active</span>
        </div>
        <h4 class="font-bold text-xs text-slate-900">${p.name}</h4>
        <p class="text-[11px] text-slate-600 mb-1">📍 ${p.address}</p>
        <p class="text-[10px] text-blue-800 font-medium mb-2">Coverage: ${p.patrol_coverage}</p>
        <div class="flex gap-1.5">
          <a href="tel:${p.phone.replace(/[^0-9]/g, '')}" class="flex-1 text-center bg-blue-600 hover:bg-blue-700 text-white font-bold py-1.5 px-2 rounded-lg text-[11px] shadow-2xs">
            📞 Call ${p.phone}
          </a>
          <a href="tel:112" class="bg-rose-600 hover:bg-rose-700 text-white font-bold py-1.5 px-2.5 rounded-lg text-[11px] shadow-2xs">
            112
          </a>
        </div>
      </div>
    `);
    policeLayer.addLayer(marker);
  });
}

function renderHospitalMarkers(hospList) {
  hospitalsLayer.clearLayers();
  hospList.forEach(h => {
    const customIcon = L.divIcon({
      className: 'custom-marker marker-hospital',
      html: `<span>🏥</span>`,
      iconSize: [34, 34],
      iconAnchor: [17, 17]
    });
    const marker = L.marker([h.lat, h.lng], { icon: customIcon });
    marker.bindPopup(`
      <div class="text-slate-900 p-1 font-sans" style="min-width: 220px;">
        <div class="flex items-center justify-between text-[10px] mb-1">
          <span class="bg-rose-50 text-rose-700 font-bold px-1.5 py-0.5 rounded border border-rose-200">🏥 24/7 TRAUMA CARE</span>
          <span class="text-emerald-700 font-semibold">● Emergency Open</span>
        </div>
        <h4 class="font-bold text-xs text-slate-900">${h.name}</h4>
        <p class="text-[11px] text-slate-600 mb-1">📍 ${h.address}</p>
        <p class="text-[10px] text-slate-700 font-medium mb-0.5">Specialty: ${h.specialty}</p>
        <p class="text-[10px] text-emerald-700 font-semibold mb-2">Capacity: ${h.beds}</p>
        <div class="flex gap-1.5">
          <a href="tel:${h.phone.replace(/[^0-9]/g, '')}" class="flex-1 text-center bg-rose-600 hover:bg-rose-700 text-white font-bold py-1.5 px-2 rounded-lg text-[11px] shadow-2xs">
            📞 Call Casualty
          </a>
          <a href="tel:108" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-1.5 px-2.5 rounded-lg text-[11px] shadow-2xs">
            🚑 108
          </a>
        </div>
      </div>
    `);
    hospitalsLayer.addLayer(marker);
  });
}

// 3. MARKER RENDERING
function renderPlacesMarkers(places) {
  markersLayer.clearLayers();

  places.forEach(place => {
    let iconClass = 'marker-heritage';
    let iconEmoji = '🏛️';
    if (place.category === 'food') {
      iconClass = 'marker-food';
      iconEmoji = '🍛';
    } else if (place.category === 'budget') {
      iconClass = 'marker-budget';
      iconEmoji = '🎒';
    }

    const customIcon = L.divIcon({
      className: `custom-marker ${iconClass}`,
      html: `<span>${iconEmoji}</span>`,
      iconSize: [32, 32],
      iconAnchor: [16, 16]
    });

    const marker = L.marker([place.lat, place.lng], { icon: customIcon });
    
    // Popup
    marker.bindPopup(`
      <div class="text-slate-900 p-1 font-sans" style="min-width: 180px;">
        <h4 class="font-bold text-xs">${place.name}</h4>
        <p class="text-[10px] text-slate-600 mb-1">${place.zone}</p>
        <div class="flex items-center justify-between text-[11px] mb-2 font-medium">
          <span class="text-emerald-700">🛡️ Safety: ${place.safety_score}%</span>
          <span class="text-amber-700">${place.budget}</span>
        </div>
        <button onclick="openPlaceModal('${place.id}')" class="w-full bg-orange-600 hover:bg-orange-700 text-white text-[11px] font-semibold py-1 px-2 rounded">
          View & Audio Story
        </button>
      </div>
    `);

    markersLayer.addLayer(marker);
  });
}

function renderHazardsMarkers(hazards) {
  hazardsLayer.clearLayers();

  hazards.forEach(h => {
    const customIcon = L.divIcon({
      className: 'custom-marker marker-hazard',
      html: `<span>⚠️</span>`,
      iconSize: [34, 34],
      iconAnchor: [17, 17]
    });

    const marker = L.marker([h.lat, h.lng], { icon: customIcon });
    
    // Circle danger zone around it
    const circle = L.circle([h.lat, h.lng], {
      color: '#ef4444',
      fillColor: '#ef4444',
      fillOpacity: 0.22,
      radius: 450
    });

    marker.bindPopup(`
      <div class="text-slate-900 p-1 font-sans" style="min-width: 200px;">
        <div class="flex items-center gap-1 text-red-600 font-bold text-xs">
          <span>⚠️ CAUTION:</span> ${h.severity}
        </div>
        <h4 class="font-bold text-xs text-slate-900 mt-1">${h.name}</h4>
        <p class="text-[10px] text-red-700 font-medium mb-1">${h.type}</p>
        <p class="text-[11px] text-slate-700 leading-tight mb-2">${h.description}</p>
        <div class="bg-red-50 border border-red-200 p-1.5 rounded text-[10px] text-red-800">
          <strong>Safe Advice:</strong> ${h.safer_alternative}
        </div>
      </div>
    `);

    hazardsLayer.addLayer(marker);
    hazardsLayer.addLayer(circle);
  });
}

function renderCorridors(corridors) {
  corridorsLayer.clearLayers();

  corridors.forEach(c => {
    const latlngs = [
      [c.start.lat, c.start.lng],
      [c.end.lat, c.end.lng]
    ];

    // High safety polyline
    const line = L.polyline(latlngs, {
      color: '#10b981',
      weight: 6,
      opacity: 0.85,
      className: 'corridor-glow'
    });

    line.bindPopup(`
      <div class="text-slate-900 p-1 font-sans">
        <h4 class="font-bold text-xs text-emerald-800">🛡️ Verified Safe Corridor: ${c.name}</h4>
        <p class="text-[11px] text-slate-700 font-medium">Safety Rating: ${c.safety_rating}%</p>
        <ul class="text-[10px] text-slate-600 mt-1 list-disc list-inside">
          ${c.features.map(f => `<li>${f}</li>`).join('')}
        </ul>
      </div>
    `);

    corridorsLayer.addLayer(line);
  });
}

// 4. PLACES CARDS IN SIDEBAR
function renderPlacesCards(places) {
  const container = document.getElementById('placesList');
  container.innerHTML = '';

  if (places.length === 0) {
    container.innerHTML = `
      <div class="text-center py-8 text-slate-500 text-xs bg-white rounded-xl border border-slate-200">
        No Pune spots found matching your filter. Try another keyword.
      </div>
    `;
    return;
  }

  places.forEach(place => {
    const card = document.createElement('div');
    card.className = 'bg-white hover:bg-orange-50/20 border border-slate-200/90 hover:border-orange-300 p-3 rounded-xl transition cursor-pointer flex gap-3 shadow-card hover:shadow-card-hover group';
    card.onclick = () => {
      map.flyTo([place.lat, place.lng], 15, { duration: 1.2 });
      openPlaceModal(place.id);
    };

    let catBadge = '🏛️ Heritage';
    if (place.category === 'food') catBadge = '🍛 Food';
    if (place.category === 'budget') catBadge = '🎒 Stays';

    card.innerHTML = `
      <img src="${place.image}" alt="${place.name}" class="w-20 h-20 rounded-lg object-cover flex-shrink-0 group-hover:scale-102 transition duration-200">
      <div class="flex-1 min-w-0">
        <div class="flex items-center justify-between gap-1 mb-0.5">
          <span class="text-[10px] font-bold text-orange-600 uppercase tracking-wide">${catBadge}</span>
          <span class="text-[10px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.5 rounded">
            🛡️ ${place.safety_score}% Safe
          </span>
        </div>
        <h4 class="font-bold text-slate-900 text-xs truncate group-hover:text-orange-600 transition">${place.name}</h4>
        <p class="text-[11px] text-slate-500 truncate mb-1">${place.zone}</p>
        <p class="text-[10px] text-slate-600 line-clamp-2 leading-tight mb-1.5">${place.tagline}</p>
        <div class="flex items-center justify-between text-[10px] text-slate-500 font-medium">
          <span>⭐ ${place.rating} (${place.reviews_count.toLocaleString()})</span>
          <span class="text-amber-700 font-semibold">${place.budget}</span>
        </div>
      </div>
    `;
    container.appendChild(card);
  });
  lucide.createIcons();
}

// 5. TABS & FILTERING
function switchTab(tabId) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active-tab'));
  document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.add('hidden'));

  const activeBtn = document.getElementById(`tab-${tabId}`);
  const activePane = document.getElementById(`pane-${tabId}`);
  if (activeBtn) activeBtn.classList.add('active-tab');
  if (activePane) activePane.classList.remove('hidden');

  // Trigger chart resize if compare tab
  if (tabId === 'compare' && comparisonChartInstance) {
    comparisonChartInstance.resize();
  }
}

function filterCategory(category) {
  currentCategory = category;
  document.querySelectorAll('.cat-pill').forEach(pill => pill.classList.remove('active-pill'));
  event.target.classList.add('active-pill');

  if (category === 'hazards') {
    // Show hazards view
    renderHazardsAsCards();
    return;
  }

  let filtered = allPlaces;
  if (category !== 'all') {
    filtered = allPlaces.filter(p => p.category === category);
  }
  renderPlacesCards(filtered);
  renderPlacesMarkers(filtered);
}

function renderHazardsAsCards() {
  const container = document.getElementById('placesList');
  container.innerHTML = `
    <div class="bg-rose-50 border border-rose-200 p-2.5 rounded-xl text-xs text-rose-800 mb-2 font-medium">
      <strong>⚠️ Pune Real-World Accident Blackspots & Caution Zones</strong><br>
      Ground-truth telemetry on known high-risk intersections and slopes.
    </div>
  `;

  allHazards.forEach(h => {
    const card = document.createElement('div');
    card.className = 'bg-white border border-rose-200 hover:border-rose-300 p-3 rounded-xl transition cursor-pointer shadow-card hover:shadow-card-hover';
    card.onclick = () => {
      map.flyTo([h.lat, h.lng], 15, { duration: 1.2 });
    };

    card.innerHTML = `
      <div class="flex items-center justify-between mb-1">
        <span class="text-[10px] font-bold text-rose-700 bg-rose-50 border border-rose-200 px-1.5 py-0.5 rounded">${h.severity} ALERT</span>
        <span class="text-[10px] text-slate-500 font-medium">${h.zone}</span>
      </div>
      <h4 class="font-bold text-slate-900 text-xs mb-1">${h.name}</h4>
      <p class="text-[11px] text-rose-700 font-semibold mb-2">${h.type}</p>
      <p class="text-[10px] text-slate-600 mb-2 leading-relaxed">${h.description}</p>
      <div class="bg-emerald-50/70 p-2 rounded-lg text-[10px] text-emerald-800 border border-emerald-200">
        <strong>🛡️ Safer Route Advice:</strong> ${h.safer_alternative}
      </div>
    `;
    container.appendChild(card);
  });
}

function handleSearch(query) {
  const q = query.toLowerCase().trim();
  const filtered = allPlaces.filter(p => 
    p.name.toLowerCase().includes(q) ||
    p.zone.toLowerCase().includes(q) ||
    p.tagline.toLowerCase().includes(q) ||
    p.description.toLowerCase().includes(q)
  );
  renderPlacesCards(filtered);
  renderPlacesMarkers(filtered);
}

// 6. PLACE DETAILS MODAL & AUDIO GUIDE (SPEECH SYNTHESIS)
function openPlaceModal(placeId) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  currentPlaceForModal = place;

  document.getElementById('modalPlaceImg').src = place.image;
  document.getElementById('modalPlaceName').innerText = place.name;
  document.getElementById('modalPlaceZone').innerText = `📍 ${place.zone} • ${place.best_time_to_visit}`;
  document.getElementById('modalPlaceCategory').innerText = place.category;
  document.getElementById('modalPlaceTagline').innerText = `"${place.tagline}"`;
  document.getElementById('modalPlaceDesc').innerText = place.description;
  document.getElementById('modalPlaceSafety').innerText = `${place.safety_score}%`;
  document.getElementById('modalPlaceLighting').innerText = `${place.lighting_score}%`;
  document.getElementById('modalPlaceBudget').innerText = place.budget;
  document.getElementById('modalPlaceCultural').innerText = place.cultural_significance;

  // Reset audio button
  document.getElementById('audioGuideLabel').innerText = 'Listen to Audio Guide';

  document.getElementById('placeModal').classList.remove('hidden');
  lucide.createIcons();
}

function closePlaceModal() {
  if (window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
  document.getElementById('placeModal').classList.add('hidden');
}

function playAudioGuide() {
  if (!currentPlaceForModal) return;

  if (!window.speechSynthesis) {
    showToast('Speech audio is not supported in this browser.');
    return;
  }

  // If already speaking, pause/cancel
  if (window.speechSynthesis.speaking) {
    window.speechSynthesis.cancel();
    document.getElementById('audioGuideLabel').innerText = 'Listen to Audio Guide';
    return;
  }

  const textToRead = currentPlaceForModal.audio_guide_text || currentPlaceForModal.description;
  const utterance = new SpeechSynthesisUtterance(textToRead);
  utterance.rate = 0.95;
  utterance.pitch = 1.0;

  utterance.onstart = () => {
    document.getElementById('audioGuideLabel').innerText = 'Playing Audio Guide... (Click to Stop)';
  };
  utterance.onend = () => {
    document.getElementById('audioGuideLabel').innerText = 'Listen to Audio Guide';
  };
  utterance.onerror = () => {
    document.getElementById('audioGuideLabel').innerText = 'Listen to Audio Guide';
  };

  window.speechSynthesis.speak(utterance);
}

function navigateHereFromModal() {
  closePlaceModal();
  switchTab('safenav');
  showToast(`SafeNav loaded towards ${currentPlaceForModal.name}`);
}

// 7. SAFENAV SMART ROUTE ENGINE
async function renderSelectedRoute() {
  const routeId = document.getElementById('routeSelect').value;
  try {
    const res = await fetch(`/api/routes?route_id=${routeId}`);
    const route = await res.json();
    renderRouteUI(route);
  } catch (err) {
    console.error('Failed to load route', err);
  }
}

function renderRouteUI(route) {
  const container = document.getElementById('routeDetailsContainer');
  container.innerHTML = `
    <div class="flex items-center justify-between text-xs text-slate-600 font-semibold px-1 py-1">
      <span>From: <strong class="text-slate-900">${route.origin}</strong></span>
      <span>➔</span>
      <span>To: <strong class="text-slate-900">${route.destination}</strong></span>
    </div>
  `;

  // Draw the safe route by default
  drawRouteOnMap(route.modes.safe.coordinates, '#10b981', 'Safe & Lit Corridor');

  // Option 1: Safe & Lit
  const safeMode = route.modes.safe;
  const safeCard = document.createElement('div');
  safeCard.className = 'bg-white border-2 border-emerald-500/90 p-3.5 rounded-xl cursor-pointer hover:bg-emerald-50/30 transition shadow-card';
  safeCard.onclick = () => drawRouteOnMap(safeMode.coordinates, '#10b981', safeMode.name);

  safeCard.innerHTML = `
    <div class="flex items-center justify-between mb-1.5">
      <div class="flex items-center gap-1.5">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <h4 class="font-bold text-slate-900 text-xs">${safeMode.name}</h4>
      </div>
      <span class="text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold px-2 py-0.5 rounded-full">
        ${safeMode.duration} • 🛡️ ${safeMode.safety_score}% Safety
      </span>
    </div>
    <p class="text-[11px] text-slate-600 mb-2 leading-relaxed">${safeMode.path_description}</p>
    <div class="bg-emerald-50/70 border border-emerald-200 p-2 rounded-lg text-[10px] text-emerald-800 font-medium">
      <strong>Avoids Hazard:</strong> ${safeMode.hazards_avoided.join(', ')}
    </div>
  `;
  container.appendChild(safeCard);

  // Option 2: Fastest Shortcut (Unlit Warning)
  const fastMode = route.modes.fastest;
  const fastCard = document.createElement('div');
  fastCard.className = 'bg-white border border-slate-200 hover:border-amber-300 p-3 rounded-xl cursor-pointer transition shadow-card';
  fastCard.onclick = () => drawRouteOnMap(fastMode.coordinates, '#f59e0b', fastMode.name);

  fastCard.innerHTML = `
    <div class="flex items-center justify-between mb-1.5">
      <h4 class="font-bold text-slate-800 text-xs">${fastMode.name}</h4>
      <span class="text-[10px] bg-amber-50 text-amber-700 border border-amber-200 font-bold px-2 py-0.5 rounded-full">
        ${fastMode.duration} • ⚠️ ${fastMode.safety_score}% Safety
      </span>
    </div>
    <p class="text-[11px] text-slate-500 mb-2 leading-relaxed">${fastMode.path_description}</p>
    <div class="bg-amber-50/60 border border-amber-200 p-2 rounded-lg text-[10px] text-amber-800 font-medium">
      ${fastMode.caution_note}
    </div>
  `;
  container.appendChild(fastCard);

  // Option 3: Heritage Walk if available
  if (route.modes.heritage_walk) {
    const hwMode = route.modes.heritage_walk;
    const hwCard = document.createElement('div');
    hwCard.className = 'bg-white border border-slate-200 hover:border-purple-300 p-3 rounded-xl cursor-pointer transition shadow-card';
    hwCard.onclick = () => drawRouteOnMap(hwMode.coordinates, '#a855f7', hwMode.name);

    hwCard.innerHTML = `
      <div class="flex items-center justify-between mb-1.5">
        <h4 class="font-bold text-purple-800 text-xs flex items-center gap-1">🏛️ ${hwMode.name}</h4>
        <span class="text-[10px] bg-purple-50 text-purple-700 border border-purple-200 font-bold px-2 py-0.5 rounded-full">
          ${hwMode.duration} • 🛡️ ${hwMode.safety_score}% Safety
        </span>
      </div>
      <p class="text-[11px] text-slate-600 leading-relaxed">${hwMode.path_description}</p>
    `;
    container.appendChild(hwCard);
  }
}

function drawRouteOnMap(coords, color, name) {
  routePolylineLayer.clearLayers();

  const line = L.polyline(coords, {
    color: color,
    weight: 7,
    opacity: 0.9,
    dashArray: color === '#f59e0b' ? '6, 8' : null
  }).addTo(routePolylineLayer);

  // Start & End markers
  const startIcon = L.divIcon({
    className: 'custom-marker',
    html: `<span style="background: ${color}; width:100%; height:100%; border-radius:50%; display:flex; align-items:center; justify-content:center;">📍</span>`,
    iconSize: [26, 26]
  });
  const endIcon = L.divIcon({
    className: 'custom-marker',
    html: `<span style="background: ${color}; width:100%; height:100%; border-radius:50%; display:flex; align-items:center; justify-content:center;">🏁</span>`,
    iconSize: [26, 26]
  });

  L.marker(coords[0], { icon: startIcon }).addTo(routePolylineLayer);
  L.marker(coords[coords.length - 1], { icon: endIcon }).addTo(routePolylineLayer);

  map.fitBounds(line.getBounds(), { padding: [60, 60] });
  showToast(`Active Route: ${name}`);
}

// 8. SPOT & NEIGHBORHOOD COMPARATOR (BEST VS WORST)
async function initComparator() {
  await updateComparison();
}

async function updateComparison() {
  const zoneA = document.getElementById('compareZoneA').value;
  const zoneB = document.getElementById('compareZoneB').value;

  try {
    const res = await fetch(`/api/compare?zone_a=${zoneA}&zone_b=${zoneB}`);
    const data = await res.json();
    renderComparisonRadar(data);
    renderComparisonVerdict(data);
  } catch (err) {
    console.error('Failed to update comparison', err);
  }
}

function renderComparisonRadar(data) {
  const ctx = document.getElementById('comparisonChart').getContext('2d');

  const labels = ['Safety', 'Cleanliness', 'Affordability', 'Transit Accessibility', 'Greenery & Vibe', 'Night Safety'];
  const aScores = [
    data.zone_a.scores.safety,
    data.zone_a.scores.cleanliness,
    data.zone_a.scores.affordability,
    data.zone_a.scores.accessibility,
    data.zone_a.scores.greenery_vibe,
    data.zone_a.scores.night_safety
  ];
  const bScores = [
    data.zone_b.scores.safety,
    data.zone_b.scores.cleanliness,
    data.zone_b.scores.affordability,
    data.zone_b.scores.accessibility,
    data.zone_b.scores.greenery_vibe,
    data.zone_b.scores.night_safety
  ];

  if (comparisonChartInstance) {
    comparisonChartInstance.destroy();
  }

  comparisonChartInstance = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [
        {
          label: data.zone_a.name,
          data: aScores,
          backgroundColor: 'rgba(249, 115, 22, 0.25)',
          borderColor: '#f97316',
          pointBackgroundColor: '#f97316',
          pointBorderColor: '#fff',
          borderWidth: 2
        },
        {
          label: data.zone_b.name,
          data: bScores,
          backgroundColor: 'rgba(99, 102, 241, 0.25)',
          borderColor: '#6366f1',
          pointBackgroundColor: '#6366f1',
          pointBorderColor: '#fff',
          borderWidth: 2
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          angleLines: { color: 'rgba(0, 0, 0, 0.08)' },
          grid: { color: 'rgba(0, 0, 0, 0.06)' },
          pointLabels: {
            color: '#334155',
            font: { size: 10, weight: '600' }
          },
          ticks: {
            display: false,
            max: 100,
            min: 0
          }
        }
      },
      plugins: {
        legend: {
          labels: {
            color: '#1e293b',
            font: { size: 11, weight: 'bold' }
          }
        }
      }
    }
  });
}

function renderComparisonVerdict(data) {
  const container = document.getElementById('comparisonVerdict');
  const a = data.zone_a;
  const b = data.zone_b;

  container.innerHTML = `
    <!-- Summary pill -->
    <div class="bg-indigo-50 border border-indigo-200 p-3 rounded-xl text-xs text-indigo-950 font-medium">
      <strong class="text-indigo-700 font-bold">AI Verdict:</strong> ${data.insights.summary}
    </div>

    <!-- Breakdown Grid -->
    <div class="grid grid-cols-2 gap-2 text-xs">
      <!-- Zone A Card -->
      <div class="bg-white p-3 rounded-xl border border-orange-200 shadow-card">
        <h4 class="font-bold text-orange-600 text-xs">${a.name}</h4>
        <p class="text-[10px] text-slate-500 mb-2 font-medium">${a.category_tag}</p>
        <div class="space-y-1 text-[11px] text-slate-700">
          <div>🛡️ Safety: <strong class="text-emerald-700">${a.scores.safety}/100</strong></div>
          <div>💰 Budget Index: <strong class="text-amber-700">${a.scores.affordability}/100</strong></div>
        </div>
        <div class="mt-2 text-[10px] text-emerald-800">
          <strong>Pros:</strong>
          <ul class="list-disc list-inside text-slate-600 space-y-0.5">
            ${a.pros.map(p => `<li>${p}</li>`).join('')}
          </ul>
        </div>
      </div>

      <!-- Zone B Card -->
      <div class="bg-white p-3 rounded-xl border border-indigo-200 shadow-card">
        <h4 class="font-bold text-indigo-600 text-xs">${b.name}</h4>
        <p class="text-[10px] text-slate-500 mb-2 font-medium">${b.category_tag}</p>
        <div class="space-y-1 text-[11px] text-slate-700">
          <div>🛡️ Safety: <strong class="text-emerald-700">${b.scores.safety}/100</strong></div>
          <div>💰 Budget Index: <strong class="text-amber-700">${b.scores.affordability}/100</strong></div>
        </div>
        <div class="mt-2 text-[10px] text-emerald-800">
          <strong>Pros:</strong>
          <ul class="list-disc list-inside text-slate-600 space-y-0.5">
            ${b.pros.map(p => `<li>${p}</li>`).join('')}
          </ul>
        </div>
      </div>
    </div>
  `;
}

// 9. CITIZEN PULSE & REPORTS
async function loadReports(category = 'all') {
  try {
    const res = await fetch(`/api/reports?category=${category}`);
    const reports = await res.json();
    renderReportsFeed(reports);
  } catch (err) {
    console.error('Failed to load reports', err);
  }
}

function filterReports(cat) {
  document.querySelectorAll('.report-filter-pill').forEach(b => b.classList.remove('active-pill'));
  event.target.classList.add('active-pill');
  loadReports(cat);
}

function renderReportsFeed(reports) {
  const container = document.getElementById('reportsFeedList');
  container.innerHTML = '';

  reports.forEach(r => {
    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200/90 p-3.5 rounded-xl space-y-2 shadow-card';

    let badgeColor = 'bg-orange-50 text-orange-700 border border-orange-200';
    if (r.severity === 'CRITICAL') badgeColor = 'bg-rose-50 text-rose-700 border border-rose-200 font-bold';
    if (r.category === 'hidden_gem') badgeColor = 'bg-purple-50 text-purple-700 border border-purple-200 font-bold';

    card.innerHTML = `
      <div class="flex items-center justify-between text-[11px]">
        <span class="px-2 py-0.5 rounded-md ${badgeColor} text-[10px] uppercase font-semibold">${r.category.replace('_', ' ')}</span>
        <span class="text-slate-400 text-[10px] font-medium">${r.timestamp}</span>
      </div>
      <h4 class="font-bold text-slate-900 text-xs">${r.title}</h4>
      <p class="text-[11px] text-slate-600 leading-relaxed">${r.description}</p>
      
      ${r.voice_transcript ? `
        <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-[10px] text-slate-700 flex items-start gap-1.5 font-medium">
          <i data-lucide="mic" class="w-3.5 h-3.5 text-orange-500 flex-shrink-0 mt-0.5"></i>
          <div>
            <strong class="text-slate-900">Voice Note:</strong> "${r.voice_transcript}"
          </div>
        </div>
      ` : ''}

      <div class="flex items-center justify-between pt-1 border-t border-slate-100 text-[11px]">
        <span class="text-slate-500 text-[10px] font-medium">Reported by ${r.reported_by} • 📍 ${r.zone}</span>
        <button onclick="upvoteReport('${r.id}', this)" class="flex items-center gap-1 bg-slate-100 hover:bg-slate-200 px-2.5 py-1 rounded-lg text-slate-800 text-xs font-semibold transition">
          <i data-lucide="thumbs-up" class="w-3.5 h-3.5 text-orange-500"></i>
          <span>${r.upvotes}</span>
        </button>
      </div>
    `;
    container.appendChild(card);
  });
  lucide.createIcons();
}

async function upvoteReport(reportId, btn) {
  try {
    const res = await fetch(`/api/reports/${reportId}/upvote`, { method: 'POST' });
    const data = await res.json();
    btn.querySelector('span').innerText = data.upvotes;
    showToast('Upvote verified on Pune community grid!');
  } catch (err) {
    console.error('Failed upvote', err);
  }
}

function openReportModal() {
  document.getElementById('reportModal').classList.remove('hidden');
}

function closeReportModal() {
  document.getElementById('reportModal').classList.add('hidden');
}

async function handleReportSubmit(e) {
  e.preventDefault();
  const category = document.getElementById('reportCategory').value;
  const title = document.getElementById('reportTitle').value;
  const zone = document.getElementById('reportZone').value;
  const description = document.getElementById('reportDesc').value;
  const reportedBy = document.getElementById('reportAuthor').value || 'Anonymous Punekar';

  // Approximate center of Pune with jitter for realistic demo pin
  const centerLat = 18.5204 + (Math.random() - 0.5) * 0.04;
  const centerLng = 73.8567 + (Math.random() - 0.5) * 0.04;

  const payload = {
    title,
    category,
    zone,
    lat: centerLat,
    lng: centerLng,
    description,
    reported_by: reportedBy,
    media_type: 'text'
  };

  try {
    const res = await fetch('/api/reports', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await res.json();
    closeReportModal();
    showToast('Alert broadcasted live to Pune map!');
    
    // Add to map immediately
    const icon = L.divIcon({
      className: 'custom-marker marker-report',
      html: `<span>📢</span>`,
      iconSize: [32, 32]
    });
    L.marker([centerLat, centerLng], { icon })
      .addTo(map)
      .bindPopup(`<b>${title}</b><br>${description}`)
      .openPopup();
    
    map.flyTo([centerLat, centerLng], 14);
    switchTab('feed');
    loadReports();
  } catch (err) {
    console.error('Submit report failed', err);
  }
}

// 10. VOICE DICTATION (WEB SPEECH RECOGNITION)
function triggerVoiceInput(targetInputId) {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    showToast('Voice dictation not supported in browser. Typing works great!');
    return;
  }

  const recognition = new SpeechRecognition();
  recognition.lang = 'en-IN';
  recognition.interimResults = false;

  showToast('Listening... Speak now into your microphone');

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    const input = document.getElementById(targetInputId);
    input.value = (input.value ? input.value + ' ' : '') + transcript;
    showToast(`Transcribed: "${transcript}"`);
  };

  recognition.onerror = (e) => {
    console.warn('Voice recognition error', e);
    showToast('Microphone error or permission denied.');
  };

  recognition.start();
}

// 11. AI CONCIERGE CHAT
function sendQuickPrompt(promptText) {
  document.getElementById('chatInput').value = promptText;
  handleChatSubmit(new Event('submit'));
}

async function handleChatSubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById('chatInput');
  const msg = input.value.trim();
  if (!msg) return;

  input.value = '';

  const messagesDiv = document.getElementById('chatMessages');

  // User Message
  const userBubble = document.createElement('div');
  userBubble.className = 'flex items-start gap-2 justify-end';
  userBubble.innerHTML = `
    <div class="bg-gradient-to-r from-orange-500 to-amber-500 text-white rounded-2xl p-2.5 max-w-[85%] text-xs leading-relaxed shadow-sm font-medium">
      ${msg}
    </div>
  `;
  messagesDiv.appendChild(userBubble);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;

  // Loading AI indicator
  const loadingBubble = document.createElement('div');
  loadingBubble.className = 'flex items-start gap-2';
  loadingBubble.id = 'ai-loading';
  loadingBubble.innerHTML = `
    <div class="w-6 h-6 rounded-full bg-cyan-600 flex items-center justify-center text-[10px] font-bold text-white flex-shrink-0">
      AI
    </div>
    <div class="bg-white border border-slate-200 rounded-2xl p-2.5 text-slate-500 text-xs shadow-card">
      Thinking about Pune context...
    </div>
  `;
  messagesDiv.appendChild(loadingBubble);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;

  try {
    const res = await fetch('/api/ai-concierge', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg })
    });
    const data = await res.json();

    loadingBubble.remove();

    // AI Response Bubble
    const aiBubble = document.createElement('div');
    aiBubble.className = 'flex items-start gap-2';
    aiBubble.innerHTML = `
      <div class="w-6 h-6 rounded-full bg-cyan-600 flex items-center justify-center text-[10px] font-bold text-white flex-shrink-0">
        AI
      </div>
      <div class="bg-white border border-slate-200 rounded-2xl p-3 text-slate-800 max-w-[88%] text-xs leading-relaxed whitespace-pre-line shadow-card font-normal">
        ${data.reply}
      </div>
    `;
    messagesDiv.appendChild(aiBubble);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

  } catch (err) {
    loadingBubble.remove();
    console.error('Chat error', err);
  }
}

// 12. NIGHT SAFETY MODE TOGGLE
function toggleNightSafetyMode() {
  nightSafetyModeActive = !nightSafetyModeActive;
  const btn = document.getElementById('nightModeBtn');
  const mapElement = document.getElementById('map');

  if (nightSafetyModeActive) {
    mapElement.classList.add('night-mode');
    btn.classList.add('bg-indigo-600', 'text-white', 'border-indigo-600');
    btn.classList.remove('bg-slate-100', 'text-slate-700', 'border-slate-200');
    showToast('🌙 Night Safety Mode Active: Highlighting well-lit corridors & CCTV zones');
    
    // Auto-focus on safe corridor
    map.flyTo([18.525, 73.845], 14);
  } else {
    mapElement.classList.remove('night-mode');
    btn.classList.remove('bg-indigo-600', 'text-white', 'border-indigo-600');
    btn.classList.add('bg-slate-100', 'text-slate-700', 'border-slate-200');
    showToast('Daylight Exploration Mode Restored');
  }
}

// 13. SIDEBAR TOGGLE (FULL SCREEN MAP)
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('hidden');
  setTimeout(() => {
    map.invalidateSize();
  }, 200);
}

// 14. SAFE HAVEN (POLICE & HOSPITALS) TOGGLE
function toggleSafeHavenMode() {
  safeHavenModeActive = !safeHavenModeActive;
  const btn = document.getElementById('safeHavenBtn');
  const panel = document.getElementById('safeHavenPanel');
  const policeToggle = document.getElementById('layerPoliceToggle');
  const hospToggle = document.getElementById('layerHospitalsToggle');

  if (safeHavenModeActive) {
    map.addLayer(policeLayer);
    map.addLayer(hospitalsLayer);
    if (policeToggle) policeToggle.checked = true;
    if (hospToggle) hospToggle.checked = true;
    if (panel) panel.classList.remove('hidden');
    btn.classList.add('bg-rose-600', 'text-white', 'border-rose-600', 'animate-pulse');
    btn.classList.remove('bg-rose-50', 'text-rose-700', 'border-rose-200');
    map.flyTo([18.5204, 73.8567], 13);
    showToast('🚨 Safe Haven Active: 6 Police Stations & 6 Trauma Hospitals Illuminated!');
  } else {
    map.removeLayer(policeLayer);
    map.removeLayer(hospitalsLayer);
    if (policeToggle) policeToggle.checked = false;
    if (hospToggle) hospToggle.checked = false;
    if (panel) panel.classList.add('hidden');
    btn.classList.remove('bg-rose-600', 'text-white', 'border-rose-600', 'animate-pulse');
    btn.classList.add('bg-rose-50', 'text-rose-700', 'border-rose-200');
    showToast('Emergency Safe Grid Deactivated');
  }
}

// 15. LAYER TOGGLES
function toggleLayer(layerName) {
  if (layerName === 'hazards') {
    const chk = document.getElementById('layerHazardsToggle').checked;
    if (chk) map.addLayer(hazardsLayer); else map.removeLayer(hazardsLayer);
  } else if (layerName === 'corridors') {
    const chk = document.getElementById('layerCorridorsToggle').checked;
    if (chk) map.addLayer(corridorsLayer); else map.removeLayer(corridorsLayer);
  } else if (layerName === 'police') {
    const chk = document.getElementById('layerPoliceToggle').checked;
    if (chk) map.addLayer(policeLayer); else map.removeLayer(policeLayer);
  } else if (layerName === 'hospitals') {
    const chk = document.getElementById('layerHospitalsToggle').checked;
    if (chk) map.addLayer(hospitalsLayer); else map.removeLayer(hospitalsLayer);
  }
}

// 15. TOAST HELPER
function showToast(message) {
  const toast = document.getElementById('toast');
  document.getElementById('toastMsg').innerText = message;
  toast.classList.remove('translate-y-20', 'opacity-0');
  setTimeout(() => {
    toast.classList.add('translate-y-20', 'opacity-0');
  }, 3200);
}
