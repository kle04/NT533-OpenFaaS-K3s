import requests
import os

def handle(event, context):
    try:
        data = event.body
        symbol = data.get("symbol")

        api_key = os.getenv("API_KEY")
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={{API}}"
        response = requests.get(url)
        result = response.json()
        stock_data = result.get("Global Quote", {})

        return {
            "statusCode": 200,
            "body": {
                "symbol": stock_data.get("01. symbol"),
                "price": stock_data.get("05. price"),
                "change": stock_data.get("10. change percent")
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"error": str(e)}
        }
