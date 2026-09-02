#!/bin/bash

# Ορισμός του URL του Streamlit
STREAMLIT_URL="http://localhost:8501"

echo "Εκκίνηση του server Streamlit σε λειτουργία headless..."
# Εκκίνηση του Streamlit σε λειτουργία headless στο παρασκήνιο
streamlit run app.py --server.headless true &

# Λήψη του ID διεργασίας του server Streamlit
STREAMLIT_PID=$!

echo "Αναμονή για την εκκίνηση του server..."
# Αναμονή μερικών δευτερολέπτων για την αρχικοποίηση του server
# Ενδέχεται να χρειαστεί να προσαρμόσετε αυτή τη διάρκεια ανάλογα με την ταχύτητα του συστήματος σας
sleep 3

echo "Opening $STREAMLIT_URL in default system browser..."
xdg-open "$STREAMLIT_URL" 2>/dev/null || python3 -m webbrowser "$STREAMLIT_URL" 2>/dev/null || echo "Please open $STREAMLIT_URL in your browser."

echo "--------------------------------------------------------------------"
echo "Η εφαρμογή Streamlit εκτελείται. Πρόσβαση στο $STREAMLIT_PID"
echo "Το ID διεργασίας του server είναι $STREAMLIT_PID."
echo "Για να σταματήσετε το server, εκτελέστε 'kill $STREAMLIT_PID' ή πατήστε Ctrl+C στο τερματικό αν εκτελείτε το Streamlit απευθείας."
echo "--------------------------------------------------------------------"

# Προαιρετικό: αποσυμβιβάστε την παρακάτω γραμμή αν θέλετε το σενάριο να περιμένει μέχρι να τελειώσει η διεργασία Streamlit
# wait $STREAMLIT_PID