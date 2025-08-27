let map = null;
let markers = [];

function initMap(vehicleLocations = []) {
    // Initialize map
    map = L.map('map-container').setView([-1.286389, 36.817223], 13); // Nairobi coordinates
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    // Add vehicle markers
    updateVehicleMarkers(vehicleLocations);
}

function updateVehicleMarkers(vehicleLocations) {
    // Clear existing markers
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];
    
    // Add new markers
    vehicleLocations.forEach(vehicle => {
        const marker = L.marker([vehicle.latitude, vehicle.longitude])
            .addTo(map)
            .bindPopup(`
                <strong>${vehicle.vehicle}</strong><br>
                ${vehicle.make} ${vehicle.model}<br>
                Status: ${vehicle.status}<br>
                Last update: ${new Date(vehicle.timestamp).toLocaleString()}
            `);
        
        markers.push(marker);
    });
    
    // Fit map to show all markers
    if (markers.length > 0) {
        const group = new L.featureGroup(markers);
        map.fitBounds(group.getBounds().pad(0.1));
    }
}

function refreshVehicleLocations() {
    fetch('/api/vehicle-locations/')
        .then(response => response.json())
        .then(data => updateVehicleMarkers(data.locations))
        .catch(error => console.error('Error fetching vehicle locations:', error));
}

// Auto-refresh every 30 seconds
setInterval(refreshVehicleLocations, 30000);

// Export for use in other files
window.FleetTrackMap = {
    initMap,
    updateVehicleMarkers,
    refreshVehicleLocations
};
