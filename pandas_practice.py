# https://www.youtube.com/watch?v=vmEHCJofslg
import pandas as pd

# LOADING DATA INTO PANDAS
# Load CSV into Pandas, you have to put in the directory to the data in the parentheses, however if you save it in the
# same directory as the code, then you just have to write the file name)
df = pd.read_csv('pokemon_data.csv')
# Print first few rows
print(df.head(3))
# Print bottom few rows
print(df.tail(3))
# Load Excel data into pandas
df_excel = pd.read_excel('pokemon_data.xlsx')
print(df_excel.head(4))
# Load tab separated data into pandas
df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

# READING DATA INTO PANDAS
# Read Headers
print(df.columns)
# Read a specific Column
print(df['Name'])
# Read top 5 of a specific columns
print(df['Name'][0:5])
# Read specific Columns
print(df[['Name', 'Type 1', 'HP']])
# Read each Row (index 1 or second row in this example)
print(df.iloc[1])
# Read a range of rows
print(df.iloc[1:4])
# Read a specific location (R,C)
print(df.iloc[2,1])
# To iterate through each row (you can index for a specific type of data like Name or not):
for index, row in df.iterrows():
    print(index,row['Name'])
# Finding specific data in data set 'df.loc' Can use multiple conditions or just a single one
a = df.loc[df['Type 1'] == 'Fire']
print(a)

# SORTING/DESCRIBING DATA
# Statistical description of all data
print(df.describe())
# Sorting values (in this example sorting name alphabetical)
print(df.sort_values('Name'))
# To do it in reverse
print(df.sort_values('Name', ascending=False))
# Sort by type 1 and then HP
print(df.sort_values(['Type 1', 'HP']))
# To do Type 1 in reverse and HP in normal order
print(df.sort_values(['Type 1', 'HP'], ascending=[0, 1]))

# MAKING CHANGES TO DATA
# Create a column that is the total of the stats of each pokemon
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# Drop a specific column
df = df.drop(columns=['Total'])
# You can create a column in a faster way (axis=1 specifies adding horizontally)
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# Move the 'Total' column over to the left
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]
# This is the same is doing df = df['#','Type 1', 'Type 2', 'Total' 'HP' 'Attack'....]

#   SAVING OUR DATA (EXPORTING INTO DESIRED FORMAT)
# Save into a csv. Use index = false to not save the indexes with the data
df.to_csv('modified.csv', index=False)
# Save into an excel file
df.to_excel('modified.xlsx', index=False)
# Save into a tab separated file
df.to_csv('modifed.txt', index=False, sep='\t')

# FILTERING DATA
# Specifying a specific type
df.loc[df['Type 1'] == 'Grass']
# Specifying a type combination. In Python use & for 'and', | for 'or', and ~ for 'not'
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
# Not just word conditions, can also be numeric (greater than, less than, etc.)
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >= 70)]
print(new_df)
new_df.to_csv('filtered.csv')
# To reset the index from the old data frame. (drop=True stops the old index from being saved as a new column)
new_df = new_df.reset_index(drop=True)
print(new_df)
# To filter out all of the names that contain 'Mega'. Use the contains function
print(df.loc[~df['Name'].str.contains('Mega')])
# To find out if the 'Type 1' is either grass or fire. Import regular expressions (re), very good library for filtering data
import re
print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])
# In order to ignore capitalization
print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
# Find all pokemon who's name starts with pi
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

# CONDITIONAL CHANGES
# Conditionally changing data, using df.loc
# Change all Fire types in 'Type 1' to 'Flamer' df.loc[df[] == condition, Then
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
df = pd.read_csv('modified.csv')
# Use one condition to modify another condition
# Example: All Fire pokemon have legendary = True
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
print(df.head(10))
# Changing multiple parameters at the same time.
# In this example, if stat total is above 500, reset generation and legendary status to test value
df = pd.read_csv('modified.csv')
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'
# Can also modify individually
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST VALUE 1', 'Test Value 2']
print(df.head(15))

# AGGREGATE STATISTICS (GROUPBY)
df = pd.read_csv('modified.csv')
# Finding statistics based on grouping
# For example find average of each stat grouped by 'Type 1'
average_by_type = df.groupby(['Type 1']).mean()
# You can even sort the values by stats. For example Defense high to low
average_by_type = df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)
print(average_by_type)
# You can use groupby for other statistics as well, such as sum, mean, count
# Couniting all of the types. This example shows how to count all of the type 1's and then each of the type 2's in that type 1
df['count'] = 1
count_type1 = df.groupby(['Type 1', 'Type 2']).count()['count']
print(count_type1)

# WORKING WITH LARGE AMOUNTS OF DATA
# Loading in large amounts of data in smaller chunks at a time
# This loads in 5 rows at a time of the modified data set
for df in pd.read_csv('modified.csv', chunksize=5):
    print('Chunk DF')
    print(df)
# This can be helfpful when working with large sets of data because you can start creating new dataframes of
# representational data with the new chunks being loaded in.
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type1']).count()
    new_df = pd.concat([new_df, results])
