# Introduction
March_Madness_2021 is a project that uses machine learning and other methods to determine the best way to predict the top 10 teams of March Madness. This was created for a local competition. 

# Process
1. In March Madness.ipynb, I generated some graphs and looked at correlation to get an understanding of what factors would be the most predictive of who wins or loses.

1. In March_Madness_ML_Models.ipynb, I created around 63k different machine learning models to attempt to correctly predict how many wins a given team would have. The results from these models are saved in Results.xlsx. The top models only achieved about 58% accuracy, so I decided that another approach was needed.

1. In March_Madness_Weighted_Average.ipynb, I used a range of weights on the top 5 most heavily correlated (R2) features to create a rank for each team. I sorted based on the rank and got a score for each combination of weights. The results from these models are stored in Weighted_Results.xlsx. With the top scores just over 200, I was happy with the results.

1. The top combination that I believed would perform the best on the 2021 data was hardcoded into submission.py. This file takes the selected columns from the 2021 data, creates a rank for each team, sorts them, and outputs the top 10 teams to the console. Submission.py was submitted for my entry in the competition along with instructions on how to use it.


# Usage
### General
To run the .ipynb files, just use them as normal in Jupyter Notebook. Ensure that March Madness.xlsx is in the same directory as the notebooks.

### Instructions for submission.py
To run the submission.py file properly, you must place it in the directory that contains the March Madness.xlsx Excel file.
When run, the script will look for the 2021 sheet of March Madness.xlsx, calculate the scores based on my algorithm, then it 
will print the top 10 teams that it determines are the best.

If you have issues running the code, try installing the pandas and sklearn libraries.
To do this on Windows or Mac, open a command prompt/terminal, and type
	pip install pandas scikit-learn
This should install the required packages and allow you to run the script.
