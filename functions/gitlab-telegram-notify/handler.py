import os
import requests

def handle(event, context):
    try:
        data = event.body
        message = "GitLab Event Notification"

        if "object_kind" in data:
            if data["object_kind"] == "push":
                user = data["user_username"]
                project = data["project"]["name"]
                message = f"[Push] {user} pushed to {project}."

            elif data["object_kind"] == "merge_request":
                user = data["user"]["username"]
                title = data["object_attributes"]["title"]
                message = f"[Merge Request] {user} created MR: {title}."

            elif data["object_kind"] == "issue":
                user = data["user"]["username"]
                title = data["object_attributes"]["title"]
                message = f"[Issue] {user} opened: {title}."

        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        telegram_url = f"https://api.telegram.org/bot{{API}}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        requests.post(telegram_url, json=payload)

        return {"statusCode": 200, "body": {"status": "Message sent"}}
    except Exception as e:
        return {"statusCode": 500, "body": {"error": str(e)}}
