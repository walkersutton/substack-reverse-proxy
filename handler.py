import json
import requests


def posts(event, context):
    profile_user_id = event["queryStringParameters"]["profile_user_id"]
    offset = event["queryStringParameters"]["offset"]
    limit = event["queryStringParameters"]["limit"]

    # TODO probably don't need all of these in request
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://substack.com/@walkersutton",
        "sec-ch-ua": '"Chromium";v="127", "Not)A;Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    }

    params = {
        "profile_user_id": profile_user_id,
        "offset": offset,
        "limit": limit,
    }

    try:
        response = requests.get(
            "https://substack.com/api/v1/profile/posts", headers=headers, params=params
        )
        response.raise_for_status()
        data = response.json()

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(data),
        }

    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps({"message": "Error fetching posts", "error": str(e)}),
        }
