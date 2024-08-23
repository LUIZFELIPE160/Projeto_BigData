import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Lista de produtos com marcas, modelos e preços
products = [
    {"produto": "Controle Remoto Universal", "marca": "Logitech", "modelo": "Logitech Harmony 350", "preco": 119.19},
    {"produto": "Controle Remoto para TV Samsung", "marca": "Samsung", "modelo": "BN59-01199F", "preco": 77.59},
    {"produto": "Controle Remoto LG", "marca": "LG", "modelo": "AKB75095307", "preco": 79.99},
    {"produto": "Carregador Rápido 18W", "marca": "Anker", "modelo": "PowerPort III Nano", "preco": 39.99},
    {"produto": "Carregador USB-C 20W", "marca": "Apple", "modelo": "20W USB-C Power Adapter", "preco": 97.98},
    {"produto": "Carregador Rápido Dual", "marca": "Aukey", "modelo": "PA-Y10", "preco": 44.99},
    {"produto": "Fone de Ouvido Bluetooth", "marca": "Jbl", "modelo": "Wave Flex TWS - Preto", "preco": 249.89},
    {"produto": "Fone de Ouvido Bluetooth", "marca": "Lenovo", "modelo": "Lp40", "preco": 97.99},
    {"produto": "Fone de Ouvido com Fio", "marca": "Havit", "modelo": "H2016D", "preco": 94.37},
    {"produto": "Fone de Ouvido com Fio", "marca": "Jbl", "modelo": "Tune 500 Preto", "preco": 149.98},
    {"produto": "Powerbank 10000mAh", "marca": "Anker", "modelo": "PowerCore 10000", "preco": 129.99},
    {"produto": "Powerbank 20000mAh", "marca": "Xiaomi", "modelo": "Mi Power Bank 3", "preco": 199.99},
    {"produto": "Rádio MP3 para Carro", "marca": "Pioneer", "modelo": "DEH-S6220BT", "preco": 499.99},
    {"produto": "Rádio MP3 para Carro", "marca": "Kenwood", "modelo": "KDC-BT558U", "preco": 449.99}
]

# Função para gerar dados de vendas
def generate_sales_data(num_rows, products):
    sales_data = []
    current_date = datetime(2023, 6, 1)

    while len(sales_data) < num_rows:
        num_sales_today = random.randint(1, 6)  # Vendas diárias entre 1 e 5 produtos
        for _ in range(num_sales_today):
            if len(sales_data) >= num_rows:
                break
            product = random.choice(products)
            sales_data.append({
                "data_venda": current_date.strftime("%Y-%m-%d"),
                "produto": product["produto"],
                "marca": product["marca"],
                "modelo": product["modelo"],
                "preco": f"R$ {product['preco']:.2f}",
                "quantidade": random.randint(1, 10)  # Quantidade de vendas variada entre 1 e 10
            })
        # Incrementa a data de forma cíclica entre os semestres de 2023 e 2024
        current_date += timedelta(days=1)
        if current_date > datetime(2024, 6, 30):
            current_date = datetime(2023, 1, 1)

    return sales_data

# Gerando 630 linhas de dados de vendas
sales_data = generate_sales_data(1468, products)

# Cria um DataFrame com os dados
df_sales = pd.DataFrame(sales_data)

# Ordena o DataFrame pela data de venda
df_sales = df_sales.sort_values(by="data_venda").reset_index(drop=True)

# Exporta o DataFrame para um arquivo CSV
csv_file_path = 'c:/Users/luizf/OneDrive/Desktop/Luiz/Trabalho big data/mnt/data/vendas.csv'
os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
df_sales.to_csv(csv_file_path, index=False)

csv_file_path
