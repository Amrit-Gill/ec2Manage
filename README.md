# Introduction
There are three scripts to list, start and stop aws-ec2 instances using python command line. 

# Prerequisite
- [Boto3](https://github.com/boto/boto3)
- [Boto3 Documentation](http://boto3.readthedocs.io/en/latest)

# Use
## listEc2
```python listEc2.py [arg]```   
Single input argument accepted. Valid choices are [all, running, stopped].

## startEc2
```python startEc2.py [arg]```   
Single input argument accepted. Valid choices is the instance id.

## stopEc2
```python stopEc2.py [arg]```   
Single input argument accepted. Valid choices is the instance id.