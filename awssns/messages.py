import os
import json
import logging

from typing import Dict, Any
from abc import ABC

import boto3

from botocore.exceptions import ClientError

from awssns.cfg import CFG

logger = logging.getLogger()


class AbstractRoute(ABC):
    def __init__(self, payload) -> None:
        self.payload = payload


class Message(AbstractRoute):
    def route(self) -> Dict[str, Any]:
        sns_client = self.get_sns_client()
        response = self.publish_sns_message(
            sns_client=sns_client, topic_arn=CFG.TOPIC_ARN_KEY, message=self.payload
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return response
        return {"ResponseMetadata": {"HTTPStatusCode": 500}}

    def get_sns_client(self) -> boto3.client:
        return boto3.client("sns", region_name=CFG.AWS_REGION)

    def publish_sns_message(
        self, sns_client: boto3.client, topic_arn: str, message: Dict[str, Any]
    ) -> Dict[str, Any]:
        try:
            response = sns_client.publish(
                TopicArn=topic_arn,
                Message=json.dumps(
                    {"default": message}
                ),  # json.dumps is required by FxA
                MessageStructure="json",
            )
            return response
        except ClientError as e:
            logger.error("SNS error", error=e)
            raise e
