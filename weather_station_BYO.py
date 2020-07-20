
import time
import math
import bme280_sensor
import wind_direction_byo
import statistics
import ds18b20_therm
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
