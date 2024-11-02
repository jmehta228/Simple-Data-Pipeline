import requests
import mysql.connector

def getAPIResponse(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    api_data = response.json()
    return api_data


def getAPIInfo(api_data):
    api_info_list = []
    api_info_list.append(api_data["location"]["localtime"])
    api_info_list.append(api_data["location"]["name"])
    api_info_list.append(api_data["location"]["region"])
    api_info_list.append(api_data["location"]["country"])
    api_info_list.append(api_data["current"]["temp_f"])
    api_info_list.append(api_data["current"]["condition"]["text"])
    api_info_list.append(api_data["current"]["wind_mph"])
    return api_info_list


def transferToDatabase(api_info_list: list):
    weather_data_connection = mysql.connector.connect (
        host = "...",
        user = "...",
        password = "...",
        database = "WeatherData"
    )

    database_cursor = weather_data_connection.cursor()
    sql_insert_statement = "insert into Weather_Info (`localtime`, `name`, `region`, `country`, `temp_f`, `condition`, `wind_mph`) values (%s, %s, %s, %s, %s, %s, %s)"
    sql_insert_values = (api_info_list[0], api_info_list[1], api_info_list[2], api_info_list[3], api_info_list[4], api_info_list[5], api_info_list[6])

    try:
        database_cursor.execute(sql_insert_statement, sql_insert_values)
        weather_data_connection.commit()
        print(database_cursor.rowcount, " record(s) inserted")
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        weather_data_connection.rollback()
    finally:
        database_cursor.close()
        weather_data_connection.close()


def main():
    base_url = "http://api.weatherapi.com/v1/current.json?key="
    api_key = open("api-key.txt", "r").read()
    city_input = input("Enter name of city or zipcode: ")
    api_url = base_url + api_key + "&q=" + city_input + "&aqi=no"

    list = getAPIInfo(getAPIResponse(api_url))

    for i in range(len(list)):
        print(list[i])
    
    transferToDatabase(list)


if __name__ == "__main__":
    main()