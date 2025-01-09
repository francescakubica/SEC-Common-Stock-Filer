# Main file

import pandas as pd
import text_file_pipeline
from openai import OpenAI


# Class for initalizing dataframe (of all transactions)
class TransactionsDataFrame:
    def __init__(self):
        self.df = pd.DataFrame(columns=['No_Trades','Trade_Date', 'Shares', 'Purchase', 'Sale','Price'])
    def append_transactions(self, new_df):
        self.df = pd.concat([self.df, new_df], ignore_index=True) 
        # Concationate with the new dataframe 


def is_valid_api_key(api_key):
    try:
        openai_api_key = api_key
        
        # Test the API key by making a request to the API
        client = OpenAI(api_key=openai_api_key)

        client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages = [
                {"role": "system", "content": "You are friendly."},
                {"role": "user", "content": f"Hello, I'm testing my API key."}
            ],
            timeout=10
        )

        return True
    except Exception as e:
        return False

def run_pipeline(text_string_list, client):

    # Put in the edge case if the file cannot be loaded later 
    if text_string_list == None:
        print('Failed to load text file, try another one or reupload.')
        exit() 

    # Initalize dataframe to hold the specific columns
    transactionsDF = TransactionsDataFrame() # Default constructor

    # Call the interface here
    user_input = "Give me 5 columns entitled : ['No_Trades','Trade_Date', 'Shares', 'Purchase', 'Sale','Price'] from all trades found in a table at the bottom of the file."

    # Step 1: Refine the promt
    prompt = text_file_pipeline.refine_prompt(user_input)
    if not prompt:
        # Returns none
        print(f"Error: Refined prompt is empty or invalid.")
        
    
    # Step 2: Search Transactions
    text_file_pipeline.search_transactions(text_string_list, transactionsDF, prompt, client) 

    # Double check it is combining to the original dataframe
    print('Checking transaction:', transactionsDF.df.head())
    return transactionsDF.df # Return the dataframe to frontend
