import requests
import os

def handle(event, context):
    try:
        data = event.body
        source_currency = data.get("source")
        target_currency = data.get("target")

        api_key = os.getenv("API_KEY")
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_currency}/{target_currency}"
        response = requests.get(url, timeout=10)
        result = response.json()

        if result.get("result") == "success":
            rate = result["conversion_rate"]
            return {
                "statusCode": 200,
                "body": {"rate": rate}
            }
        else:
            return {
                "statusCode": 400,
                "body": {"error": "Conversion failed"}
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"error": str(e)}
        }
