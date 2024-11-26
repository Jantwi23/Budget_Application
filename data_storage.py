# Dictionary to store all expense and budget data
data = {
    "expenses": [],
    "budgets": {}
}

def save_data(data):
    """Save data to this module."""
    with open("data_storage.py", "w") as file:
        file.write(f"data = {data}")
    print("Data saved successfully!")
