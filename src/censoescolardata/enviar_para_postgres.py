
import os
import pandas as pd
from sqlalchemy import create_engine

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_atual, "..", "..", "censo_escolar_2025.json")

pg_engine = create_engine("postgresql+psycopg://postgres:postgres@127.0.0.1:5433/dados_censo")
print(f"🔄 Lendo o arquivo '{caminho_json}'...")

try:
    df = pd.read_json(caminho_json)

    df.columns = [col.lower() for col in df.columns]

    total_registros = len(df)
    print(f"📊 Encontrados {total_registros} registros. Enviando para o PostgreSQL...")

    df.to_sql("instituicoes_ensino", pg_engine, if_exists="append", index=False)

    print(f"✅ Carga concluída com sucesso! {total_registros} registros inseridos na tabela instituicoes_ensino.")

except Exception as e:
    print(f"❌ Erro durante a importação do JSON: {e}")