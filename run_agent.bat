@echo off
cd C:\Users\sanjp\Voyage\Agents\coding-agent\backend
start python app.py
cd ..\frontend
start http://localhost:5000