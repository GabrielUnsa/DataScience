import pandas as pd

# URL de CSV free https://www.datablist.com/learn/csv/download-sample-csv-files/customers-100.csv

url = "https://drive.google.com/uc?id=1zO8ekHWx9U7mrbx_0Hoxxu6od7uxJqWw&export=download"

df = pd.read_csv(url) #Load iris dataframe  
#df_no_headers = pd.read_csv(url, header=None) #Load dataframe without headers

'''
df prints the entire dataframe
df.head(n) - prints the first n rows of the dataframe
df.tail(n) - prints the last n rows of the dataframe
df.columns = headers - assigns new column headers to the dataframe where headers is a list of strings
df = pd.read_json() - read the dataframe to a json object
df = pd.read_excel() - read the dataframe to an excel object
df = pd.read_sql() - read the dataframe to a sql database
'''
print(df.dtypes)  #Prints the data types of each column
print("*"*40)
print(df.describe())  #Prints statistical summary of numerical columns
print("$"*40)
print(df.describe(include="all"))  #Prints statistical summary of all columns
# unique: is the number of distinct  in the column
# top: is the most frequent value in the column
# freq: is the frequency of the most frequent value in the column
print(df.info())  #Prints concise summary of the dataframe (first 30 rows and bottom 30 rows of the dataframe)



### Data Acquisition Lab ###
#Drive Link:

