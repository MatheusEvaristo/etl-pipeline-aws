import requests
import boto3
import csv
from io import StringIO
from datetime import datetime
import time

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,brl"
    response = requests.get(url)
    data = response.json()
    
    if 'bitcoin' in data and 'ethereum' in data:
        btc_usd = data['bitcoin']['usd']
        btc_brl = data['bitcoin']['brl']
        eth_usd = data['ethereum']['usd']
        eth_brl = data['ethereum']['brl']
        return btc_usd, btc_brl, eth_usd, eth_brl
    else:
        print("Erro na API ou limite excedido")
        return None, None, None, None

def load_data_to_s3(data, bucket_name, file_name):
    s3 = boto3.client('s3')
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer, delimiter=';')
    
    for row in data:
        writer.writerow(row)
    
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
    print(f'Dados enviados para o S3 com o nome de arquivo: {file_name}')

def main():
    bucket_name = 'etl-pipeline-matheus'
    file_name = 'dados_transformados.csv'
    
    data = []
    
    for i in range(10):  
        btc_usd, btc_brl, eth_usd, eth_brl = get_crypto_data()
        
        if btc_usd and btc_brl and eth_usd and eth_brl:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data.append([timestamp, btc_usd, btc_brl, eth_usd, eth_brl])
            print(f'Dados coletados: {timestamp} - BTC USD: {btc_usd} - ETH USD: {eth_usd}')
        
        time.sleep(15)
    
    load_data_to_s3(data, bucket_name, file_name)

if __name__ == "__main__":
    main()