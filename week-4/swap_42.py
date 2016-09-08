import sys

new_dict = {}

def swap_keys_values(d):
    new_dict = dict([(v,k) for k,v in d.items()])

    return new_dict

#his is same as ours
