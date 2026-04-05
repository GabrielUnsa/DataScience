'''
Model Evaluation

Split the data into training and testing sets
    # Randomly split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    # X: independent variables, Y: dependent variable
    # test_size: proportion of the dataset to include in the test split (0.3 = 30%)
    # random_state: controls the shuffling applied to the data before applying the split (for reproducibility)

Generalization error: the measure of how accurately an algorithm is able to predict outcome values for previously unseen data. It is used to estimate the performance of a model on new data. Viewing distribution plots of the predicted values vs the actual values can help visualize the generalization error.

Cross-Validation: A technique for assessing how the results of a statistical analysis will generalize to an independent data set. It is mainly used in settings where the goal is prediction, and one wants to estimate how accurately a predictive model will perform in practice. The most common method is k-Fold Cross-Validation.

    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LinearRegression
    import numpy as np
    lm = LinearRegression()
    scores = cross_val_score(lm, X, Y, cv=k) # where k is the number of folds, lm is the model, X is the independent /variables, Y is the dependent variable
    # cross_val_score returns an array of scores of the estimator for each run of the cross validation
    print("Cross-Validation Scores:", scores)
    # We can average the result together to estimate out-of-sample r² using the mean method
    np.mean(scores)

    
    #For more information on predictions using cross-validation
    from sklearn.model_selection import cross_val_predict
    predictions = cross_val_predict(lr2e, X, Y, cv=k) # where k is the number of folds, lr2e is the model, X is the independent variables, Y is the dependent variable

Overfitting, Underfitting and Model Selection: Podemos usar r² para saber que tipo de grado de polinomio nos conviene usar
    Rsqu_test=[]
    order = [1,2,3,4,5,6,7,8,9,10]
    for n in order:
        pr = PolynomialFeatures(degree=n)
        x_train_pr = pr.fit_transform(x_train[['horsepower']])
        x_test_pr = pr.fit_transform(x_test[['horsepower']])
        lm = LinearRegression()
        lm.fit(x_train_pr, y_train)
        Rsqu_test.append(lm.score(x_test_pr, y_test))
    plt.plot(order, Rsqu_test)

Ridge Regression: A method of estimating the coefficients of multiple-regression models in scenarios where independent variables are highly correlated. It adds a penalty equivalent to the square of the magnitude of coefficients. Prevencion de sobreajuste (overfitting).
    from sklearn.linear_model import Ridge
    ridgeModel = Ridge(alpha=cross_val) # cross_val is the regularization parameter
    ridgeModel.fit(X_train, Y_train)
    yhat_ridge = ridgeModel.predict(X_test)
    
Grid Search: A method to perform hyperparameter optimization to find the best set of parameters for a given model. It exhaustively considers all parameter combinations specified in a grid.
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import Ridge
    parameters = {'alpha': [0.1, 1.0, 10.0, 100.0], 'fit_intercept': [True, False]} #fit_intercept: whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations.
    parameters2 = {'alpha': [0.1, 1.0, 10.0, 100.0], 'normalize': [True, False]} #normalize: This parameter is ignored when fit_intercept is set to False. If True, the regressors X will be normalized before regression.
    RR = Ridge()
    grid = GridSearchCV(RR, parameters, cv=4) # cv is the number of folds
    grid.fit(X_train, Y_train)
    print("Best Parameters:", grid.best_params_)
    print("Best Estimator:", grid.best_estimator_)
    print("Best Score:", grid.best_score_)
    scores = grid.cv_results_
    scores['mean_test_score']
    
'''