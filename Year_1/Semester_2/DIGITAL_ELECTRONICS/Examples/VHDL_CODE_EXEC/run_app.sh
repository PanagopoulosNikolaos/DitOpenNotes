#!/bin/bash

# Define the Streamlit URL
STREAMLIT_URL="http://localhost:8501"

echo "Starting Streamlit server in headless mode..."
# Start Streamlit in headless mode in the background
streamlit run app.py --server.headless true &

# Get the process ID of the Streamlit server
STREAMLIT_PID=$!

echo "Waiting for server to start..."
sleep 3

echo "Opening $STREAMLIT_URL in default browser..."
if command -v xdg-open > /dev/null; then
    xdg-open "$STREAMLIT_URL"
elif command -v brave-browser > /dev/null; then
    brave-browser "$STREAMLIT_URL"
elif command -v google-chrome > /dev/null; then
    google-chrome "$STREAMLIT_URL"
elif command -v firefox > /dev/null; then
    firefox "$STREAMLIT_URL"
else
    echo "Please open $STREAMLIT_URL in your browser."
fi

echo "--------------------------------------------------------------------"
echo "Streamlit app is running. Access it at $STREAMLIT_URL"
echo "The server process ID is $STREAMLIT_PID."
echo "To stop the server, run 'kill $STREAMLIT_PID' or press Ctrl+C in the terminal."
echo "--------------------------------------------------------------------"
