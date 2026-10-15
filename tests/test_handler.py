import json
import unittest

from app.handler import lambda_handler


class TestLambdaHandler(unittest.TestCase):

    def make_event(self, operation="add", a="10", b="5"):
        return {
            "queryStringParameters": {
                "operation": operation,
                "a": a,
                "b": b
            }
        }

    def test_addition_request(self):
        response = lambda_handler(self.make_event(), None)

        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(body["result"], 15)

    def test_multiplication_request(self):
        response = lambda_handler(
            self.make_event("multiply", "6", "7"), None
        )

        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(body["result"], 42)

    def test_invalid_operation(self):
        response = lambda_handler(
            self.make_event("divide", "10", "2"), None
        )

        self.assertEqual(response["statusCode"], 400)

    def test_missing_parameters(self):
        response = lambda_handler(
            {"queryStringParameters": {"operation": "add"}}, None
        )

        self.assertEqual(response["statusCode"], 400)


if __name__ == "__main__":
    unittest.main()