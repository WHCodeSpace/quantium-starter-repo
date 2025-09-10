import csv
import os

# List of CSV files
files = [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv"
]

input_folder = "data"
output_file = "pink_morsel_sales.csv"

results = []

# Step 1: Loop through files and filter
for fname in files:
    file_path = os.path.join(input_folder, fname)

    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["product"].strip().lower() == "pink morsel":
                # Clean price (remove $), convert to float
                price = float(row["price"].replace("$", "").strip())
                quantity = int(row["quantity"])
                sales = price * quantity

                results.append({
                    "Sales": round(sales, 2),  # keep 2 decimal places
                    "Date": row["date"],
                    "Region": row["region"]
                })

# Step 2: Write to new CSV
if results:
    with open(output_file, "w", newline='', encoding="utf-8") as outfile:
        fieldnames = ["Sales", "Date", "Region"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

print(f"Done! Exported {len(results)} rows to {output_file}")
