# 1.Using the List Comprehension structure, convert the names of the numeric variables in the car_crashes data to uppercase and add NUM

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

disp=['NUM_'+ i.upper() if df[i].dtype != 'object' else i.upper() for i in df.columns ]

# 2. Using the List Comprehension structure, write “FLAG” at the end of the names of the variables that do not contain “no” in their name in the car_crashes database.

disp1=[i.upper() + '_FLAG' for i in df.columns if 'no' not in i]
# 3. Using the List Comprehension structure, select the names of the variables that are DIFFERENT from the variable names given below and create a new dataframe.

og_list = ["abbrev", "no_previous"]
new_cols=[i for i in df.columns if i not in og_list]
df=df[new_cols]