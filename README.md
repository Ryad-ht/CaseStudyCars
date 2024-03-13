# Used Car Prices Analysis

## Project Overview
This project aims to explore and analyze used car sales data to identify key factors influencing the selling prices of used cars. Through exploratory data analysis (EDA) and regression analysis, we seek to uncover trends and relationships within the data that can provide insights for sellers, buyers, and dealerships.

## Features
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Regression Analysis to predict car selling prices

## Getting Started

### Prerequisites
Ensure you have Python 3.x installed on your system. This project also requires the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

### Installation
1. **Clone the repository:**
```bash
git clone https://yourrepositorylink.git
cd your-project-directory
```

2. **Set up a Python virtual environment (optional but recommended):**
```bash
python -m venv venv
```

- On Windows, activate the virtual environment:
```bash
.\venv\Scripts\activate
```

- On macOS and Linux, activate the virtual environment:
```bash
source venv/bin/activate
```

3. **Install the required packages:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Usage
To run the analysis, navigate to the project directory and execute the main Python script:

```bash
python main.py
```

Replace `main.py` with the actual name of your script. This will perform the data cleaning, EDA, and regression analysis, outputting the results to your terminal or saving them as files, depending on how you've set up your script.

## Acknowledgments
- Data provided from Kaggle https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data


////////////////////////////////////////////////////////////////////////////////////////////////////////////


## Project Details

### Objective
To identify key factors that significantly influence the selling price of used cars and uncover underlying market trends.

### Hypotheses
- **Year of Manufacture:** Newer cars typically sell at higher prices.
- **Make and Model:** Certain makes and models are more desirable, fetching higher prices.
- **Odometer Reading:** Lower mileage cars tend to sell for more.
- **Condition:** Cars in better condition command higher prices.
- **Color:** Popular colors may affect selling prices.
- **Seasonality:** Seasonal trends could influence car prices and demand.

### Data Analysis Steps
1. **Data Cleaning:** Address missing or inconsistent entries, focusing on crucial columns like year, odometer, condition, and selling price.
2. **Exploratory Data Analysis (EDA):** Visualize selling price distributions by year, make, model, etc., to detect patterns.
3. **Feature Engineering:** Develop new features, such as car age, to deepen the analysis of how car attributes relate to selling price.
4. **Statistical Analysis:** Apply regression models to assess the influence of various factors on selling prices.
5. **Trend Analysis:** Examine sale date data for seasonal trends.

### Expected Outcomes
- Key factors significantly impacting used car selling prices.
- Insights into preferences for certain car attributes (e.g., color, make, model) within the market.
- Any seasonal trends affecting prices.

### Value of the Study
- **For Sellers:** Insights on positive price factors can enhance market positioning.
- **For Buyers:** The study guides on optimal buying times and types for value maximization.
- **For Dealerships:** Market trend knowledge supports inventory and pricing strategies.
