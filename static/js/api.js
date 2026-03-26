// API Configuration and Helper Functions
const API_BASE = '/api';

// API Request Helper
async function apiRequest(endpoint, options = {}) {
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers,
    };
    
    const response = await fetch(`${API_BASE}${endpoint}`, {
        ...options,
        headers,
    });
    
    if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(data.error || 'Request failed');
    }
    
    return response.json();
}

// Components API
const ComponentsAPI = {
    async getAll(filters = {}) {
        const params = new URLSearchParams(filters);
        return apiRequest(`/components/?${params}`);
    },
    
    async getById(id) {
        return apiRequest(`/components/${id}/`);
    },
    
    async create(data) {
        return apiRequest('/components/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
    },
    
    async update(id, data) {
        return apiRequest(`/components/${id}/`, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    },
    
    async delete(id) {
        return apiRequest(`/components/${id}/`, {
            method: 'DELETE',
        });
    },
};

// Projects API
const ProjectsAPI = {
    async getAll(filters = {}) {
        const params = new URLSearchParams(filters);
        return apiRequest(`/projects/?${params}`);
    },
    
    async getById(id) {
        return apiRequest(`/projects/${id}/`);
    },
    
    async create(data) {
        return apiRequest('/projects/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
    },
    
    async update(id, data) {
        return apiRequest(`/projects/${id}/`, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    },
    
    async delete(id) {
        return apiRequest(`/projects/${id}/`, {
            method: 'DELETE',
        });
    },
};

// BOM API
const BOMAPI = {
    async getByProject(projectId) {
        return apiRequest(`/bom/?project_id=${projectId}`);
    },
    
    async create(data) {
        return apiRequest('/bom/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
    },
    
    async delete(id) {
        return apiRequest(`/bom/${id}/`, {
            method: 'DELETE',
        });
    },
};

// Analytics API
const AnalyticsAPI = {
    async getData() {
        return apiRequest('/analytics/');
    },
};

// Utility Functions
function showAlert(message, type = 'success') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    const container = document.querySelector('.main-content') || document.body;
    container.insertBefore(alertDiv, container.firstChild);
    
    setTimeout(() => alertDiv.remove(), 3000);
}

function formatCurrency(value) {
    return `$${parseFloat(value).toFixed(2)}`;
}

function formatWeight(value) {
    return `${parseFloat(value).toFixed(3)} kg`;
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString();
}
