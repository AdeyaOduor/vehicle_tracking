// Initialize Material Components
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all Material Design components
    const buttons = document.querySelectorAll('.mdc-button');
    buttons.forEach(button => {
        mdc.ripple.MDCRipple.attachTo(button);
    });
    
    const textFields = document.querySelectorAll('.mdc-text-field');
    textFields.forEach(field => {
        mdc.textField.MDCTextField.attachTo(field);
    });
    
    const checkboxes = document.querySelectorAll('.mdc-checkbox');
    checkboxes.forEach(checkbox => {
        mdc.checkbox.MDCCheckbox.attachTo(checkbox);
    });
    
    // Auto-dismiss messages after 5 seconds
    setTimeout(() => {
        const messages = document.querySelectorAll('.mdc-snackbar');
        messages.forEach(message => {
            message.style.display = 'none';
        });
    }, 5000);
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = this.querySelectorAll('[required]');
            let valid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    valid = false;
                    field.classList.add('mdc-text-field--invalid');
                } else {
                    field.classList.remove('mdc-text-field--invalid');
                }
            });
            
            if (!valid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });
});

// Utility functions
function showLoading(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading"></span> Processing...';
    button.disabled = true;
    return originalText;
}

function hideLoading(button, originalText) {
    button.innerHTML = originalText;
    button.disabled = false;
}

// API functions
async function apiRequest(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
                ...options.headers
            },
            ...options
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('API request failed:', error);
        throw error;
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Export for use in other files
window.FleetTrack = {
    utils: {
        showLoading,
        hideLoading,
        apiRequest,
        getCookie
    }
};
