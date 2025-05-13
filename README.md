# Projeto ETL com API de Criptomoedas

Este é um projeto de pipeline ETL (Extração, Transformação e Carga) desenvolvido em Python.

## Objetivo

Coletar dados da API pública CoinGecko sobre as criptomoedas **Bitcoin** e **Ethereum**, tanto em **dólares (USD)** quanto em **reais (BRL)**, de forma programada.
- Objetivo fazer 1 coleta de dados a cada 1 segundo, mas, não foi possivel devido ao limite da API publica.
- Com isso, Foram feitas **10 coletas**, com um intervalo de **15 segundos** entre elas.
- A coleta respeita o limite da API pública para evitar bloqueios.
- Após a coleta, os dados são tratados e enviados para um bucket do Amazon S3 no formato `.csv`.

## Tecnologias utilizadas

- Python 3.11
- Pandas – para manipulação e transformação de dados
- Requests – para requisição dos dados da API de criptomoedas
- Boto3 – para integração com o Amazon S3
- Amazon S3 (AWS) – para armazenar os dados em nuvem
- Git & GitHub – para versionamento e hospedagem do código
- Power BI – para visualização gráfica dos dados

## Armazenamento

O resultado final é salvo como arquivo `.csv` no Amazon S3 no bucket:
