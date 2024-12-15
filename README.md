# Heritage Housing Project

This is a basic, goal-driven Machine Learning Project to predict sale prices of houses in Ames, Iowa.

* Click [here]("""""""""""""""""""""""""") to see live project.

## Business Case

* The client has supplied a dataset with house sale prices and other property attributes in order to accomplish prediction of sale prices. We aim to determine the best selling price for these residences as well as examine the ways in which particular property attributes affect their market worth.
* Business Requirements section has more details about what we are aiming.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

* Hypothesis 1: We suspect properties with greater Overall Quality will be priced higher.

* Hypothesis 2: We suspect properties with larger spaces will be priced higher.

* Hypothesis 3: We suspect the more recent the year of construction, the higher the sale price tends to be.


**Validation**

 - 1. The first hypothesis argument is supported by the fact of correlation analysis that homes with greater Overall Quality typically have higher sale prices.
 - 2. The correlation study between SalePrice and space variables supports this.
 - 3. The correlation study between SalePrice and YearBuilt supports this.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1:

- Study on the datasets and prepare a solid Pearson & Spearman Correlation report.

- Visualize the correlation relation between SalePrice and others

- Observe positive and negative correlated variables with SalePrice

- Pick the highest correlated variables to use for more.

### Business Requirement 2:

- Create and deliver a ML model which is able to predict the sale price of the four inherited houses and any house in Ames, Iowa.

- Conventional Machine Learning to map the relationships between the features and the target. This will be Involving:

- Test and choose machine learning techniques to find the model that works best for project's requirements and our needs.

## Dashboard Design

### Summary 🏠

- This page contains summarized information about the project, the client's requirements and explanation of variables.

- "checkbox" to show all variables

### Hypothesis 📝

- This page contains 3 hypothesis that we suspect and validate for the project in "success" box.

### Correlation Analysis 📊

- This page has visualization of correlation study which is Pearson and Spearman and list showing positive and negative correlated variables.

- "table" to display dataset's head() function.

- "images" to show studied correlation graphs.


### House Price Prediction 💰

- This page contains estimated sale price of 4 houses that is required and interactive section to estimate any other house.

- "cards" to display 4 houses' attributes and estimated sale prices.

- "input widgets" to provide variables

- "button" to predict


### Machine Learning Model 🤖

- This page contains chosen pipeline's information, feature importance plot and model performance metrics

- "table" to show model performance petrics and comparison

- "image" to show graph of actual vs predicted values analysis

- "graph" to display feature importance analysis

## Epics and Issues

- Click [here](https://github.com/users/aksurcos/projects/4) to see Kanban Board.

### Epics
- Epic 1: Data Collection & Information Gathering
- Epic 2: Data Inspection, Cleaning, and Preparation
- Epic 3: Model Training, Optimization and Validation
- Epic 4: Plan and Creation of Dashboard
- Epic 5: Deployment

#### Issues

##### Issue in Data Collection & Information Gathering
- Info and Data Collection

##### Issues in Data Inspection, Cleaning, and Preparation
- Data Inspection and Cleaning
- Correlation Study and Visualization 

##### Issues in Model Training, Optimization and Validation
- Feature Engineering
- Train Machine Learning Model
- Optimize and Validate Model

##### Issues in Plan and Creation of Dashboard
- Plan and Creation of Dashboard
- Develop and Test Dashboard 

##### Issues in Deployment
- Deployment

## Unfixed Bugs

* Not detected any.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

   - Pandas
   - Matplotlib for plots
   - Seaborn for correlation study
   - Feature Engine for imputation and encoders    
   - Scikit-learn for ML Algorithms and Pipeline    

## Credits

* Code Institute's Churnometer Walkthrough Project 
* Custom Codes from LMS

## Acknowledgements

* This was the hardest project that I've done, I felt like there are too many details to be considered, I believe it was because this project is my first data analysis project so that I've kept it little bit basic. Thank you who has understanding.
* Thank you to all Code Institute students, especially to Slack Community.
* I believe, it would be fair if I say that I needed to see some of old projects, thank you to all Predictive Analytics students.

