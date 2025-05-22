def lambda_handler(event, context=None):
    try:
        num1 = event.get('num1')
        num2 = event.get('num2')

        if num1 is None or num2 is None:
            return {
                "statusCode": 400,
                "body": "Both 'num1' and 'num2' must be provided."
            }

        # Validate that both inputs are numeric
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return {
                "statusCode": 400,
                "body": "'num1' and 'num2' must be numeric values (int or float)."
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

    with open("test_event.json") as f:
        event = json.load(f)

    response = lambda_handler(event)
    print(json.dumps(response, indent=2))
