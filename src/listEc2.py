#!/usr/bin/python

import sys, boto3

def verifyInArg(argv):
	bool = True
	if len(sys.argv) != 2 or sys.argv[1] not in ["all", "running", "stoped"]:
		bool = False
	return bool


def listEc2(state):
	stateValue = state
	if state in ["all"]:
		stateValue = '*'

	ec2 = boto3.resource('ec2')
	instances = ec2.instances.filter(
    	Filters=[{'Name': 'instance-state-name', 'Values': [stateValue]}])
	for instance in instances:
		print('Instance State' + '\t' + 'Instance Id' + '\t' + 'Instance Type')
    	print(state + '\t' + '\t' + instance.id + '\t' +  instance.instance_type)


if __name__ == '__main__':
	bool = verifyInArg(sys.argv)
	if bool:
		listEc2(sys.argv[1])