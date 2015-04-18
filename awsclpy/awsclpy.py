#!/usr/bin/env python

from subprocess import Popen, PIPE
from datetime import datetime
from _utils import log, flatten
import json
import os

class AWSCLPy(object):
    def __init__(self, **kwargs):
        super(AWSCLPy, self).__init__()
        self.profile = kwargs.get('profile', None)
        self.access_key_id = kwargs.get('access_key_id', None)
        self.secret_access_key = kwargs.get('secret_access_key', None)
        self.default_region = kwargs.get('default_region', None)
        self.quiet = kwargs.get('quiet', False)
        self.logging = kwargs.get('logging', False)
        self.logdir = kwargs.get('logdir', './logs')
        self.dry_run = kwargs.get('dry_run', False)

    def service_command(self, command, subcommand, *parameters):
        parameters = flatten(parameters)
        args = ['aws', '--output', 'json']

        if self.profile:
            args.extend(['--profile', self.profile])
        else:
            if self.access_key_id and self.secret_access_key:
                os.environ["AWS_ACCESS_KEY_ID"] = self.access_key_id
                os.environ["AWS_SECRET_ACCESS_KEY"] = self.secret_access_key

        if self.default_region:
            os.environ["AWS_DEFAULT_REGION"] = self.default_region

        args.extend([command, subcommand])
        args.extend(parameters)

        if self.quiet == False:
            label = ('Dry-' if self.dry_run else '') + 'Running ';
            print(label + ' '.join(args))

        if self.dry_run:
            return None

        try:
            request_datetime = datetime.now()
            process = Popen(args, stdout=PIPE)
            out, err = process.communicate()
            response_datetime = datetime.now()

            if self.logging:
                log(' '.join(args), request_datetime, self.logdir)
                log(out, response_datetime, self.logdir)

            if process.returncode == 0 and out:
                return json.loads(out)

            return process.returncode == 0
        except Exception as e:
            print(e)

        return None

    def autoscaling(self, subcommand, *parameters):
        return self.service_command('autoscaling', subcommand, *parameters)

    def cloudformation(self, subcommand, *parameters):
        return self.service_command('cloudformation', subcommand, *parameters)

    def cloudsearch(self, subcommand, *parameters):
        return self.service_command('cloudsearch', subcommand, *parameters)

    def cloudsearchdomain(self, subcommand, *parameters):
        return self.service_command('cloudsearchdomain', subcommand, *parameters)

    def cloudtrail(self, subcommand, *parameters):
        return self.service_command('cloudtrail', subcommand, *parameters)

    def cloudwatch(self, subcommand, *parameters):
        return self.service_command('cloudwatch', subcommand, *parameters)

    def cognito_identity(self, subcommand, *parameters):
        return self.service_command('cognito-identity', subcommand, *parameters)

    def cognito_sync(self, subcommand, *parameters):
        return self.service_command('cognito-sync', subcommand, *parameters)

    def configure(self, subcommand, *parameters):
        return self.service_command('configure', subcommand, *parameters)

    def datapipeline(self, subcommand, *parameters):
        return self.service_command('datapipeline', subcommand, *parameters)

    def directconnect(self, subcommand, *parameters):
        return self.service_command('directconnect', subcommand, *parameters)

    def dynamodb(self, subcommand, *parameters):
        return self.service_command('dynamodb', subcommand, *parameters)

    def ec2(self, subcommand, *parameters):
        return self.service_command('ec2', subcommand, *parameters)

    def elasticache(self, subcommand, *parameters):
        return self.service_command('elasticache', subcommand, *parameters)

    def elasticbeanstalk(self, subcommand, *parameters):
        return self.service_command('elasticbeanstalk', subcommand, *parameters)

    def elastictranscoder(self, subcommand, *parameters):
        return self.service_command('elastictranscoder', subcommand, *parameters)

    def elb(self, subcommand, *parameters):
        return self.service_command('elb', subcommand, *parameters)

    def emr(self, subcommand, *parameters):
        return self.service_command('emr', subcommand, *parameters)

    def iam(self, subcommand, *parameters):
        return self.service_command('iam', subcommand, *parameters)

    def importexport(self, subcommand, *parameters):
        return self.service_command('importexport', subcommand, *parameters)

    def kinesis(self, subcommand, *parameters):
        return self.service_command('kinesis', subcommand, *parameters)

    def logs(self, subcommand, *parameters):
        return self.service_command('logs', subcommand, *parameters)

    def opsworks(self, subcommand, *parameters):
        return self.service_command('opsworks', subcommand, *parameters)

    def rds(self, subcommand, *parameters):
        return self.service_command('rds', subcommand, *parameters)

    def redshift(self, subcommand, *parameters):
        return self.service_command('redshift', subcommand, *parameters)

    def route53(self, subcommand, *parameters):
        return self.service_command('route53', subcommand, *parameters)

    def route53domains(self, subcommand, *parameters):
        return self.service_command('route53domains', subcommand, *parameters)

    def s3(self, subcommand, *parameters):
        return self.service_command('s3', subcommand, *parameters)

    def s3api(self, subcommand, *parameters):
        return self.service_command('s3api', subcommand, *parameters)

    def ses(self, subcommand, *parameters):
        return self.service_command('ses', subcommand, *parameters)

    def sns(self, subcommand, *parameters):
        return self.service_command('sns', subcommand, *parameters)

    def sqs(self, subcommand, *parameters):
        return self.service_command('sqs', subcommand, *parameters)

    def storagegateway(self, subcommand, *parameters):
        return self.service_command('storagegateway', subcommand, *parameters)

    def sts(self, subcommand, *parameters):
        return self.service_command('sts', subcommand, *parameters)

    def support(self, subcommand, *parameters):
        return self.service_command('support', subcommand, *parameters)

    def swf(self, subcommand, *parameters):
        return self.service_command('swf', subcommand, *parameters)
