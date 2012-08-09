'''
Created on Aug 8, 2012

@author: berendi
'''
from epp_request import eppRequest

t = eppRequest()
#t.add_extension("test_name", "test_val")
t.add_namespaces({'domain':'http://nu.nl/ns'})

print t.get_xml()