# Simple-Data-Pipeline
Function getAPIResponse(url: str):

Takes a URL as input and makes a GET request to that URL.
Checks if the response status code is 200 (indicating success). If not, it returns None.
If the response is successful, it returns the JSON data from the API.
Function getAPIInfo(api_data):

Accepts the API data (JSON) and extracts specific weather information, including:
Local time
Location name
Region
Country
Temperature in Fahrenheit
Weather condition description
Wind speed in mph
Returns this information as a list.
Function transferToDatabase(api_info_list: list):

Establishes a connection to a MySQL database named "WeatherData".
Prepares an SQL insert statement to store the weather information.
Executes the SQL command to insert the data into the Weather_Info table.
Handles errors, rolling back the transaction in case of an error, and ensures the database connection is closed afterward.
Function main():

Constructs the base URL for the WeatherAPI using an API key stored in an external text file (api-key.txt).
Prompts the user for a city name or zipcode.
Constructs the full API URL and fetches weather data using the previously defined functions.
Calls getAPIInfo to process the response and prints the weather information.
The function to transfer the data to the database is commented out.
Execution Block:

The script runs the main() function when executed directly.
ETL Breakdown
Extract:

The Extract phase involves retrieving data from a source. In this program, the getAPIResponse(url: str) function handles this by sending a GET request to the WeatherAPI. It retrieves real-time weather data based on user input (city name or zipcode) and returns the JSON response.
Transform:

The Transform phase involves processing and converting the extracted data into a suitable format for analysis or storage. This is performed in the getAPIInfo(api_data) function, where:
The JSON data is parsed to extract relevant weather information, which is collected into a list format.
Load:

The Load phase involves writing the transformed data to a target destination, such as a database. This is managed by the transferToDatabase(api_info_list: list) function, which:
Connects to a MySQL database named "WeatherData".
Prepares and executes an SQL insert statement to store the weather information in the Weather_Info table.
Summary of ETL Flow in the Program
Extract: Data is fetched from the WeatherAPI using a user-provided location.
Transform: The raw JSON response is transformed into a structured list containing only the relevant weather details.
Load: The transformed data is then loaded into a MySQL database for storage and potential future analysis.
