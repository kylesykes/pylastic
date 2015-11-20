#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Library for high level interactions with ElasticSearch. 

Goals for this libray:
Functions to wrap basic index manipulations: create, delete, update.
Functions to push data at single documents and bulk mode.
Functions to create basic and complicated queries and searches.

"""

import requests
import json

########## Index functions ##########
def create_index(es_url, index_name, mapping=None):
    """Create index_name index and push the mapping if present."""
    if mapping:
        return requests.post('/'.join([es_url, index_name]), data=json.dumps(mapping, encoding='utf8'))
    else:
        return requests.put('/'.join([es_url, index_name]))
                
                
def delete_index(es_url, index_name):
    """Deletes the index_name index."""
    return requests.delete('/'.join([es_url, index_name]))

    
########## Load data functions ##########

# TODO: def add()   add single document


def add_bulk(es_url, index_name, iterable, d_type='default'):
    """Use the bulk API to load elements in iterable."""
    return requests.post('/'.join([es_url, index_name, d_type, '_bulk']), data=build_bulk_string(iterable))        
 

########## Load data functions ##########

   
    
########## Helper functions ##########
def build_bulk_string(iterable, action='create'):
    """Build a string in bulk syntax from iterable."""
    prefix = '{' + action + ':{}}\n'
    return prefix + prefix.join([json.dumps(o) + '\n' for o in iterable])
    
    