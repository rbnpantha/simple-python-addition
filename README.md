# 🧮 Simple Lambda Addition (Python)

This is a basic AWS Lambda-style function written in Python that adds two numbers. 
It's designed to simulate how AWS Lambda works, and can be **run locally without any AWS services, Docker, or external dependencies**.

---

## 📌 What It Does

The `lambda_handler` function takes an event dictionary (like a typical AWS Lambda event payload) containing two numbers:

```json
{
  "num1": 10,
  "num2": 25
}
```

It returns the sum of the two numbers in a response object:

```json
{
  "statusCode": 200,
  "body": "The sum is 35"
}
```

---

## 🛠️ How It Works

- The core logic resides in `lambda_function.py`.
- It expects a JSON-like dictionary containing `num1` and `num2`.
- The function is structured like a real AWS Lambda function using:

  ```python
  def lambda_handler(event, context=None):
  ```

- To simulate real-world invocation, a sample input file (`test_event.json`) is read and passed into the handler function.
- The result is printed to the console.

---

## 🚀 How to Run It Locally

### ✅ Prerequisites
- Python 3 installed (macOS comes with it by default)
- A terminal or command line

### 📁 Folder Structure

```
simple_lambda_addition/
├── lambda_function.py     # Main lambda function code
└── test_event.json        # Sample input for local testing
```

### ▶️ Steps to Run

1. Open Terminal and navigate to the folder:

   ```bash
   cd path/to/simple_lambda_addition
   ```

2. Run the lambda function:

   ```bash
   python3 lambda_function.py
   ```

3. You’ll see output like:

   ```json
   {
     "statusCode": 200,
     "body": "The sum is 35"
   }
   ```

---

## ✏️ Example Input (`test_event.json`)

```json
{
  "num1": 10,
  "num2": 25
}
```

You can change `num1` and `num2` to any integers and re-run the script.

---

## 🔍 lambda_function.py (Code)

```python
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

    with open("test_event.json") as f:
        event = json.load(f)

    response = lambda_handler(event)
    print(json.dumps(response, indent=2))
```

---

## 💡 Next Steps

You can extend this tiny project by:
- Adding input validation to ensure the values are numeric
- Wrapping it in an API using Flask or FastAPI
- Deploying to AWS Lambda using the AWS SAM CLI
- Writing unit tests using `pytest`

---

## 📃 License

This project is open-source and free to use for learning and experimentation.
