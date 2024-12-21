# **Competition Analysis in Canadian Grocery Prices**

## **Overview**
This project aims to analyze historical grocery price data to uncover pricing trends, competition dynamics, and pricing irregularities within Canada's grocery sector. Using advanced data preprocessing, statistical analysis, and machine learning techniques, the project delivers actionable insights and recommendations to stakeholders.

---

## **Objective**
- Analyze grocery pricing trends and dynamics across vendors in Canada.
- Identify patterns, including seasonal trends and potential collusion.
- Provide actionable insights and recommendations for improving competition.

---

## **Directory Structure**

```plaintext
📂 project_root
├── 📂 data
│   ├── hammer-4-product.csv      # Metadata and product details (e.g., product name, brand).
│   ├── hammer-4-raw.csv          # Time-series price data (e.g., timestamps, current/sale prices).
│   ├── cleaned_merged_data.csv   # Preprocessed dataset with additional features.
│   ├── milk.csv                  # Preprocessed dataset with only milk products
│
├── 📂 notebooks
│   ├── cheapest_vendor.ipynb        # Analysis identifying the vendor with the lowest prices.
│   ├── price_change_cluster.ipynb   # Clustering analysis based on price changes over time.
│   ├── pricing_strategies.ipynb     # Insights and recommendations for effective pricing strategies.
│   ├── pricing_trends_milk.ipynb    # Analysis of pricing trends specifically for milk products.
│   ├── sandwich_pricing.ipynb       # Examination of pricing strategies and trends for sandwiches.
|
├── 📂 reports
│   ├── report.pdf  # Detailed findings and recommendations.
│
├── 📂 scripts
│   ├── preprocess.py    # Data cleaning and feature engineering script.
│
├── README.md            # Project documentation (this file).
├── requirements.txt     # Required Python packages and versions.
```

---

## **Files and Purpose**

### **Data Files**
- **`product.csv`**: Contains metadata for products, such as name, brand, and units.
- **`raw.csv`**: Time-series price data, including timestamps, current prices, and sale prices.
- **`cleaned_merged_data.csv`**: Preprocessed dataset with additional features for analysis.

### **Notebooks**
- **`cheapest_vendor.ipynb`**: Identify the vendor offering the lowest prices across categories.  
- **`price_change_cluster.ipynb`**: Perform clustering analysis to group vendors based on price change behaviors.  
- **`pricing_strategies.ipynb`**: Derive insights and recommendations for optimal pricing strategies.  
- **`pricing_trends_milk.ipynb`**: Analyze pricing trends specifically for milk products to uncover key patterns.  
- **`sandwich_pricing.ipynb`**: Investigate pricing strategies and trends for sandwiches to enhance competitive positioning.  

### **Scripts**
- **`preprocess.py`**: Automates data cleaning and feature engineering.

### **Reports and Visuals**
- **`report.pdf`**: Comprehensive report summarizing findings and recommendations.

---

## **Key Deliverables**

1. **Cleaned Dataset**:
-cleaned_merged.csv
-milk.csv
2. **Comprehensive Report**:
report.pdf
---

## **Key Analyses**

1. **Pricing Trends**
-- pricing_strategies.ipynb
-- pricing_trends_milk.ipynb
-- sandwich_pricing.ipynb

2. **Vendor Comparison**
-- cheapest_vendor.ipynb
-- price_change_cluster.ipynb

**Known Issues Resolved**

- **Duplicate Price Entries**: Resolved by deduplicating based on product IDs and consolidating prices for entries that appeared multiple times on the same day.
- **Inconsistent Vendor Names**: Standardization of vendor names ensures consistency across the dataset.
- **Missing Data Handling**: Implemented strategies for handling missing values and ensuring that important columns (like product names) are not empty.
- **Data Type Inconsistencies**: Ensured all numeric values are properly converted and validated to prevent analysis errors.


## **Reporting and Visualization**
- **Generate visualizations using `matplotlib`, `seaborn`, and `plotly`.**
- **Create a report.**

---

## **Tools and Libraries**

| **Category**          | **Tool/Library**       | **Purpose**                                  |
|------------------------|------------------------|----------------------------------------------|
| Data Handling          | `pandas`, `numpy`     | Cleaning, preprocessing, and analysis.       |
| Visualization          | `matplotlib`, `seaborn`, `plotly` | Creating static and interactive dashboards. |
| Statistical Analysis   | `scipy`, `statsmodels`| Seasonal decomposition, hypothesis testing.  |
| Machine Learning       | `sklearn`, `TensorFlow` | Clustering, anomaly detection, forecasting. |

---

## **Setup and Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/chitranshmotwani/GroceryDataAnalysis.git
cd GroceryDataAnalysis
```

### **2. Install Required Packages**
```bash
pip install -r requirements.txt
```

### **3. Download Required Data Files**
1. Download the zip file containing the data from the following link: [Download Hammer Data](https://jacobfilipp.com/hammerdata/hammer-5-csv.zip).
2. Extract the contents of the zip file.
3. Place the `hammer-4-raw.csv` and `hammer-4-product.csv` files into the `data` folder within your cloned repository.

### **4. Run Preprocessing Script**
```bash
python scripts/preprocess.py
```
This will generate the `cleaned_merged_data.csv` file, which is required for the subsequent analysis.

### **5. Run Scripts**
After preprocessing, you can run the analysis files in the `notebooks` folder as needed.

