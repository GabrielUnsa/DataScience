'''
Model Development

Linear Regression: Will refer to one independent variable to make a prediction

Simple Linear Regression (SLR): A method to help us understand the relationship between two continuous variables (one independent and one dependent)
    Fitting the Model SLR
        first: we define the dependent (target) variable Y and independent (predictor) variable X
            X = df[['independent_variable']]
            Y = df['dependent_variable']
            
        second: then use lm.fit(X,Y) to fit the model, i.e. fine the parameters b0 and b1
            from sklearn.linear_model import LinearRegression
            lm = LinearRegression()
            lm.fit(X, Y)
        
        third: We can obtain a prediction
            Yhat = lm.predict(X)
        
        notes: We can view the intercept (b0) and coefficient (b1) values
            print(lm.intercept_) #b0
            print(lm.coef_)      #b1

Multiple Linear Regression (MLR): Will refer to multiple independent variables to make a prediction. One continuous target (Y) variable and multiple independent or predictor (X) variables
    Fitting the Model MLR
        first: we define the dependent (target) variable Y and independent (predictor) variables X
            X = df[['independent_variable1', 'independent_variable2', ...]]
            Y = df['dependent_variable']
            
        second: then use lm.fit(X,Y) to fit the model, i.e. fine the parameters b0, b1, b2, ...
            from sklearn.linear_model import LinearRegression
            lm = LinearRegression()
            lm.fit(X, Y)
        
        third: We can obtain a prediction
            Yhat = lm.predict(X)
        
        notes: We can view the intercept (b0) and coefficient (b1, b2, ...) values
            print(lm.intercept_) #b0
            print(lm.coef_)      #b1, b2, ...

Model Evaluation using Visualization
    Regression Plot
        import seaborn as sns
        sns.regplot(x='independent_variable', y='dependent_variable', data=df)
        plt.title("Independent Variable vs Dependent Variable")
        plt.show()
        plt.ylim(0,) #set y-axis limit to start from 0
        
    Residual Plot
        import seaborn as sns
        sns.residplot(x='independent_variable', y='dependent_variable', data=df)
        sns.residplot(df['independent_variable'], df['dependent_variable']) #alternative way
        plt.title("Residuals Plot")
        plt.show()
    
    Distribution Plot
        import seaborn as sns
        ax1 = sns.distplot(df['dependent_variable'], hist=False, color="r", label="Actual Value")
        sns.distplot(Yhat, hist=False, color="b", label="Fitted Values", ax=ax1)
        plt.title("Actual vs Fitted Values for Dependent Variable")
        plt.show()
    
Polynomial Regression and Pipelines
    Calculating Polynomial Coefficients of 3rd order
        import numpy as np
        f = np.polyfit(X['independent_variable'], Y, 3) #3rd order polynomial
        p = np.poly1d(f)
        print(p) #prints the polynomial coefficients

    Multi-dimensional Polynomial linear regression
        #Preprocessing library create a polynomial features object
            from sklearn.preprocessing import PolynomialFeatures
        #Then we transform the feactures into a polynomial feature with the "fit_transform" method
            pr = PolynomialFeatures(degree=2, include_bias=False) #2nd order polynomial
        
        Example:
        pr = PolynomialFeatures(degree=2)
        print(pr)
        pr.fit_transform(X[['independent_variable1', 'independent_variable2']], include_bias=False)
        print(pr)
        
        Pre-processing
            We can Normalize the each feature simultaneously
            from sklearn.preprocessing import StandardScaler
            SCALE = StandardScaler()
            SCALE.fit(x_data[['independent_variable1', 'independent_variable2']])
            x_scale = SCALE.transform(x_data[['independent_variable1', 'independent_variable2']])
        
        Pipelines: simplify the process of creating complex workflows by chaining multiple steps together into a single object
            from sklearn.preprocessing import StandardScaler
            from sklearn.preprocessing import PolynomialFeatures
            from sklearn.linear_model import LinearRegression
            from sklearn.pipeline import Pipeline
            
            #Tuple: First element the name of estimador and second element contein model constructor
                Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(degree=2)),...., ('model', LinearRegression())]
            
            #create pipeline object
            pipeline = Pipeline(Input)
            
            #fit the model
            pipeline.fit(df[['independent_variable1', 'independent_variable2']], Y)
            yhat = pipeline.predict(df[['independent_variable1', 'independent_variable2']])

Measuring for In Simple Evaluation: how good the models fit of a model
    Mean Squared Error (MSE): average of the squared errors between predicted and actual values
        from sklearn.metrics import mean_squared_error
        MSE = mean_squared_error(df['dependent_variable'], Y_predicted_simple_fit)
        print(MSE)
        # If MSE is very large, the model did not fit well to the data. If MSE is very small, the model fit well to the data.

    R-squared (R²): proportion of variance in the dependent variable that can be explained by the independent variable(s)
        Coefficient of Determination or R-squared (R²) = 1 - (SS_res / SS_tot) = 1 - (MSE of regression line / MSE of the average of the data)
        where SS_res is the sum of squares of residuals and SS_tot is the total sum of squares
        
        # Calculate R² using r2_score       
        from sklearn.metrics import r2_score
        R2 = r2_score(df['dependent_variable'], Y_predicted_simple_fit)
        print(R2)
        
        # Alternatively, we can also obtain R² using the lm.fit() method
        from sklearn.linear_model import LinearRegression
        lm = LinearRegression()
        lm.fit(X, Y)
        
        # If R² is 1, the model perfectly fits the data. If R² is 0, the model does not explain any of the variance in the dependent variable.

    Mean Absolute Error (MAE): average of the absolute errors between predicted and actual values
        from sklearn.metrics import mean_absolute_error
        MAE = mean_absolute_error(df['dependent_variable'], Y_predicted_simple_fit)
        print(MAE)       
        
    Root Mean Squared Error (RMSE): square root of the average of the squared errors between predicted and actual values
        from sklearn.metrics import mean_squared_error
        import numpy as np
        RMSE = np.sqrt(mean_squared_error(df['dependent_variable'], Y_predicted_simple_fit))
        print(RMSE)

'''