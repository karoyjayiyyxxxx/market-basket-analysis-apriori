# Market Basket Analysis with Apriori

This project implements Association Rule Learning using the Apriori algorithm in Python. It analyzes a dataset of retail transactions to discover strong relationships between items purchased together.

## 📋 Overview

Market Basket Analysis is a modeling technique based upon the theory that if you buy a certain group of items, you are more (or less) likely to buy another group of items.

Key Concepts in this Code:

* Support: How popular an itemset is (e.g., how often "Milk" appears in all transactions).
* Confidence: Likelihood that item Y is purchased when item X is purchased.
* Lift: Controls for the support (popularity) of item Y.
    * `Lift > 1`: Positive correlation (Buying X increases chance of buying Y).
    * `Lift < 1`: Negative correlation.
    * `Lift = 1`: No correlation.

## 🛠️ Dependencies

* Python 3.x
* Pandas (Data manipulation)
* Apyori (Implementation of Apriori algorithm)

## 🚀 Installation & Usage

1.  Clone the repository
    ```bash
    git clone [https://github.com/YOUR_USERNAME/market-basket-analysis-apriori.git](https://github.com/YOUR_USERNAME/market-basket-analysis-apriori.git)
    cd market-basket-analysis-apriori
    ```

2.  Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

3.  Prepare Data
    Ensure `Market_Basket_Optimisation.csv` is in the project directory. This dataset should contain transaction data without a header row.

4.  Run the Analysis
    ```bash
    python main.py
    ```

## ⚙️ Configuration

You can tweak the parameters in `main.py` to change the strictness of the rules:

```python
rules = apriori(transactions, 
                min_support = 0.003,    # Minimum popularity
                min_confidence = 0.2,   # Minimum likelihood
                min_lift = 3,           # Minimum correlation strength
                min_length = 2)         # At least 2 items in the relationship
