import boto3

# AWS Config (Make sure you have run `aws configure` in VS Code)
s3 = boto3.client('s3')

# Define Bucket and File Details
bucket_name = "medicine-inventory-bucket"  # Replace with your bucket name
file_name = "medicine_inventory.csv"  # Your file name
s3_key = "inventory-data/medicine_inventory.csv"  # S3 Key (folder structure)

# Upload File
s3.upload_file(file_name, bucket_name, s3_key)
print(f"✅ File {file_name} uploaded to S3 bucket: {bucket_name}/{s3_key}")

