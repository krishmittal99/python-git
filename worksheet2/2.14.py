# 14. Sensor readings
sensor_data = {1:2.3, 2:4.5, 3:1.8, 4:3.6}
high_sensors = [k for k,v in sensor_data.items() if v > 3.0]
print(high_sensors)
