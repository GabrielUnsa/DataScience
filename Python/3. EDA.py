'''
Explotaroty Data Analysis (EDA)

Descriptive Statistics
    First: df.describe() #provides summary statistics of numerical columns and shows distribution of data
    Second: df.value_counts() #Summarize the categorial data or groups values and have discrete values
    Example:
        drive_wheel_counts = df['drive-wheels'].value_counts()
        print(drive_wheel_counts)
        drive_wheel_counts.rename(columns={'drive-wheels':'value_counts'}, inplace=True)
        print(drive_wheel_counts)
        drive_wheel_counts.index.name = 'drive-wheels'
        print(drive_wheel_counts)
    Third: Plotting 
        df['column_name'].hist() #Histogram
        df['column_name'].plot(kind='box') #Box plot
        df.plot(kind='scatter', x='col1', y='col2') #Scatter plot
        df.plot(kind='bar', x='col1', y='col2') #Bar plot
        Example:
            Categorial Data Visualization
                MathPlot (histogram and box plot):
                    import matplotlib.pyplot as plt
                    
                    Histograma
                    df['price'].hist(bins=30)
                    plt.xlabel("Price")
                    plt.ylabel("Count")
                    plt.title("Price Distribution")
                    plt.show()
                    
                    Box Plot
                    df.boxplot(column='price')
                    plt.title("Price Box Plot")
                    plt.show()
            
                Seaborn (box plot):
                    import seaborn as sns
                    sns.boxplot(x='drive-wheels', y='price', data=df)
                    plt.title("Drive Wheels vs Price")
                    plt.show()
            
            Numerical Continuous Data Visualization
                MathPlot (scatter plot):
                    import matplotlib.pyplot as plt
                    y = df['price']
                    x = df['engine-size']
                    plt.scatter(x, y)
                    plt.xlabel("Engine Size")
                    plt.ylabel("Price")
                    plt.title("Engine Size vs Price")
                    plt.show()
                
                Seaborn (scatter plot):
                    import seaborn as sns
                    sns.scatterplot(x='engine-size', y='price', data=df)
                    plt.title("Engine Size vs Price")
                    plt.show()

Grouping Data
    df_test = df[['drive-wheels', 'body-style', 'price']] 
    df_grouped = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
    print(df_grouped)
    
    Plotting Grouped Data
        Privot Table: One variable display along the columns and the other variable displayed along the rows
            df_pivot = df_grouped.pivot(index='drive-wheels', columns='body-style')
            print(df_pivot)
        
        Heatmap: Takes a rectangular grid of data and assings a colors intensity based on the data values at the grid points
            import matplotlib.pyplot as plt
            plt.pcolor(df_pivot, cmap='RdBu') #Red and Blue color map
            plt.colorbar()
            plt.show()
            
ANOVA - Analysis of Variance
    from scipy import stats
    df_anova = df[['make', 'price']]
    grouped_anova = df_anova.groupby(['make'])
    anova_results_1 = stats.f_oneway( grouped_anova.get_group("honda")['price'], grouped_anova.get_group("subaru")['price'] )
    print(anova_results_1)
    anova_results_2 = stats.f_oneway( grouped_anova.get_group("honda")['price'], grouped_anova.get_group("jaguar")['price'], grouped_anova.get_group("jeep")['price'] )
    print(anova_results_2)
    
Correlation Analysis: Measuring the strength of the relationship between two variables (independent and dependent)
    View Method
        import seaborn as sns
        sns.regplot(x='engine-size', y='price', data=df)
        plt.ylim(0,)
        plt.show()
        
    Pearson Correlation Coefficient
        from scipy.stats import pearsonr
        pearson_coef, p_value = pearsonr(df['horsepower'], df['price'])
        print("Pearson Correlation Coefficient:", pearson_coef)
        print("P-value:", p_value)    
'''
