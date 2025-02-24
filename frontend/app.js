document.addEventListener('DOMContentLoaded', () => {
    const appElement = document.getElementById('app');

    // Show loading state
    appElement.innerHTML = '<h1>Coding Agent</h1><p>Loading...</p>';

    // Test API connection
    fetch('/api/test')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            appElement.innerHTML = `
                <h1>Coding Agent</h1>
                <p>${data.message}</p>
                <div class="features">
                    <button onclick="analyzeCode()">Analyze Code</button>
                    <button onclick="showSuggestions()">Get Suggestions</button>
                </div>
                <div id="output"></div>
            `;
        })
        .catch(error => {
            console.error('Error:', error);
            appElement.innerHTML = `
                <h1>Error</h1>
                <p>${error.message}</p>
                <button onclick="location.reload()">Try Again</button>
            `;
        });

    // Add analysis functions
    window.analyzeCode = async () => {
        const output = document.getElementById('output');
        output.innerHTML = '<p>Analyzing code...</p>';

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ project: 'current' })
            });

            const data = await response.json();
            output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        } catch (error) {
            output.innerHTML = `<p>Error: ${error.message}</p>`;
        }
    };

    window.showSuggestions = async () => {
        const output = document.getElementById('output');
        output.innerHTML = '<p>Getting suggestions...</p>';

        try {
            const response = await fetch('/api/suggestions', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ project: 'current' })
            });

            const data = await response.json();
            output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        } catch (error) {
            output.innerHTML = `<p>Error: ${error.message}</p>`;
        }
    };
});