import unittest


class TestAWSCLPy(unittest.TestCase):
    def setUp(self):
        from awsclpy import AWSCLPy
        self.aws = AWSCLPy()

    def test_service_command(self):
        self.aws.service_command
