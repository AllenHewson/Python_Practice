# NUMERICAL DIFFERENTIATION
import pandas as pd
import numpy as np
import math
diff_df=pd.read_csv('numerical_differentiation_data.csv')
# Create the thetaprime and rprime columns
diff_df["Thetaprime"] = ""
diff_df["rprime"] = ""
h = diff_df["t"][1] - diff_df["t"][0]
# Use the forward difference based method f'(x) = (f(x+h)-f(x))/h for the first derivatives
diff_df["Thetaprime"][0] = (diff_df.iloc[1, 1] - diff_df.iloc[0, 1])/h
diff_df["rprime"][0] = (diff_df.iloc[1, 2] - diff_df.iloc[0, 2])/h
# Use a backward difference based method f'(x) = (f(x)-f(x-h))/h for the last derivative
diff_df["Thetaprime"][5] = (diff_df.iloc[5, 1] - diff_df.iloc[4, 1])/h
diff_df["rprime"][5] = (diff_df.iloc[5, 2] - diff_df.iloc[4, 2])/h
# Use the central difference based method f'(x) = (f(x+h)-f(x-h))/2h for the other derivatives
for i, row in diff_df.loc[1:4].iterrows():
    diff_df["Thetaprime"][i] = (diff_df.iloc[i+1, 1] - diff_df.iloc[i-1, 1]) / (2*h)
    diff_df["rprime"][i] = (diff_df.iloc[i+1, 2] - diff_df.iloc[i-1, 2]) / (2*h)
# Finally create the velocity column using v = sqrt(rprime^2 + (r*thetaprime)^2)
diff_df['Velocity'] = np.sqrt(np.power(diff_df['rprime'].astype(float), 2) + np.power(diff_df['Thetaprime'].astype(float) * diff_df['r'].astype(float), 2))
print(diff_df)

## NUMERICAL INTEGRATION
int_df = pd.read_csv('numerical_integration_data.csv')
# Find the total work done by integrating force*velocity over time . To do this, the trapezoidal method will be used
# Create a Power (force*velocity) column
int_df['Power'] = int_df['Force'] * int_df['Velocity']
print(int_df)
# Use the trapezoidal method to integrate this integral = h/2[f(0) + 2f(1) + 2f(2) +...+  2f(n-1) + f(n]
h = int_df['t'][1] - int_df['t'][0]
middle_sum = 2 * int_df['Power'].loc[1:4].sum()
total_work = h/2 * (int_df['Power'][0] + middle_sum + int_df['Power'][5])
print(f"The total work is {total_work}J")
