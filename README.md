# aws-orphaned-security-groups
Boto3 script that finds orphaned security groups

Requirements
boto3

Artifact

<pre>
$ python sgroup.py
------------------------------------------
Total Security Groups: 106
Security Groups attached to instances: 55
Orphaned Security Groups: 51
------------------------------------------
Orphaned Security Group Ids:
sg-xxxxxxxx, sg-yyyyyyyy, ...
------------------------------------------
Orphaned Security Group Names:
sg-name-example-1, sg-name-example-2, ...
------------------------------------------
</pre>
