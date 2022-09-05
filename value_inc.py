import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

data.info()

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SellingPricePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SellingPricePerTransaction'] - data['CostPerTransaction']

data['MarkUpPerTransaction'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

round(data['MarkUpPerTransaction'], 2)

data['MarkUpPerTransaction'] = round(data['MarkUpPerTransaction'], 2)

data['Day'].astype(str)

data.info()

Day = data['Day'].astype(str)
Year = data['Year'].astype(str)

print(Day.dtype)

data.info()

my_date = 'Day'+'-'+'Month'+'-'+'Year'

my_date = Day+'-'+data['Month']+'-'+Year

data['Date'] = my_date

data.iloc[5]

split_col = data['ClientKeywords'].str.split(',' , expand=True)

data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['LengthOfContract'] = split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[', '')

data['ItemDescription'] = data['ItemDescription'].str.lower()

data1 = pd.read_csv('value_inc_seasons.csv')

data1 = pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on = 'Month')

data = data.drop('ClientKeywords' , axis = 1)

data = data.drop('Season_x' , axis = 1)

data = data.drop('Day' , axis = 1)

data = data.drop(['Month', 'Year'] , axis = 1)

data.to_csv('valueInc.csv', index = False)
