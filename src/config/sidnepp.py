'''
Created on Aug 7, 2012

@author: berendi
'''

"""
IP/Hostname of the EPP Server
"""
SERVER_ADDRESS   = 'testdrs.domain-registry.nl';

"""
The protocol prefix used for the connection to the EPP interface
"""
PROTOCOL_PREFIX = 'ssl://';

"""
EPP Server name for use for validating if the server runs a compatible version with this client;
"""
SERVER_NAME    = 'testdrs.domain-registry.nl';

"""
Port of the EPP Server
"""
SERVER_PORT  = "700";

"""
Username at the EPP Server
"""
USERNAME    = '';

"""
Password
"""
PASSWORD    = '';

"""
Base directory of the Sidn EPP API
"""
RUN_PATH      = '';

"""
Timeout of the connection
"""
TIMEOUT       = 5;

"""
Location of the directory of where the XML's are located. This will base of the RUN_PATH constant.
This shouldn't have to be edited unless you changed the XML directory to a different location.
"""
XML_PATH    = '/xml';