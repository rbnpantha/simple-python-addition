from lambda_function import lambda_handler

def test_addition_valid_input():
    event = {"num1": 5, "num2": 7}
    response = lambda_handler(event)
    assert response["statusCode"] == 200
    assert "The sum is 12" in response["body"]

def test_missing_num1():
    event = {"num2": 7}
    response = lambda_handler(event)
    assert response["statusCode"] == 400
    assert "must be provided" in response["body"]

def test_missing_num2():
    event = {"num1": 5}
    response = lambda_handler(event)
    assert response["statusCode"] == 400
    assert "must be provided" in response["body"]

def test_both_missing():
    event = {}
    response = lambda_handler(event)
    assert response["statusCode"] == 400
    assert "must be provided" in response["body"]

def test_non_numeric_num1():
    event = {"num1": "abc", "num2": 10}
    response = lambda_handler(event)
    assert response["statusCode"] == 400
    assert "must be numeric" in response["body"]

def test_non_numeric_num2():
    event = {"num1": 10, "num2": [1, 2, 3]}
    response = lambda_handler(event)
    assert response["statusCode"] == 400
    assert "must be numeric" in response["body"]
