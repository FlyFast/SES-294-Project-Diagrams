import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

print("*****************************************************************************************")
print("This program reads in data from the Mamajek Brown Dwarf Data Excel file and plots the data")
# Print the current working directory to the console
print("The current working directory is: " + os.getcwd())
# Print the current date and time to the console
print("The current date and time is: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("*****************************************************************************************")
print("")

# *****************************************************************************************
# Section 1
# Plot Teff vs logL
# *****************************************************************************************

# Switch to the directory where the data is stored
os.chdir('c:\\Users\\Keith\Desktop\\Dev\\SES 294 H-R Diagrams')

# Read the data into a Pandas DataFrame ensuring that numeric data is treated as float()
# Use the first row as the column names
# Only read the Teff, Peak Wavelength, logL, and Mv columns
mamajek = pd.read_excel('Brown Dwarf Data.xlsx', sheet_name='data', header=0, usecols='B, C, D, F, I, Z')

# Print the mamajek DataFrame to the console
print("Mamajek:")
print(mamajek)

# Copy the first 92 rows of the marmajek DataFrame to a new marmajek2 DataFrame
# This will only include the rows with complete Teff and logL data
# If you don't filter out the rows with missing data, the plot will not work
# because the plot function cannot handle missing data (which are strings).
marmajek1 = mamajek.iloc[0:77, 0:4]
marmajek1_1 = mamajek.iloc[78:91, 0:4]

# Convert all of the columns, except the first, to floats
marmajek1.iloc[:, :] = marmajek1.iloc[:, :].astype(float)
marmajek1_1.iloc[:, :] = marmajek1_1.iloc[:, :].astype(float)

# Print the type of each row and column to the console
# print(mamajek1.dtypes)

# Print the DataFrame to the console
#print("Mamajek1:")
#print(marmajek1)

# Set the default plot size
plt.rcParams['figure.figsize'] = [20, 12]

# Create a plot with two subplots
# plt.subplot(2,2,1)

# Plot a scatter plot of x=Teff and y=logL
plt.scatter(marmajek1['Teff'], marmajek1['logL'], marker='x', color='blue', label='Stars')
plt.scatter(marmajek1_1['Teff'], marmajek1_1['logL'], marker='+', color='brown', label='Brown Dwarfs')
# Add a legend to the plot
plt.legend(loc='upper right')
# Invert the x-axis
plt.gca().invert_xaxis()
# Label the x-axis
plt.xlabel('Teff (K)')
# Label the y-axis
plt.ylabel('logL')
# Add a title to the plot
plt.title('H-R Diagram for Brown Dwarfs')
# Display the plot
plt.show()


# *****************************************************************************************
# Section 2
# Plot J-H vs Mv
# *****************************************************************************************
# Copy the first 91 rows of the marmajek DataFrame to a new marmajek2 DataFrame
# This will only include the rows with complete Teff and Mv data
# If you don't filter out the rows with missing data, the plot will not work
# because the plot function cannot handle missing data (which are strings).
marmajek2 = mamajek.iloc[78:92, 4:6]

print("marmajek2:")
print(marmajek2)

# Convert all of the columns, except the first, to floats
marmajek2.iloc[:, :] = marmajek2.iloc[:, :].astype(float)

# Print the type of each row and column to the console
# print(marmajek2.dtypes)

# Print the DataFrame to the console
print(marmajek2)

# Create the third subplot
# plt.subplot(2,2,2)

# Plot a scatter plot of x=W1-W2 and y=Mv
plt.scatter(marmajek2['Mv'], marmajek2['W1-W2'])
# Invert the x-axis
plt.gca().invert_xaxis()
# Invert the y-axis
#plt.gca().invert_yaxis()
# Label the x-axis
plt.xlabel('W1-W2 (Color)')
# Label the y-axis
plt.ylabel('Mv')
# Add a title to the plot
plt.title('Color-Magnitude Diagram for Brown Dwarfs')

# Display the plot
plt.show()


# *****************************************************************************************
# Section 3
# Plot  Teff vs peak wavelength
# *****************************************************************************************
# Copy only the rows with complete Teff and wavelength data
# If you don't filter out the rows with missing data, the plot will not work
# because the plot function cannot handle missing data (which are strings).

# Read the data into a Pandas DataFrame ensuring that numeric data is treated as float()
# We read it in again to get the first column which contains the spectral type
# Not the most efficience code but it works
mamajek = pd.read_excel('Brown Dwarf Data.xlsx', sheet_name='data', header=0, usecols='A, B, C, D, F, I, Z')

print("marmajek:")
print(mamajek)


# Combine the values in columns 0 and 1 in the marmajek dataframe into a single column and append it to the end of the dataframe
# This will be used to label the points in the plot
mamajek['Teff-Spectral Type'] = mamajek['Spectral Type'].astype(str) + " / " + mamajek['Peak wavelength (μm)'].round(3).astype(str)

# Split the data into stars and brown dwarfs
marmajek3 = mamajek.iloc[1:78, 0:3]
marmajek3_1= mamajek.iloc[79:117, 0:3]

print("marmajek3:")
print(marmajek3)

# Convert all of the columns, except the first, to floats
marmajek3.iloc[:, 1:] = marmajek3.iloc[:, 1:].astype(float)
marmajek3_1.iloc[:, 1:] = marmajek3_1.iloc[:, 1:].astype(float)

# Do the following after converting the columns to floats
# This prevents errors when converting the columns to floats due tot he text fields
# Add the 'Teff-Spectral Type' column to the marmajek3 dataframe
marmajek3['Teff-Spectral Type'] = mamajek['Teff-Spectral Type'].iloc[1:78]
# Add the 'Teff-Spectral Type' column to the marmajek3_1 dataframe
marmajek3_1['Teff-Spectral Type'] = mamajek['Teff-Spectral Type'].iloc[79:117]

# Print the type of each row and column to the console
# print(marmajek3.dtypes)

# Print the DataFrame to the console
print(marmajek3)

# Create the third subplot
#plt.subplot(2,2,3)

# Plot a scatter plot of x=W1-W2 and y=Mv
plt.scatter(marmajek3['Teff-Spectral Type'], marmajek3['Peak wavelength (μm)'], marker='x', color='blue', label='Stars') # Stars
#plt.scatter(marmajek3_1['Teff'], marmajek3_1['Peak wavelength (μm)'], marker='+', color='brown', label='Brown Dwarfs') # Brown Dwarfs
plt.scatter(marmajek3_1['Teff-Spectral Type'], marmajek3_1['Peak wavelength (μm)'], marker='+', color='brown', label='Brown Dwarfs') # Brown Dwarfs
# Rotate the x-axis labels 90 degrees
plt.xticks(rotation=90)
# Add a legend to the plot
plt.legend(loc='upper left')
# Invert the x-axis
#plt.gca().invert_xaxis()
# Invert the y-axis
#plt.gca().invert_yaxis()
# Label the x-axis
plt.xlabel('Spectral Class / Teff (K)')
# Label the y-axis
plt.ylabel('Peak wavelength (μm)')
# Add a title to the plot
plt.title("Wien's Law Diagram for Brown Dwarfs")


# Display the plot
plt.show()
