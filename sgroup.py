import boto3

ec2 = boto3.resource('ec2')

sgs = list(ec2.security_groups.all())
insts = list(ec2.instances.all())

# get orphaned security group id's
all_sgs_ids = set([sg.group_id for sg in sgs])
all_inst_sgs_ids = set([sg['GroupId'] for inst in insts for sg in inst.security_groups])
unused_sgs_ids = all_sgs_ids - all_inst_sgs_ids

# get orphanced security group names
all_sgs_names = set([sg.group_name for sg in sgs])
all_inst_sgs_names = set([sg['GroupName'] for inst in insts for sg in inst.security_groups])
unused_sgs_names = all_sgs_names - all_inst_sgs_names


print '-' * 42
print 'Total Security Groups:', len(all_sgs_ids)
print 'Security Groups attached to instances:', len(all_inst_sgs_ids)
print 'Orphaned Security Groups:', len(unused_sgs_ids)
print '-' * 42
print 'Orphaned Security Group Ids:'
print ', '.join(unused_sgs_ids)
print '-' * 42
print 'Orphaned Security Group Names:'
print ', '.join(unused_sgs_names)
print '-' * 42
