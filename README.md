# LINK TO INSTRUCTIONS ON USE:
https://www.canva.com/design/DAGb0qlASmU/TULDjcUx6GjvENKRvsaoeA/view?utm_content=DAGb0qlASmU&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h43ecb3e9d4

# WHAT IS IT?
This application was made to speed up data entry when analyzing Schedule13D text files from SEC.
Working under Professor Stice Lawrence at the University of Southern California, I was tasked to analyze
Schedule13D filing to record Common Stock transactions. On average, recording these transactions by hand takes 1 hour for 10 filings. 
With this tool, I've shortened that to 25 files in 1 hour, a 125% increase in efficiency. 
Users can use their own API_key, upload txt downloads of the files, and then it will return a downloadable csv. 

# ABOUT - FOR USERS 
This is a tool that will allow you to speed up the manual data entry process. 
I am using ChatGPT with a specific prompt, that scrapes the Schedule13D text files and creates a CSV with the transactions trade dates, shares, purchase, sale, and price. 
I have neglected the other columns to increase accuracy. This is not meant to be used in bulk, instead, to supplement your data entry. 
Please upload files one by one for the best results. Additionally, please attempt to not upload files with no transactions, it will still work, but you may get confused because it’ll return a CSV with no trades listed. 

# Deployment 
This is the first application I have deployed and used GitHub for a repository. I utilized Streamlit to build the front-end and deploy it. 
This tool is used by me and 2 other Research Assistants tasked with recording Schedule13D transactions.

# Challenges 

-> Challenges on setting up the Openai API_Key, allowing the user to utilize their own.
I have not worked with chatgpt's API key before, and had difficulty figuring out how to allow the user to input their own key,
validate it, and then store their key. 
Solution: Used streamlit session_state so that it will keep the api_key in a session. Once the user clicks the button 'Validate'
it will verify if the api key is valid (by running a demo api call) and then update the session state.

-> Passing the data frame address instead of a copy. 
I realized that if I made a copy of the 'transactions dataframe' which contains all transactions, it would slow down the process
and create unnecessary overhead. Instead of doing this, I passed the dataframe address across the functions. 

-> Understanding how to append to the pre-existing data frame of transactions.

-> Connecting the front-end to the inner workings. 
