def lambda_handler(event, context=None):
    try:
        num1 = event.get('num1')
        num2 = event.get('num2')

        if num1 is None or num2 is None:
            return {
                "statusCode": 400,
                "body": "Both 'num1' and 'num2' must be provided."
            }

        result = num1 + num2
        return {
            "statusCode": 200,
            "body": f"The sum is {result}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }

# Run locally
if __name__ == "__main__":
    import json

    # Read test event from file
    with open("test_event.json") as f:
        event = json.load(f)

    response = lambda_handler(event)
    print(json.dumps(response, indent=2))
