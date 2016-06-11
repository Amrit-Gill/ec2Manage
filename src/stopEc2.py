#!/usr/bin/python

import sys, boto3

def verifyInArg(argv):
	bool = True
	if len(sys.argv) != 2:
		bool = False
		print('One input argument required | %d given | Valid choices is the instance id' %(len(sys.argv)-1))
	return bool


def stopEc2(id):
	ec2 = boto3.resource('ec2')
	try:
		instance = ec2.Instance(id)
	except ValueError:
		print("Oops!  The instance id is not valid")

	if instance.state['Name'] in ["stopped"]:
		print("Instance already stopped")
	else:
		instance.stop()
		print('Instance stoped')


if __name__ == '__main__':
	bool = verifyInArg(sys.argv)
	if bool:
		stopEc2(sys.argv[1])