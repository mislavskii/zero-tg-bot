import requests

def get_crypto_quotes():
    # URL API CoinGecko для получения котировок
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # Криптовалюты, которые нас интересуют
    # Названия должны соответствовать идентификаторам криптовалют на CoinGecko
    cryptos = ["bitcoin", "ethereum", "tether", "binancecoin", "ripple"]
    
    # Валюта, к которой мы хотим получить котировки
    currency = "usd"
    
    # Параметры запроса
    params = {
        "ids": ",".join(cryptos),  # Список криптовалют через запятую
        "vs_currencies": currency  # Валюта котировки
    }
    
    try:
        # Выполняем запрос к API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Проверяем на наличие ошибок
        
        # Получаем JSON-ответ
        data = response.json()
        
        # Преобразуем данные в словарь {валюта: котировка}
        quotes = {crypto: data[crypto][currency] for crypto in cryptos if crypto in data}
        return quotes
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return {}

# Пример использования
if __name__ == "__main__":
    quotes = get_crypto_quotes()
    print("Актуальные котировки криптовалют:")
    for crypto, price in quotes.items():
        print(f"{crypto.capitalize()}: {price} USD")