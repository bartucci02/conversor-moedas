import streamlit as st
import requests

def obter_taxa_cambio(moeda_origem, moeda_destino):
    api_key = 'SUA_CHAVE_API'  # Substitua pela sua chave
    url = f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if moeda_destino in data['rates']:
            return data['rates'][moeda_destino]
        else:
            st.error(f"Moeda de destino '{moeda_destino}' não encontrada.")
            return None
    except Exception as e:
        st.error(f"Erro ao acessar a API: {e}")
        return None

st.title("Conversor de Moedas")

moeda_origem = st.text_input("Moeda de Origem (ex: USD)").upper()
moeda_destino = st.text_input("Moeda de Destino (ex: BRL)").upper()
valor = st.number_input("Valor a Converter", min_value=0.0)

if st.button("Converter"):
    if moeda_origem and moeda_destino and valor > 0:
        taxa = obter_taxa_cambio(moeda_origem, moeda_destino)
        if taxa is not None:
            valor_convertido = valor * taxa
            st.success(f"{valor:.2f} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}")
    else:
        st.error("Preencha todos os campos corretamente.")