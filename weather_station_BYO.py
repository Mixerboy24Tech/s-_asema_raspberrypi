from gpiozero import Button
import time
import math
import bme280_sensor
import wind_direction_byo
import statistics
import database


wind_count = 0
radius_cm = 9.0
wind_interval = 5
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600
ADJUSTMENT = 1.18
BUCKET_SIZE = 0.2
rain_count = 
gust = 0
store_speed = []
store_directions = []



def spin():
        global wind_count
        wind_count = wind_count + 1

def calculate_speed(time_sec):
        global wind_count
        circumference_cm = (2 * math.pi) * radius_cm
        rotations = wind_count / 2.0

        dist_km = circumference_cm * rotations / CM_IN_A_KM

        km_per_sec = dist_km / time_sec
        km_per_hour = km_per_sec * SECS_IN_AN_HOUR

        final_speed =  km_per_hour * ADJUSTMENT

        return final_speed

def bucket_tipped():
        global rain_count
        rain_count = rain_count + 1

def  reset_raindall():
        global rain_count
        rain_count = 0

def reset_wind():
        global win_count
        wind_count = 0

def reset_gust():
        global gust
        gust =0

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin
db = database.weather_database()


while True:
        start_time = time.time()
        while time.time() - start_time <= interval:
                wind_start_time = time.time()
                reset_wind()

                while time.time() - wind_start_time <= wind_interval:
                        store_directions.append(wind_direction_byo.get_value())

                final_speed = calculate_speed(wind_interval)
                store_speeds.append(final_speed)

        wind_average = wind_direction_byo.get_average(store_direction)
        wind_gust = max(store_speeds)
        wind_speed = statistics.mean(store_speeds)
        rainfall = rain_count * BUCKET_SIZE
        reset_rainfall()
        store_speeds = []
        store_directions = []
        humidity, pressure, ambient_temp = bme280_sensor.read_all()

        db.insert(ambient_temp, ground_temp, 0, pressure, humidity, wind_average, wind_speed, wind_gust, rainfall)
        print (wind_average, wind_speed, wind_gust, rainfall, humidity, pressure, ambient_temp 
