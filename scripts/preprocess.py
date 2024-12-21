import pandas as pd

def load_data(raw_file_path, product_file_path):
    # Load the data files
    raw_data = pd.read_csv(raw_file_path, encoding='utf-8-sig')
    product_data = pd.read_csv(product_file_path, encoding='utf-8-sig')
    
    return raw_data, product_data

def clean_raw_data(raw_data):
    # Rename columns for clarity
    raw_data.columns = ['nowtime', 'current_price', 'old_price', 'price_per_unit', 'other', 'product_id']
    
    # Convert 'nowtime' to datetime and handle errors
    raw_data['nowtime'] = pd.to_datetime(raw_data['nowtime'], errors='coerce')
    
    # Convert prices to numeric, coerce errors to NaN
    raw_data['current_price'] = pd.to_numeric(raw_data['current_price'], errors='coerce')
    raw_data['old_price'] = pd.to_numeric(raw_data['old_price'], errors='coerce').fillna(0)  # Fill missing old prices with 0
    
    # Handle price_per_unit by extracting numeric values (removing non-numeric characters)
    raw_data['price_per_unit'] = raw_data['price_per_unit'].replace(r'[$,]', '', regex=True).str.extract('(\d+\.?\d*)')[0].astype(float)

    # Trim whitespace in all string columns
    for col in raw_data.select_dtypes(include='object').columns:
       raw_data[col] = raw_data[col].str.strip()
    
    # Extract date from 'nowtime' to address multiple entries for the same day
    raw_data['date'] = raw_data['nowtime'].dt.date
    raw_data = raw_data.drop_duplicates(subset=['product_id', 'date'], keep='first')
    raw_data.drop(columns=['date'], inplace=True)  # Drop temporary 'date' column
    
    # Validate prices to ensure they are non-negative
    raw_data = raw_data[(raw_data['current_price'] >= 0) & (raw_data['old_price'] >= 0)]
    
    return raw_data

def clean_product_data(product_data):
    # Rename columns for clarity
    product_data.columns = ['id', 'concatted', 'vendor', 'product_name', 'units', 'brand', 'detail_url', 'sku', 'upc']
    
    # Convert 'id' to numeric
    product_data['id'] = pd.to_numeric(product_data['id'], errors='coerce')
    
    # Trim whitespace in all string columns
    for col in product_data.select_dtypes(include='object').columns:
        product_data[col] = product_data[col].str.strip()

    return product_data

def merge_data(raw_data, product_data):
    # Merge the two datasets on product_id and id
    merged_data = pd.merge(raw_data, product_data, left_on='product_id', right_on='id', how='left')
    
    # Drop rows with missing product names (invalid products)
    merged_data = merged_data[~merged_data['product_name'].isnull()]
    
    # Drop any duplicate columns resulting from the merge
    merged_data.drop(columns=['id'], inplace=True)
    
    # Deduplicate merged data if necessary
    merged_data.drop_duplicates(inplace=True)
    
    return merged_data

def save_cleaned_data(cleaned_data, output_file_path):
    # Save the cleaned and merged data to a new CSV file
    cleaned_data.to_csv(output_file_path, index=False, encoding='utf-8-sig')

def main():
    raw_file_path = '../data/hammer-4-raw.csv'
    product_file_path = '../data/hammer-4-product.csv'
    output_file_path = '../data/cleaned_merged_data.csv'
    
    # Load data
    raw_data, product_data = load_data(raw_file_path, product_file_path)
    
    # Clean data
    clean_raw = clean_raw_data(raw_data)
    clean_product = clean_product_data(product_data)
    
    # Merge datasets
    merged_data = merge_data(clean_raw, clean_product)
    
    # Save cleaned data
    save_cleaned_data(merged_data, output_file_path)
    print(f"Data preprocessing complete. Cleaned data saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()