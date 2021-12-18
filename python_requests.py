#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:44:08 2021

@author: dawid
"""

import requests
import datetime
import hashlib
import hmac

# use empty string if api_subaccount_id not present

def get_api_key_from_file(filepath):
    file = open(filepath, 'r')
    line = file.readline()
    file.close()
    return line

def get_api_secret_from_file(filepath):
    file = open(filepath, 'r')
    line = file.readline()
    file.close()
    return line
    

def generate_api_signature(timestamp, uri, http_method_type, api_content_hash, api_subaccount_id, file_path,request_body):
    signature = str(timestamp) + uri + http_method_type + str(api_content_hash) + api_subaccount_id
    secret = get_api_secret_from_file(file_path) 
    return hmac.new(secret.encode(), signature.encode(), hashlib.sha512).hexdigest()    

def generate_api_content_hash(request_body):
    return hashlib.sha512(request_body.encode()).hexdigest()


def get_timestamp():
    date = datetime.datetime.now()
    time_stamp = str(datetime.datetime.timestamp(date)*1000)
    return time_stamp[0:13]
    


def do_request(uri, api_key_file_path, secret_file_path, method, request_body):
    headers = {'api-key': get_api_key_from_file(api_key_file_path), 
           'api-timestamp': get_timestamp(), 
           'api-content-hash': generate_api_content_hash(request_body),
           'api-signature': generate_api_signature(get_timestamp(), 
                                                   uri, 
                                                   method, 
                                                   generate_api_content_hash(request_body),
                                                   '',
                                                   secret_file_path,
                                                   '')
           }
    
    if (method == 'GET'):
       request = requests.get(uri, headers=headers)
       return request.content
         

uri = 'https://api.bittrex.com/v3/account'
uri_currencies = 'https://api.bittrex.com/v3/currencies'
file_path_api_key = '/home/dawid/Documents/api_key.txt'
file_path_api_secret = '/home/dawid/Documents/api_secret.txt'

print(do_request(uri_currencies, file_path_api_key,file_path_api_secret, 'GET', '', ))


   