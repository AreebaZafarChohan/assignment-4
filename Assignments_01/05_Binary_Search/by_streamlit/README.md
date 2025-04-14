# 🔍 Binary Search Visualizer

A Streamlit application that visually demonstrates how the binary search algorithm works step by step using interactive bar charts.

![Binary Search Visualization](https://assignment-4-46cql5ndtntvxdz2ra6y5j.streamlit.app/)

## ✨ Features

- Visual representation of binary search algorithm
- Color-coded pointers (low, mid, high)
- Step-by-step animation
- Customizable input array
- Interactive web interface

---

## 🎮 How to Use
Enter a sorted list of comma-separated numbers (e.g., "1,3,5,7,9,11,13,15")

Enter the target number you want to search for

Click "Run Binary Search" button

Watch the algorithm work step by step

## 🎨 Color Coding

| Color | Represents | Description |
|-------|------------|-------------|
| 🟩 Green | Low pointer | Left boundary of current search space |
| 🟦 Blue | Mid pointer | Current element being checked |
| 🟥 Red | High pointer | Right boundary of current search space |
| ⬜ Gray | Other elements | Elements not in current search space |

## 📝 Algorithm Explanation
Binary search works by:

Starting with the entire sorted array

Repeatedly dividing the search interval in half

Comparing the middle element with the target value

Narrowing down the search space based on the comparison

Continuing until the element is found or the interval is empty

## 📊 Example
For array [1, 3, 5, 7, 9, 11, 13, 15] searching for 7:

First checks middle element (7) - found!

If searching for 8:

Checks 7 (too small)

Checks 11 (too big)

Checks 9 (too big)

Determines 8 doesn't exist

---

Developed with ❤️ by **Areeba Zafar**