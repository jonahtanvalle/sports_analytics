from project.pymongo_insert import get_database
import pandas as pd

dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

# Showing the collection as DataFrame
items_df = pd.DataFrame(collection_name.find())
