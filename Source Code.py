import pandas as pd
import matplotlib.pyplot as plt
# from ydata_profiling import ProfileReport

# data = pd.read_csv("marketing_campaign.csv", encoding='ISO-8859-1')
#
# profile = ProfileReport(data, title="Profiling Report")
# profile.to_file("marketing_campaign.html")

data = pd.read_csv("marketing_campaign.csv", delimiter=';')
print(data.info())

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the box plots for all columns
data.boxplot(ax=ax)

plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')

# Show the plot
plt.tight_layout()

# Show the plot
plt.show()

# Plot the distribution of a column to visualize the outliers
plt.boxplot(data['Income'])
plt.show()

# Dropping non relevant Features
data = data.drop(["ID", "Z_Revenue", "Z_CostContact", "Dt_Customer", "Year_Birth"], axis=1)

# Calculate the IQR for the Income column
Q1 = data['Income'].quantile(0.25)
Q3 = data['Income'].quantile(0.75)
IQR = Q3 - Q1

# Identify the outliers in the Income column
outliers = data[(data['Income'] < (Q1 - 1.5 * IQR)) | (data['Income'] > (Q3 + 1.5 * IQR))]

# Print the number of outliers
# print("Number of outliers in the Income column:", len(outliers))
# Remove the outliers in the Income column
data = data[~((data['Income'] < (Q1 - 1.5 * IQR)) | (data['Income'] > (Q3 + 1.5 * IQR)))]

# Drop missing value
data = data.dropna()

# Check for duplicates
duplicates = data.duplicated()
print("Duplicate rows:")
print(duplicates)

# Count the number of duplicate rows
num_duplicates = duplicates.sum()
print(f"Number of duplicate rows: {num_duplicates}")

# Display duplicate rows
duplicate_rows = data[duplicates]
print("Duplicate rows data:")
print(duplicate_rows)
# Remove duplicated value
data = data.drop_duplicates()

# Classify variables
cate_col = []
num_col = []
for col in data.columns:
    if data[col].dtype == 'object' or data[col].nunique() <= 4:
        cate_col.append(col)
    else:
        num_col.append(col)
print("cate_col:" , cate_col)
print("num_col:" , num_col)
# Encode
# scaler = StandardScaler()
# for i in range(len(num_col)):
#     data[[num_col[i]]] = scaler.fit_transform(data[[num_col[i]]])
#
# # ordinal_encoder = OrdinalEncoder()
# # education_values = ['Basic', '2nd Cycle', 'Graduation', 'Master', 'PhD']
# # marital_values = ['Single', 'Alone', 'Together', 'Married', 'Divorced', 'Widow', 'YOLO', 'Absurd']
#
# data["Education"] = OrdinalEncoder().fit_transform(data[["Education"]])
# data["Marital_Status"] = OrdinalEncoder().fit_transform(data[["Marital_Status"]])
#
# encode = OneHotEncoder()
# for i in range(2, len(cate_col) - 1):
#     data[[cate_col[i]]] = encode.fit_transform(data[[cate_col[i]]])

# Export
data.to_csv('Marketing_Campain_final.csv', index=False)

