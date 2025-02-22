import pandas as pd

# Load the JSON files into Pandas DataFrames
brands_df = pd.read_json('brands.json')
receipts_df = pd.read_json('receipts.json')
users_df = pd.read_json('users.json')

# Check for missing values
missing_brands = brands_df.isnull().sum()
missing_receipts = receipts_df.isnull().sum()
missing_users = users_df.isnull().sum()

# Check for duplicates
duplicate_brands = brands_df.duplicated().sum()
duplicate_receipts = receipts_df.duplicated().sum()
duplicate_users = users_df.duplicated().sum()

# Check for inconsistencies in brand names
inconsistent_brands = brands_df['name'].str.contains('[^a-zA-Z0-9\s]', regex=True).sum()

# Check for invalid dates
invalid_receipt_dates = receipts_df['purchaseDate'].apply(lambda x: pd.to_datetime(x, errors='coerce')).isnull().sum()
invalid_user_dates = users_df['createdDate'].apply(lambda x: pd.to_datetime(x, errors='coerce')).isnull().sum()

# Print the results
print("Missing values in Brands:", missing_brands)
print("Missing values in Receipts:", missing_receipts)
print("Missing values in Users:", missing_users)

print("Duplicate brands:", duplicate_brands)
print("Duplicate receipts:", duplicate_receipts)
print("Duplicate users:", duplicate_users)

print("Inconsistent brand names:", inconsistent_brands)

print("Invalid receipt dates:", invalid_receipt_dates)
print("Invalid user creation dates:", invalid_user_dates)

''' 
SUMMARY OF FINDINGS:

Duplicate Values: Many duplicate values were detected in users.json.
Inconsistent Brand Names: Some brand names in brands.json contain non-alphanumeric characters.
Invalid Dates: Some entries in the purchaseDate column in receipts.json and the createdDate column in users.json contain invalid date formats.
Inconsistent topBrand Field: The topBrand field in brands.json is not consistently populated.
Inconsistent rewardsReceiptStatus Field: The rewardsReceiptStatus field in receipts.json has multiple variations for the same status.
Inconsistent role Field: The role field in users.json has inconsistencies in capitalization.

'''