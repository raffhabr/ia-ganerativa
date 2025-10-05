import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurações
start_date = datetime(2025, 1, 1, 0, 0, 0)
end_date = start_date + timedelta(days=7)
time_interval = timedelta(minutes=15)

# Listas para armazenar os dados
data = []

current_time = start_date
sensor_id = 1

while current_time < end_date:
    hour = current_time.hour
    day_of_week = current_time.weekday()  # 0 = segunda, 6 = domingo

    # Temperatura: mais baixa à noite, mais alta de dia
    if 6 <= hour <= 18:
        temperature = np.random.normal(24, 2)  # dia
    else:
        temperature = np.random.normal(20, 2)  # noite

    # Luminosidade: zero à noite, alta no dia
    if 6 <= hour <= 18:
        luminosity = np.random.normal(500, 100)  # lux
    else:
        luminosity = 0

    # Ocupação: maior em horário comercial (8h–18h, seg–sex)
    if day_of_week < 5 and 8 <= hour <= 18:
        occupation = np.random.choice([0, 1], p=[0.3, 0.7])
    else:
        occupation = np.random.choice([0, 1], p=[0.9, 0.1])

    # Adiciona os registros (3 sensores distintos)
    data.append([current_time, f"TEMP_{sensor_id}", round(temperature, 2)])
    data.append([current_time, f"LUX_{sensor_id}", round(luminosity, 2)])
    data.append([current_time, f"OCC_{sensor_id}", occupation])

    # Avança no tempo
    current_time += time_interval

# Criar DataFrame
df = pd.DataFrame(data, columns=["timestamp", "sensor_id", "valor"])

# Salvar em CSV
df.to_csv("smart_office_data.csv", index=False, sep=";")

print("Arquivo 'smart_office_data.csv' gerado com sucesso!")
