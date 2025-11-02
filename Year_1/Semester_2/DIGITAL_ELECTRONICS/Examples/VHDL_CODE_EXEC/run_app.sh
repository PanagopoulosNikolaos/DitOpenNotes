#!/bin/bash

# Define the Streamlit URL
STREAMLIT_URL="http://localhost:8501"

echo "Starting Streamlit server in headless mode..."
# Start Streamlit in headless mode in the background
streamlit run app.py --server.headless true &

# Get the process ID of the Streamlit server
STREAMLIT_PID=$!

echo "Waiting for server to start..."
# Wait a few seconds for the server to initialize
# You might need to adjust this sleep duration based on your system speed
sleep 3

echo "Opening $STREAMLIT_URL in Brave Browser..."
# Attempt to open the URL in Brave
# This assumes 'brave-browser' is the command to launch Brave on your system.
# If Brave is running, it might open a new tab or reuse an existing window
# depending on its settings.
brave-browser "$STREAMLIT_URL"

echo "--------------------------------------------------------------------"
echo "Streamlit app is running. Access it at $STREAMLIT_URL"
echo "The server process ID is $STREAMLIT_PID."
echo "To stop the server, run 'kill $STREAMLIT_PID' or press Ctrl+C in the terminal if you run Streamlit directly."
echo "--------------------------------------------------------------------"

# Optional: uncomment the line below if you want the script to wait until the Streamlit process ends
# wait $STREAMLIT_PID
