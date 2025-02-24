# Run backend server
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "backend/app.py"

# Wait for server to start
Start-Sleep -Seconds 5

# Open browser
Start-Process "http://localhost:5000"