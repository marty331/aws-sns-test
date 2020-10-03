import json

import pytest

from unittest import TestCase
from mock import patch

from awssns.messages import Message


class MockClient:
    client_type = "sns"

    def publish(self, TopicArn, Message, MessageStructure):
        if TopicArn is None:
            raise ClientError(
                operation_name="test", error_response={"error": "test error"}
            )
        return dict(MessageId="Test123", ResponseMetadata=dict(HTTPStatusCode=200))


class MessageTest(TestCase):
    def setUp(self) -> None:
        sns_client_patch = patch("boto3.client")

        self.addCleanup(sns_client_patch.stop)

        self.sns_client = sns_client_patch.start()

    def test_message(self):
        self.sns_client.return_value = MockClient()
        message = Message(payload="Test Message")
        message_ran = message.route()
        assert route_ran["ResponseMetadata"]["HTTPStatusCode"] == 200
