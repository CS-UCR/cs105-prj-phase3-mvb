# cs105-prj-phase3-mvb

Phase 1 and phase 2 README's can be found within the phase 1 and phase 2 folders.

Bhagpreet's phase 3 consists of multiple linear regression models. The code has no dependencies other than the MSE's calculated will change slightly but are never far from each other from each run. The data that was used is coaching stats that was scraped, integrated, and EDA was performed on the data. The first linear regression model that was developed was to see what the best coefficients were for determing the number of playoff wins a team would get for their season. The coefficient that did the best was win_percent_squared. This is the win percent from the regular season, which is squared to normalize the data since it was found that this feature was skewed left in phase 2. The next model using the best features ran 5 fold cross validation to determine the consistency of the model's predictions. The MSE was low for the model, and the same cross validation is used on later models to test performances. The later models are specific to a single coach, and determines that coaches number of playoff wins for the given season. The model's seemed to do well in their performances, since they have small margins of error compared to the values that are being predicted. I found that regular season stats help determine how the playoffs can go in the given season, which reflects how much the regular season can matter for when the season transitions to the playoffs.
