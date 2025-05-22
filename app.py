import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm
import random
import pandas as pd
import json

from power_aware_trading import simulate_token_trading
from power_aware_trading import PowerAwareGraph
from power_aware_trading import SmartGridGraph

# --- Helper Function to Plot Graph ---
def plot_graph(graph, net_energy):
    pos = nx.spring_layout(graph, seed=42)
    values = list(net_energy.values())
    max_abs_val = max(abs(v) for v in values) if values else 1
    norm = mcolors.Normalize(vmin=-max_abs_val, vmax=max_abs_val)
    cmap = cm.RdYlGn
    node_colors = [cmap(norm(net_energy.get(node, 0))) for node in graph.nodes]

    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw_networkx(graph, pos, node_color=node_colors, with_labels=True, node_size=600, font_weight='bold', ax=ax)
    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax).set_label('Net Energy')
    ax.set_title("Smart Grid Graph (Green = Surplus, Red = Deficit)")
    ax.axis('off')
    st.pyplot(fig)
    plt.clf()

# --- Streamlit App ---
st.set_page_config(page_title="Power-Aware Token Trading", layout="wide")
st.title("🔋 Smart Energy Analytics: Power-Aware Token Trading")

# Sidebar Configuration
st.sidebar.header("Graph Settings")
num_nodes = st.sidebar.slider("Number of nodes", 5, 20, 6)
connection_density = st.sidebar.slider("Connection density", 0.1, 1.0, 0.5)
random_seed = st.sidebar.number_input("Random seed", value=42, step=1)
random.seed(random_seed)

# Graph Generation
base_graph = SmartGridGraph(num_nodes=num_nodes, connection_density=connection_density)
powers = {i: round(random.uniform(0.5, 2.0), 2) for i in range(num_nodes)}
edge_list = base_graph.get_edge_list()
power_graph = PowerAwareGraph(num_nodes=num_nodes, edge_list=edge_list, powers=powers)

# Net Energy Input
st.sidebar.markdown("### Net Energy per Node")
default_net_energy = {i: round(random.uniform(-5, 5), 1) for i in range(num_nodes)}
net_energy = {i: st.sidebar.number_input(f"Node {i}", value=default_net_energy[i], step=0.1) for i in range(num_nodes)}

# Plot the Graph
st.markdown("### 📊 Network Graph")
plot_graph(power_graph.get_graph(), net_energy)

# Simulate Token Trading
wallet, trades_log = simulate_token_trading(power_graph, net_energy.copy())

# Show Wallets
st.markdown("### 💰 Wallet Balances After Trading")
st.table({k: v['tokens'] for k, v in wallet.items()})

# Interactive Trade-by-Trade Reveal
st.markdown("### 🔄 Step Through Trades One by One")

# Initialize session state
if 'trade_index' not in st.session_state:
    st.session_state.trade_index = -1  # No trades shown initially

# Buttons to increment/decrement
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("➕ Show Next Trade"):
        if st.session_state.trade_index < len(trades_log) - 1:
            st.session_state.trade_index += 1

with col2:
    if st.button("➖ Remove Last Trade"):
        if st.session_state.trade_index > -1:
            st.session_state.trade_index -= 1

# Display cumulative log
if trades_log and st.session_state.trade_index >= 0:
    st.markdown(f"### 📋 Trades 1 to {st.session_state.trade_index + 1}")
    partial_log = trades_log[:st.session_state.trade_index + 1]
    df_partial = pd.DataFrame(partial_log)
    st.dataframe(df_partial)
elif not trades_log:
    st.info("⚠️ No trades executed. Check net energy distribution.")
else:
    st.info("🔎 Click ➕ to start revealing trades.")

# Export
st.markdown("### 📤 Export Options")
col1, col2 = st.columns(2)
with col1:
    if trades_log and st.button("Export All Trades as CSV"):
        csv = pd.DataFrame(trades_log).to_csv(index=False)
        st.download_button("Download CSV", csv, file_name="trades_log.csv", mime="text/csv")
with col2:
    if st.button("Export Wallets as JSON"):
        st.download_button("Download JSON", json.dumps(wallet, indent=2), file_name="wallets.json", mime="application/json")
