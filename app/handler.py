import json

from app.calculator import add, subtract, multiply


OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
}


def lambda_handler(event, context):
    """Handle calculator requests from API Gateway."""
    try:
        params = event.get("queryStringParameters") or {}

        operation = params.get("operation")
        a = params.get("a")
        b = params.get("b")

        if operation not in OPERATIONS:
            raise ValueError(
                "Operation must be add, subtract, or multiply."
            )

        if a is None or b is None:
            raise ValueError("Both a and b parameters are required.")

        try:
            a = int(a)
            b = int(b)
        except (TypeError, ValueError):
            raise ValueError("Both a and b must be positive integers.")

        result = OPERATIONS[operation](a, b)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "operation": operation,
                "a": a,
                "b": b,
                "result": result
            })
        }

    except (ValueError, TypeError) as exc:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"error": str(exc)})
        }