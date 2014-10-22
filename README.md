awsclpy
=======

Chain AWSCLI commands. Just run the commands you would normally run in the command
line in Python in order to get access to variables, logs, and a better and easier
way of automating your AWSCLI tasks.

Here's an example where we create an ENI (Elastic Network Interface) and spin up
a new EC2 (Elastic Cloud Computing) instance with it, then create an ELB (Elastic
Load Balancer) and attach the EC2 instance to it.

**Warning: executing the example below will literally create resources in your AWS
account if you have a working AWSCLI.**

```python
from awsclpy import AWSCLPy

aws = AWSCLPy(profile = None,
              quiet = False,
              logging = False,
              logdir = './logs',
              dry_run = False)

my_eni = aws.ec2('create-network-interface',
                 '--description', 'My Eni',
                 '--subnet-id', 'subnet-xxxxxxxx',
                 '--groups', ['sg-aaaaaaaa', 'sg-bbbbbbbb', 'sg-cccccccc'])


my_ec2 = aws.ec2('run-instances',
                 '--image-id', 'ami-xxxxxxxx',
                 '--key-name', 'my-key-name',
                 '--instance-type', 'm3.medium',
                 '--network-interfaces', '''{
                                                "NetworkInterfaceId": "%s",
                                                "DeviceIndex": 0,
                                                "DeleteOnTermination": false
                                            }''' % my_eni['NetworkInterface']['NetworkInterfaceId'])

my_elb_name = 'my-elb'

my_elb = aws.elb('create-load-balancer',
                 '--load-balancer-name', my_elb_name,
                 '--listeners', [
                     'Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80',
                 ],
                 '--security-groups', ['sg-dddddddd', 'sg-eeeeeeee'],
                 '--subnets', 'subnet-yyyyyyy')

successful = aws.elb('register-instances-with-load-balancer',
                     '--load-balancer-name', my_elb_name,
                     '--instances', my_ec2['Instances'][0]['InstanceId'])

if successful:
    print 'Now, that was awesome!'
```

Tradiotionally you would need to run the commands, write down the output values
you were interested in, then pass those values to the next commands... manually.
Yikes!
