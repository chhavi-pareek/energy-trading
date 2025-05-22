⚡ Power-Aware Token Trading Simulator
This project simulates a smart energy trading network using a power-aware model built on top of a graph. Nodes (homes) with surplus energy can transfer tokens to deficit nodes efficiently based on both connectivity and power levels, minimizing cost via a custom Dijkstra’s algorithm.



🚀 Features
Generates a random smart grid graph using NetworkX

Assigns power levels to each node and reweights edge costs accordingly

Computes optimized token transfers from surplus to deficit nodes

Visualizes network graph with energy status color mapping (green = surplus, red = deficit)

Step-by-step trade log viewer with CSV/JSON export options

Fully interactive Streamlit web interface



🛠️ Tech Stack
Python 🐍

Streamlit 📊

NetworkX 🔗

Matplotlib 🎨

Pandas 🧮



🧪 Run Locally
# Step 1: Clone the repo
git clone https://github.com/yourusername/power-aware-token-trading.git
cd power-aware-token-trading

# Step 2: Create environment
pip install -r requirements.txt

# Step 3: Launch the app
streamlit run app.py



🔧 Customize Parameters
Adjust number of nodes and connection density via sidebar

Manually input net energy values for each node

Walk through trades step by step using ➕ and ➖ buttons


📦 Export Options
Wallet balances after trading (JSON)

Trade logs with paths and costs (CSV)
