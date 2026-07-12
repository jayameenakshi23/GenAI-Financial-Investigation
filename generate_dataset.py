import pandas as pd
import random

random.seed(42)

cities = [
    "Chennai",
    "Bengaluru",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Pune",
    "Kolkata",
    "Coimbatore"
]

merchants = [
    "Amazon",
    "Flipkart",
    "Swiggy",
    "Zomato",
    "Reliance",
    "Croma",
    "Myntra",
    "Petrol Pump",
    "Jewellery Store",
    "ATM Withdrawal"
]

risk_levels = ["Low", "Medium", "High"]

data = []

for i in range(1, 101):

    transaction_id = f"TXN{i:03d}"
    customer_id = f"CUST{random.randint(1001,1100)}"

    amount = random.randint(500,100000)

    merchant = random.choice(merchants)

    city = random.choice(cities)

    if amount > 70000:
        risk = random.choices(
            ["High","Medium"],
            weights=[70,30]
        )[0]

    elif amount > 30000:
        risk = random.choices(
            ["Medium","Low"],
            weights=[60,40]
        )[0]

    else:
        risk = random.choices(
            ["Low","Medium"],
            weights=[85,15]
        )[0]

    data.append([
        transaction_id,
        customer_id,
        amount,
        merchant,
        city,
        risk
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Transaction_ID",
        "Customer_ID",
        "Amount",
        "Merchant",
        "Location",
        "Risk_Flag"
    ]
)

df.to_csv("data/transaction.csv", index=False)

print("Dataset created successfully!")
print(df.head())