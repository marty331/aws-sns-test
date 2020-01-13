from decouple import AutoConfig


class AutoConfigPlus(AutoConfig):
    @property
    def AWS_REGION(self):
        return self("AWS_REGION", "us-west-2")

    @property
    def TOPIC_ARN_KEY(self):
        return self("TOPIC_ARN_KEY", "fake_topic_arn_key")

    @property
    def AWS_ACCESS_KEY_ID(self):
        return self("AWS_ACCESS_KEY_ID", "fake_aws_access_key_id")

    @property
    def AWS_SECRET_ACCESS_KEY(self):
        return self("AWS_SECRET_ACCESS_KEY", "fake_aws_secret_access_key")


CFG = AutoConfigPlus()
