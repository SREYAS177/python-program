# Name        : Sreyas Suresh
# Roll Number : 55
# Class       : MCA
import json
import pandas as pd

# Sample JSON weather dataset
weather_json = """
{
    "cities": [
        {
            "location": {"city": "Kochi", "country": "India"},
            "weather": {"temperature": 30, "humidity": 75}
        },
        {
            "location": {"city": "Delhi", "country": "India"},
            "weather": {"temperature": 35, "humidity": 60}
        },
        {
            "location": {"city": "Mumbai", "country": "India"},
            "weather": {"temperature": 32, "humidity": 70}
        }
    ]
}
"""

# Parse JSON data
data = json.loads(weather_json)

# Extract nested JSON data
records = []

for city_data in data["cities"]:
    record = {
        "City": city_data["location"]["city"],
        "Country": city_data["location"]["country"],
        "Temperature": city_data["weather"]["temperature"],
        "Humidity": city_data["weather"]["humidity"]
    }
    records.append(record)

# Convert into a table
df = pd.DataFrame(records)

print("Weather Information:")
print(df.to_string(index=False))

# Display summarized reports
print("\nAverage Temperature:",
      df["Temperature"].mean())

print("Average Humidity:",
      df["Humidity"].mean())

print("\nWeather Report for Each City:")
for index, row in df.iterrows():
    print(row["City"], "-",
          row["Temperature"], "°C,",
          row["Humidity"], "% humidity")
