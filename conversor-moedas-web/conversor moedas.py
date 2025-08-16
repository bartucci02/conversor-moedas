import requests

def obter_taxa_cambio(moeda_origem, moeda_destino):

    api_key  = "67d37b305d06c317643cb17b"
    url = f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = response.json()

        if moeda_destino in dados["rates"]:
            return dados["rates"][moeda_destino]
        else:
            raise ValueError(f"Moeda de destino '{moeda_destino}' não encontrada.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None
    except ValueError as e:
        print(e)
        return None 

def converter_moeda(valor, moeda_origem, moeda_destino):
    taxa = obter_taxa_cambio(moeda_origem, moeda_destino)
    if taxa is not None:
        valor_convertido = valor * taxa
        return valor_convertido
    else:
        return None 

def main():
    print ("Bem vindo ao conversor de moedas!")

    moeda_origem = input("Digite a moeda de origem (ex: USD, EUR): ").upper()
    moeda_destino = input("Digite a moeda de destino (ex: BRL, JPY): ").upper() 

    try:
        valor = float(input("Digite o valor a ser convertido: "))
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
        return
    
    resultado = converter_moeda(valor, moeda_origem, moeda_destino)
    if resultado is not None:
        print(f"{valor} {moeda_origem} é igual a {resultado:.2f} {moeda_destino}.")
    else:
        print("Não foi possível realizar a conversão. Verifique as moedas e tente novamente.")

main()
