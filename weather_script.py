import requests
import csv
from datetime import datetime
import os

API_KEY= os.getenv("OPENWEATHER_API_KEY")
CITY = "Seoul"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]

#print(f"현재 온도 : {temp}도")
#print(f"현재 습도 : {humidity}%")   
#print(f"날씨 : {description}")
timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(temp, humidity, description, timezone)

#위의 4새의 데이터를 가지는 csv파일 생성
csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]

# csv가 존재하면 ->True
# csv가 존재하지 않으면 ->False
file_exists = os.path.isfile(csv_filename)

# mode = "a" -> if not is file -> create
# if is flie -> write
with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)
    
    
    # 파일이 존재하지 않는다->header가 없다
    if not file_exists:
        writer.writerow(header)
    
    writer.writerow([timezone, temp, humidity, description])

    print("csv")
