import pandas as pd
pd.set_option("display.max_columns", None)
from apyori import apriori

if __name__ == "__main__":
    # 讀取資料
    dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None) # header = None 表示沒有標題列

    # 將資料轉換成 由許多清單(list)所組成的清單(list)，即轉換成不規則陣列 [][]
    transactions = []
    for i in range(0, dataset.shape[0]):
        transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])
        
    rules = apriori(transactions, 
                    min_support = 0.003, # 至少要有 0.003的支持度
                    min_confidence = 0.2, # 至少要有0.2的信賴度
                    min_lift = 3, # 增益至少要有3
                    min_length = 2)
    df_results = pd.DataFrame(list(rules)) # 將法則轉換成DataFrame物件，以利進行挑選
    df_results = df_results.sort_values(by=['support'], ascending=False) # Sort Descending
    print(df_results.head(5))
