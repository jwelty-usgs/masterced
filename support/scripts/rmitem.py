#!/usr/bin/python
import sciencebasepy as pysb
import getopt
import sys
import os

opt_fields = ['env=','user=','id=<id1>,<id2>,...,<idn>','children', 'test', 'undelete', 'batchsize']
def usage():
    print("""
    %s id1,id2,...,idn [options]
    
Deletes items and their children

Required Parameters
-------------------
    --env=[prod|beta] The ScienceBase environment to run in (default to prod)
    --user=[User] Username to run job as (defaulted if stored in ~/.pw)    
Optional Parameters
-------------------
    --children Delete only children
    --test Test to see what would be deleted
    --undelete Undelete previously deleted items
    --batchsize=[size] Number of items to delete at a time, up to 1000.  Default is 100.
""" % (sys.argv[0]))

def get_user_pw_from_file(filename):
    password = 'Sage4GrouseCED!!'
    sbuser = 'fw1sagegrouseced'
    if filename and os.path.isfile(os.path.expanduser(filename)):
        with open (os.path.expanduser(filename), "r") as myfile:
            data=myfile.readlines()
            userpw = data[0].split()
            if len(userpw) == 2:
                sbuser = str(userpw[0].strip())
                password = str(userpw[1].strip())
    return sbuser, password
    
def undelete_items(item_ids):
    for item_id in reversed(item_ids):
        print("restoring " + str(item_id))
        if not istest:
            try:
                sb.undeleteSbItem(item_id)
            except:
                print("RESTORE FAILED!")
                
def get_delete_ids(item_id, delete_self):
    items_to_delete = []
    for child_id in sb.get_child_ids(item_id):
        items_to_delete.extend(get_delete_ids(child_id, True))
    if delete_self:
        items_to_delete.append(item_id)
    return items_to_delete
    
def delete_items(item_ids, batchsize, delete_only_children):
    items_to_delete = []
    for item_id in item_ids:  
        items_to_delete.extend(get_delete_ids(item_id, not delete_only_children))
    savelist = list(items_to_delete)
    batchnum = 0
    while items_to_delete:
        batch = items_to_delete[:batchsize]
        batchnum += 1
        print("deleting batch %s: %s" % (str(batchnum), batch))        
        if not istest:
            sb.delete_items(batch)
        items_to_delete = items_to_delete[batchsize:]
    print('deleted: '),
    print(','.join(savelist))
    
#
# Main
#
if len(sys.argv) < 2:
    usage()
    sys.exit(0)
try:
    opts, args = getopt.getopt(sys.argv[2:], '', opt_fields)
except getopt.GetoptError, err:
    print(str(err))
    usage()
    sys.exit(2)
    
delete_only_children = False
username = 'fw1sagegrouseced'
password = 'Sage4GrouseCED!!'
sbenv = "prod"
item_ids = [x.strip() for x in sys.argv[1].split(',')]
undelete = False
istest = False
batchsize = 100

for o, a in opts:
    if o in '--env':
        sbenv = a
    elif o in '--user':
        username = a
    elif o in '--batchsize':
        batchsize = min(int(o), 1000)
    elif o in '--children':
        delete_only_children = True
    elif o in '--undelete':
        undelete = True
    elif o in '--test':
        istest = True
    else:
        assert False, 'unhandled option'

if item_ids is None: 
    print('No ID specified')
    usage()
    sys.exit(1)
if username is None:
    username, password = get_user_pw_from_file('~/.pw')
    if username is None:        
        print('No user specified')
        usage()
        sys.exit(2)
if sbenv is None:
    print('No environment specified')
    usage()
    sys.exit(3) 
    
if istest:
    print('user=' + username),
    print('env=' + sbenv),
    print('items=' + str(item_ids)),
    print('undelete? ' + str(undelete)),
    print('children? ' + str(delete_only_children)),
    print('batchsize=' + str(batchsize))

if password:
    sb = pysb.SbSession(sbenv).login(username, password)
else:
    sb = pysb.SbSession(sbenv).loginc(username)

for item_id in item_ids:    
    if undelete:
        undelete_items(item_ids)
    else:
        delete_items(item_ids, batchsize, delete_only_children)       