import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def knapsack_dp(weights, values, capacity):
    n = len(values)
    dp = np.zeros((n + 1, capacity + 1), dtype=int)

    for idx in range(1, n + 1):
        for wdx in range(1, capacity + 1):
            if weights[idx - 1] <= wdx:
                dp[idx][wdx] = max(
                    dp[idx - 1][wdx],
                    dp[idx - 1][wdx - weights[idx - 1]] + values[idx - 1],
                )
            else:
                dp[idx][wdx] = dp[idx - 1][wdx]
    return dp


# get selected items from dp table
def get_selected_items(dp, wts, vals, capacity):
    selected_items = []
    n = len(vals)
    w = capacity

    for idx in range(n, 0, -1):
        if dp[idx][w] != dp[idx - 1][w]:
            selected_items.append(idx - 1)
            w -= wts[idx - 1]
    return selected_items


# there will be count of items selected for each weights


def plot_knapsack(weights, values, selected_items):
    n = len(values)
    fig, ax = plt.subplots()

    data = np.array([weights, values]).T
    colors = np.ones_like(data)

    for i in selected_items:
        colors[i, :] = 0

    cmap = ListedColormap(["green", "white"])

    ax.matshow(colors, cmap=cmap)

    for idx in range(n):
        ax.text(0, idx, f"{weights[idx]}", va="center", ha="center", color="black")
        ax.text(1, idx, f"{values[idx]}", va="center", ha="center", color="black")

    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Weight", "Value"])
    ax.set_yticks(range(n))
    ax.set_yticklabels([f"Item {idx + 1}" for idx in range(n)])

    st.pyplot(fig)


st.title("Knapsack problem - Graphical Sim")

n = st.number_input("Number of Items", min_value=1, value=4)
weights = [st.slider(f"Weight of item {idx + 1}", 1, 100, 10) for idx in range(n)]
values = [st.slider(f"values of item {idx + 1}", 1, 100, 20) for idx in range(n)]
capacity = st.slider("Knapsack Capacity", 1, 100, 50)

if st.button("solve"):
    dp = knapsack_dp(weights, values, capacity)
    max_value = dp[n][capacity]
    selected_items = get_selected_items(dp, weights, values, capacity)
    st.write(f"Maximum value: {max_value}")
    st.write(f"Selected items: {selected_items}")
    plot_knapsack(weights, values, selected_items)

if st.checkbox("Show DP Table"):
    dp = knapsack_dp(weights, values, capacity)
    st.write(dp)
