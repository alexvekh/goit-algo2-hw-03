# 📦 Logistics and Data Structure Performance

This repository contains two separate projects:
- The Edmonds-Karp algorithm for computing the maximum flow in a logistics network.
- A performance comparison of OOBTree and dict for storing products and executing range queries by price.

## 🧮 Project 1: Maximum Flow in a Logistics Network
- graph.py – Builds a visual representation of the graph.
- edmond_karp.py – Implements the Edmonds-Karp algorithm to find the maximum flow.
- report.pdf – Report with calculations and explanations (answers to questions).

✅ Conclusions are described in the report.pdf file.

## 📊 Project 2: OOBTree vs Dict — Range Query Comparison
- generated_items_data.csv – A generated dataset of 10,000 products.
  
  CSV format with the following columns:
    - ID — Unique product identifier.
    - Name — Product name.
    - Category — Product category.
    - Price — Product price (float).
- b-tree_vs_dict.py – Loads the CSV data and stores it in two structures:
    - OOBTree (from the BTrees.OOBTree library)
    - dict
    
    It generates 100 random price ranges and measures the execution time for comparison.

✅ Conclusion: OOBTree demonstrates higher efficiency in performing range queries due to its B-tree structure.


    Total range_query time for OOBTree: 0.000902 seconds  
    Total range_query time for Dict: 1.051120 seconds

## Requirements
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt