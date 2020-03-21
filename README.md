# cs105-prj-phase3-mvb

Phase 1 and phase 2 README's can be found within the phase 1 and phase 2 folders.
Phase1 README: https://github.com/CS-UCR/cs105-prj-phase1-mvb/blob/master/Phase1/README.md
Phase2 README: https://github.com/CS-UCR/cs105-prj-phase2-mvb/blob/master/README.md

Bhagpreet's phase 3 consists of multiple linear regression models. The code has no dependencies other than the MSE's calculated will change slightly but are never far from each other from each run. The data that was used is coaching stats that was scraped, integrated, and EDA was performed on the data. The first linear regression model that was developed was to see what the best coefficients were for determing the number of playoff wins a team would get for their season. The coefficient that did the best was win_percent_squared. This is the win percent from the regular season, which is squared to normalize the data since it was found that this feature was skewed left in phase 2. The next model using the best features ran 5 fold cross validation to determine the consistency of the model's predictions. The MSE was low for the model, and the same cross validation is used on later models to test performances. The later models are specific to a single coach, and determines that coaches number of playoff wins for the given season. The model's seemed to do well in their performances, since they have small margins of error compared to the values that are being predicted. I found that regular season stats help determine how the playoffs can go in the given season, which reflects how much the regular season can matter for when the season transitions to the playoffs.

Mitchell's phase 3 is found in the notebook labeled, successful_teams.ipynb. In this notebook, you will find data analysis which predicts the teams that are most likely to win the NBA finals. This phase uses datasets from previous phases which were scraped/downloaded then cleaned, and even created from other datasets. The data consists of stats from previous championship teams and current (2019-2020) NBA teams. There were two linear regression models created to make the prediction of which teams are most likely to win this season's championship. The first model, a flawed model, trained the dataframe, df_train, based on past championship teams stats. The df_test dataframe made flawed predictions as it did not have a similar order to the current standings. The second model was created by taking the differential stats of championship teams and runner-up teams. Then the df_train data frame trained specific stat differentials that proved to be important in winning teams. ex: turnover difference, rebounding difference, etc... The test dataframe utlized current team stats and their opposition stats to follow the model created to train the train dataframe. This prediction was much more accurate and formed an order very similar to the order of standings, but not exact, which is what is expected. Because this phase is in a .ipynb file, code can be run through jupyter notebook with datasets in folder, phase3_dataset.
