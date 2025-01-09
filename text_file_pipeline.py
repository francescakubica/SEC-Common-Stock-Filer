from openai import OpenAI
import pandas as pd
import datetime as dt
import streamlit as st


''' 
# Refine the prompt 
def refine_prompt(user_input):
    try:
        response = client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages = [
                {"role": "system", "content": "You are an expert at refining prompts specifically for finding transactions in a Schedule 13D file. Usually found at the bottom of the file."},
                {"role": "user", "content": f"Please refine this query to find all transactions in the Schedule 13D file, only respond with the refined prompt, no other comments: {user_input}"}
            ],
            timeout=20
        )
        print(f"API Response: {response}") # To Debug
        refined_prompt = response.choices[0].message.content.strip() # Get the new prompt
        return refined_prompt
    
    except Exception as e:
        print(f"Error refining prompt: {e}")
        return None
'''

# Function to parse through the transactions content
def search_transactions(text_string_list, transactionsDF, refined_prompt, client):
  
    # Current approach: Ask for chatgpt to make a new dataframe with th
    
    # Loop that calls each list of files seperately 
    for text_string in text_string_list:
        try:
            messages = [
                    {"role": "system", "content": "You are an expert in finding transactions in Schedule13D Filings"},
                    {
                        "role": "user",
                        "content": (
                            f"The user's refined query is: '{refined_prompt}'."
                            f"Here is the file: '{text_string}'"
                            "Please identify and return ALL the transactions most relevant to the user's query at the bottom of the file. "
                            "Return the results as a JSON array of objects, with each object containing EXACTLY the following 6 columns: "
                            "\"No_Trades\", \"Trade_Date\", \"Shares\", \"Purchase\", \"Sale\", and \"Price\". "
                            "The No_Trades will be 1 if no trades are found, 0 if trades found. If No_Trades = 1, put NaN for all columns except No_Trades, and stop. The Purchase and Sale Column will be a 1 or 0 depending if the transaction is a Purchase or Sale. "
                            "Do not include any extra fields, explanations, comments, code blocks, or any text outside of the JSON array. "
                            "Make sure the JSON is syntactically valid and properly formatted."
                        )
                    }
                ]


            response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, timeout=20)
            raw_output = response.choices[0].message.content # Don'thave to strip 
            # Debug
            print("Raw Output from Model 2:", raw_output)  # Debugging log

            # Strip Markdown code block delimiters if present
            if raw_output.startswith("```") and raw_output.endswith("```"):
                raw_output = raw_output.strip("```").strip("json").strip()

            # Clean up common issues with raw JSON-like output
            raw_output = raw_output.replace("\n", "").replace("\t", "").strip()

            import json
            try:
                parsed_output = json.loads(raw_output) # Load the input from API call 
                print("Parsed JSON Output:", parsed_output)

                # Append the new transactions to the existing dataframe
                new_df = pd.DataFrame(parsed_output)

                # Transform the Trade_Date column to be in a standard format if it exists
                if new_df['Trade_Date'].notna().all(): # Check all values are not NaN
                    new_df['Trade_Date'] = pd.to_datetime(new_df['Trade_Date'])
                    new_df['Trade_Date'] = new_df['Trade_Date'].dt.strftime('%m/%d/%Y')

                # Debug
                print('New Dataframe Parsed:', new_df.head())

                # Update the transactionsDF (Combined)
                transactionsDF.append_transactions(new_df)

            except json.JSONDecodeError as e:
                print(f"Error: Raw output is not valid JSON. {e}")
                print("Raw Output (Debug):", repr(raw_output))  # Log raw output for debugging
                
        
        except Exception as e:
            print('Error searching transactions', e)
            # Do not update the transactionsDF if there is an error
    
    # Right now, if it hits an error then it stops. I dont want it to do that 

