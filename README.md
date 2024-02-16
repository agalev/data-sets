# Datasets collection

A collection of datasets I gathered with intention of using them for data analysis.

## Apple Healthkit

I utilized Apple's Healthkit framework to extract 2 datasets. The time range for those is Jan 1, 2018 - Feb 13, 2024.

1) Recorded workouts. Sample:
```
{
   "start": "2018-03-27T04:51:15.210-0700",
   "calories": 231.119,
   "activityId": 37,
   "metadata": {
     "HKWeatherHumidity": null,
     "HKTimeZone": "America/New_York",
     "HKWeatherTemperature": null
   },
   "id": "C7186A65-3BCD-4BD2-B75D-F7EA58874C13",
   "end": "2018-03-27T05:21:05.763-0700",
   "tracked": true,
   "sourceName": "Alexander’s Apple Watch",
   "sourceId": "com.apple.health.751F3196-45F5-46E0-9A04-7107C72D35B8",
   "activityName": "Running",
   "distance": 2.7826020019522395,
   "device": "Watch3,2"
 },
 {
   "start": "2018-03-26T05:14:28.730-0700",
   "calories": 156.0479999999999,
   "activityId": 37,
   "metadata": {
     "HKWeatherHumidity": null,
     "HKTimeZone": "America/New_York",
     "HKWeatherTemperature": null
   },
   "id": "D4799A31-E630-4054-AF28-E205884808F9",
   "end": "2018-03-26T05:49:33.095-0700",
   "tracked": true,
   "sourceName": "Alexander’s Apple Watch",
   "sourceId": "com.apple.health.751F3196-45F5-46E0-9A04-7107C72D35B8",
   "activityName": "Running",
   "distance": 2.025130203127466,
   "device": "Watch3,2"
 }
```
2) Recorded Heart rate. Original sample:
```
{
    "endDate": "2017-12-31T00:00:31.541-0800",
    "id": "359C453D-B40B-481B-B3D1-75C0FC817AF7",
    "metadata": { "HKMetadataKeyHeartRateMotionContext": 1 },
    "sourceId": "com.apple.health.751F3196-45F5-46E0-9A04-7107C72D35B8",
    "sourceName": "Alexander’s Apple Watch",
    "startDate": "2017-12-31T00:00:31.541-0800",
    "value": 76
  }
```
Note: The original heartrate dataset was extremely large with over 1.2 million records and amounted to 450mb. Polars was used to drop the static and irrelevant columns and the resulting CSV contains the startDate and value. It resulted in minimizing the dataset down to 40mb.