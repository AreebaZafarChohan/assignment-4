# Binary Search with Streamlit

import streamlit as st
import time
import matplotlib.pyplot as plt

# Function to perform binary search and yield steps
def binary_search_steps(arr, target):
    steps = []
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        steps.append((low, mid, high))
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return steps

# Function to plot the current step
def plot_step(arr, low, mid, high):
    colors = ['gray'] * len(arr)
    if low < len(arr):
        colors[low] = 'green'
    if mid < len(arr):
        colors[mid] = 'blue'
    if high < len(arr):
        colors[high] = 'red'
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color=colors)
    ax.set_xticks(range(len(arr)))
    ax.set_xticklabels(arr)
    st.pyplot(fig)

# Streamlit app
st.title("🔍 Binary Search Visualizer")
st.markdown("Visualize how binary search algorithm works step by step.")

# User inputs
array_input = st.text_input("Enter a sorted list of numbers (comma-separated):", "1,3,5,7,9,11,13,15")
target_input = st.number_input("Enter the target number:", value=7)

# Convert input string to list of integers
try:
    arr = list(map(int, array_input.strip().split(',')))
    arr.sort()
except:
    st.error("Please enter a valid list of numbers.")
    st.stop()

# Run binary search and visualize steps
if st.button("Run Binary Search"):
    steps = binary_search_steps(arr, target_input)
    for low, mid, high in steps:
        plot_step(arr, low, mid, high)
        time.sleep(1)  # Pause for a second between steps
