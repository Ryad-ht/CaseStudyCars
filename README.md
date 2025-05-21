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

Certainly! Here’s how the project overview can be presented in English, including the data cleaning and outlier removal steps as integral parts of the analysis process.

---

## Project Overview

### Objective
To visually analyze the distribution of selling prices among used cars and examine how the average selling price varies by year of manufacture, following thorough data cleaning and preparation.

### Data Analysis Approach
The analysis follows a structured process that includes data cleaning, outlier removal, and then two primary visual analyses:
1. **Data Cleaning and Preparation:** Loading the data from a CSV file, followed by a cleaning step to address missing or inconsistent entries and normalize attributes such as the vehicle's body type.
2. **Outlier Removal:** Identifying and excluding outliers in selling prices and odometer readings to ensure the analysis reflects representative trends without being skewed by extreme data.
3. **Distribution of Selling Prices:** Using a histogram to display the frequency distribution of selling prices, providing an overview of price variability in the used car market.
4. **Average Selling Price by Year:** Creating a bar chart to depict how the average selling price varies with the year of manufacture, highlighting the impact of a vehicle's age on its resale value.

### Results
- **Cleaning and Preparation:** This initial step ensures the data analyzed are reliable and relevant, eliminating potential sources of error or bias in the subsequent analysis.
- **Outlier Removal:** This step enhances the quality of the analysis by focusing attention on the most representative data, allowing for more accurate conclusions.
- **Visualizations:** The produced charts offer clear insights into the distribution of selling prices and how the year of manufacture affects average prices, helping to decode market trends in the used car sector.

### Value of the Study
This analysis provides essential insights for sellers, buyers, and automotive industry professionals:
- **For Sellers:** Identify optimal pricing positioning by understanding the current distribution of selling prices and the effect of the year of manufacture on value.
- **For Buyers:** Recognize buying opportunities by identifying price trends and avoiding overpriced purchases.
- **For Professionals:** Adjust inventory and pricing strategies based on updated and reliable market data.

By integrating data cleaning and outlier removal as critical elements of the analysis, the project highlights the importance of rigorous data preparation for deriving accurate and actionable insights into the used car market.
