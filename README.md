# ⚡ Power-Aware Token Trading Simulator

A simulation of smart energy token trading between nodes in a power network, optimized by power-aware graph algorithms.

---

## ✨ Features

- ⚡ Assigns power levels to each node and reweights edge costs accordingly
- 🔁 Computes optimized token transfers from surplus to deficit nodes
- 🧠 Uses a custom Dijkstra’s algorithm for power-aware routing
- 🌐 Visualizes network graph with energy status color mapping  
  (🟢 green = surplus, 🔴 red = deficit)
- 📋 Step-by-step trade log viewer with CSV/JSON export options
- 🖥️ Fully interactive Streamlit web interface

---

## 🛠️ Tech Stack

- 🐍 Python  
- 📊 Streamlit  
- 🔗 NetworkX  
- 🎨 Matplotlib  
- 🧾 Pandas  

---

## 🚀 Run Locally

```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/power-aware-token-trading.git  
cd power-aware-token-trading

# Step 2: Create environment and install dependencies
pip install -r requirements.txt

# Step 3: Launch the Streamlit app
streamlit run app.py
