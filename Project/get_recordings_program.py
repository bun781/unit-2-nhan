import requests

import time

from bmp280 import BMP280
from smbus2 import SMBus

# set up bmp280 connection with raspberri pi
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

# function get temp & humidity from bmp
def bmp280_get_data(bmp280):
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()

    dict_ = {
        'Temperature': temperature,
        'Pressure': pressure
    }
    return dict_

# class for http requests
class http:
    # initiate variable for the instance
    def __init__(self, server_ip:str, username:str, password:str, sensor_location:str, bmp280):
        self.server_ip = server_ip
        self.username = username
        self.password = password
        self.sensor_location = sensor_location
        self.bmp280 = bmp280

        self.access_token = ""

        self.sensor_id_temperature = 0
        self.sensor_id_humidity = 0
        self.sensor_id_pressure = 0

    # method to register user
    def register(self):
        user = {"username": f'{self.username}', 'password': f'{self.password}'}
        r = requests.post(f"http://{self.server_ip}/register", json = user)
        return r.json()

    # method to get token
    def get_token(self):
        user = {"username": f'{self.username}', 'password': f'{self.password}'}
        r = requests.post(f"http://{self.server_ip}/login", json=user)

        self.access_token = r.json()["access token"] #return token for access

        return self.access_token

    #method to create new sensor and get id
    def create_new_sensor_all_type(self):
        auth = {"Authorization": f"Bearer {self.access_token}"}

        temperature_sensor = {"type": "Temperature", "location": f"{self.sensor_location}", "name": f"Temperature {self.sensor_location}", "unit": "C"}
        temperature_r = requests.post(f'http://{self.server_ip}/sensor/new', json=temperature_sensor, headers=auth)
        self.sensor_id_temperature = temperature_r.json()['id'] # update the instance's variable

        # humidity_sensor = {"type": "Humidity", "location": f"{self.sensor_location}", "name": f"Humidity {self.sensor_location}", "unit": "C"}
        # humidity_r = requests.post(f'http://{self.server_ip}/sensor/new', json=temperature_sensor, headers=auth)
        # self.sensor_id_humidity = humidity_r.json()['id']

        pressure_sensor = {"type": "Pressure", "location": f"{self.sensor_location}", "name": f"Pressure {self.sensor_location}", "unit": "C"}
        pressure_r = requests.post(f'http://{self.server_ip}/sensor/new', json=temperature_sensor, headers=auth)
        self.sensor_id_pressure = pressure_r.json()['id'] # update the instance's variable

        return f'Temperature sensor ID is {self.sensor_id_temperature}, Humidity sensor id is {self.sensor_id_humidity}, Pressure sensor id is{self.sensor_id_pressure}'

    #method to update temperature
    def update_all_censor(self):
        auth = {"Authorization": f"Bearer {self.access_token}"}

        sensor_data = bmp280_get_data(bmp280) #get the sensor data from get data function

        temperature_data = {'sensor_id': self.sensor_id_temperature, 'value': sensor_data['Temperature']}
        temperature_r = requests.post(f'http://{self.server_ip}/reading/new', json=temperature_data, headers=auth)

        pressure_data = {'sensor_id': self.sensor_id_pressure, 'value': sensor_data['Pressure']}
        humidity_r = requests.post(f'http://{self.server_ip}/reading/new', json=pressure_data, headers=auth)

        return f'The temperature data sent was {temperature_r.json()}\n The humidity data sent was {humidity_r.json()}'

    def get_readings(self):
        auth = auth = {"Authorization": f"Bearer {self.access_token}"}
        r = requests.post(f'http://{self.server_ip}/user/readings', headers=auth)
        readings = r.json()
        return readings

#~~~~~~~~~~~~~~

server = http(server_ip='192.168.4.137', username=input("What is the username you want to choose"), password=input("What is the password that you want to use?"), sensor_location=input("Where are the censors located at?"), bmp280=bmp280)
server.register()
server.get_token()
server.create_new_sensor_all_type()

time_elapsed = 0
time_since_last_token_refresh = 0

while time_elapsed < 86400: #3600*24 seconds
    if time_since_last_token_refresh > 9000: #60*10 seconds, every 10 minutes, cuze the auth token expires in 10 minutes iirc
        server.get_token()
        time_since_last_token_refresh = 0

    server.update_all_censor()

    time.sleep(60)

    time_elapsed += 60
    time_since_last_token_refresh += 60

server.get_readings()
