cities = {
    'Toronto': {'temperature': 25, 'population': 1000000},
    'Calgary': {'temperature': 30, 'population': 5},
    'Montreal': {'temperature': 40, 'population': 6}
}

for k, v in cities.items():
    print("\nIn " + k + ", ", end="")
    print("The temperature is " + str(v['temperature']))
    print("The population is " + str(v['population']))