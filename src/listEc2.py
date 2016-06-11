#!/usr/bin/python

import sys, boto3

def verifyInArg(argv):
	bool = True
	if len(sys.argv) != 2 or sys.argv[1] not in ["all", "running", "stopped"]:
		bool = False
		print('One input argument required | %d given | Valid choices are all, running or stopped' %(len(sys.argv)-1))
	return bool


def listEc2(state):
	stateValue = state
	if state in ["all"]:
		stateValue = '*'

	ec2 = boto3.resource('ec2')
	instances = ec2.instances.filter(
    	Filters=[{'Name': 'instance-state-name', 'Values': [stateValue]}])
	if not list(instances):
		print('No %s instance' %stateValue)
	for instance in instances:
		print('Instance State' + '\t' + 'Instance Id' + '\t' + 'Instance Type')
		print(instance.state['Name'] + '\t' + '\t' + instance.id + '\t' +  instance.instance_type)


if __name__ == '__main__':
	bool = verifyInArg(sys.argv)
	if bool:
		listEc2(sys.argv[1])