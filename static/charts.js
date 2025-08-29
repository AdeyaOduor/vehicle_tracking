// static/js/charts.js
let charts = {};

function initCharts(data) {
    // Vehicle Status Chart
    initVehicleStatusChart(data.vehicleStats);
    
    // Maintenance Status Chart
    initMaintenanceStatusChart(data.maintenanceStats);
    
    // Fuel Consumption Chart
    initFuelConsumptionChart(data.fuelStats);
}

function initVehicleStatusChart(stats) {
    const ctx = document.getElementById('vehicle-status-chart');
    if (!ctx) return;
    
    charts.vehicleStatus = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Active', 'Maintenance', 'Inactive'],
            datasets: [{
                data: [stats.active, stats.maintenance, stats.inactive],
                backgroundColor: [
                    '#4caf50', // Green
                    '#ff9800', // Orange
                    '#f44336'  // Red
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                title: {
                    display: true,
                    text: 'Vehicle Status Distribution'
                }
            }
        }
    });
}

function initMaintenanceStatusChart(stats) {
    const ctx = document.getElementById('maintenance-status-chart');
    if (!ctx) return;
    
    charts.maintenanceStatus = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Completed', 'Pending', 'In Progress'],
            datasets: [{
                label: 'Maintenance Tickets',
                data: [stats.completed, stats.pending, stats.in_progress],
                backgroundColor: [
                    '#4caf50', // Green
                    '#ff9800', // Orange
                    '#2196f3'  // Blue
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Maintenance Tickets Status'
                }
            }
        }
    });
}

function initFuelConsumptionChart(stats) {
    const ctx = document.getElementById('fuel-consumption-chart');
    if (!ctx) return;
    
    charts.fuelConsumption = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            datasets: [{
                label: 'Liters Consumed',
                data: [120, 150, 180, 200],
                borderColor: '#1976d2',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Weekly Fuel Consumption'
                }
            }
        }
    });
}

function updateCharts(newData) {
    if (charts.vehicleStatus) {
        charts.vehicleStatus.data.datasets[0].data = [
            newData.vehicleStats.active,
            newData.vehicleStats.maintenance,
            newData.vehicleStats.inactive
        ];
        charts.vehicleStatus.update();
    }
    
    if (charts.maintenanceStatus) {
        charts.maintenanceStatus.data.datasets[0].data = [
            newData.maintenanceStats.completed,
            newData.maintenanceStats.pending,
            newData.maintenanceStats.in_progress
        ];
        charts.maintenanceStatus.update();
    }
}

// Export for use in other files
window.FleetTrackCharts = {
    initCharts,
    updateCharts
};
