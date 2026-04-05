'''
Dealing with missing values

Drop missing values
    df.dropna() or df.dropna(axis=0) #drops any row with missing values (entire row is removed)
    df.dropna(axis=1) #drops any column with missing values (entire column is removed)
    df.dropna(thresh=n) #drops any row with less than n non-missing values
    df.dropna(subset=['col1', 'col2']) #drops any row with missing values in specified columns  
    df.dropna(subset=['col1', 'col2'], axis=0, inplace=True) #drops any row with missing values in specified columns and modifies the original dataframe *inplace=True is defaulted to False*

Replace missing values 
    df.replace(missing_value, new_value) #replaces missing_value with new_value
    mean = df['col1'].mean()
    df['col1'].replace(np.nan, mean) #replaces missing values in col1 with the mean of col1
    df['col1'].fillna(mean) #another way to replace missing values in col1 with the mean of col1
     
Data Fomatting
    df['col1'] = df['col1'].astype('int') #changes the data type of col1 to integer
    df['col1'] = nro / df['col1'].astype('float') #changes the data type of col1 to float (example)
    df.rename(columns={'old_name':'new_name'}, inplace=True) #renames column old_name to new_name
    df.tail(10) #displays the last 10 rows of the dataframe

Data Normalization
    Methods of normalization:
    1. Min-Max Normalization.
        df['col1'] = (df['col1'] - df['col1'].min()) / (df['col1'].max() - df['col1'].min())
    2. Z-Score Normalization.
        df['col1'] = (df['col1'] - df['col1'].mean()) / df['col1'].std()
    3. Simple Feature Scaling.
        df['col1'] = df['col1'] / df['col1'].max()

Binning
    bins = np.linspace(min_value, max_value, number_of_bins) #creates bins from min_value to max_value with number_of_bins - 1
    group_names = ['bin1', 'bin2', 'bin3', ...] #creates names for the bins
    df['binned_col'] = pd.cut(df['col1'], bins, labels=group_names, include_lowest=True) #creates a new column binned_col with the binned values of col1
    Example:
        bins = np.linspace(min(df['age']), max(df['age']), 4)
        group_names = ['Youth', 'Middle Age', 'Senior']
        df['age_binned'] = pd.cut(df['age'], bins, labels=group_names, include_lowest=True)
        
Turning Categorical Variables into Numerical Variables
    One-Hot Encoding
        df = pd.get_dummies(df, columns=['categorical_col']) #creates new columns for each category in categorical_col with binary values (0 or 1)
    Label Encoding
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        df['categorical_col'] = le.fit_transform(df['categorical_col']) #replaces categorical_col with numerical values (0, 1, 2, ...) based on the categories 
    Ordinal Encoding
        from sklearn.preprocessing import OrdinalEncoder
        oe = OrdinalEncoder(categories=[['low', 'medium', 'high']])
        df['ordinal_col'] = oe.fit_transform(df[['ordinal_col']]) #replaces ordinal_col with numerical values based on the order specified in categories
'''