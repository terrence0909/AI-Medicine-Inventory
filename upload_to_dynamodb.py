import boto3
from datetime import datetime

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MedicineStock')

# Sample data
medicine_stock = [
    {"medicine_name": "Paracetamol", "location": "Hospital A", "stock_level": 100},
    {"medicine_name": "Ibuprofen", "location": "Pharmacy B", "stock_level": 200},
    {"medicine_name": "Insulin", "location": "Clinic C", "stock_level": 50}
]

# Insert data into DynamoDB
for item in medicine_stock:
    item["last_updated"] = str(datetime.now())  # Add timestamp
    table.put_item(Item=item)
    print(f"✅ Added {item['medicine_name']} to {item['location']}")

print("✅ All data inserted successfully!")
