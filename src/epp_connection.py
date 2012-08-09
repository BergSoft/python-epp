'''
Created on Aug 9, 2012

@author: berendi
'''

class EppConnection(object):
  
  hostname          = ''
  port              = 700
  timeout           = 5
  username          = ''
  password          = ''
  defaultnamespace  = {'xmlns':'urn:ietf:params:xml:ns:epp-1.0'}
  objuri            = {'domain':'urn:ietf:params:xml:ns:domain-1.0', 'contact':'urn:ietf:params:xml:ns:contact-1.0', 'host':'urn:ietf:params:xml:ns:host-1.0'}
  exturi            = None
  xpathuri          = {'epp':'urn:ietf:params:xml:ns:epp-1.0','contact':'urn:ietf:params:xml:ns:contact-1.0','host':'urn:ietf:params:xml:ns:host-1.0','ns':''}
  language          = ''
  version           = ''
  connection        = None
  logging           = None
  responses         = {}
  
  
  def __init__(self, logging = False):
    if logging:
      self.enableLogging()
    
    self.language   = 'en'
    self.version    = '1.0'
    
    self.responses['eppHelloRequest']     = 'eppHelloResponse';
    self.responses['eppLoginRequest']     = 'eppLoginResponse';
    self.responses['eppLogoutRequest']    = 'eppLogoutResponse';
    self.responses['eppPollRequest']      = 'eppPollResponse';
    self.responses['eppCheckRequest']     = 'eppCheckResponse';
    self.responses['eppInfoRequest']      = 'eppInfoResponse';
    self.responses['eppCreateRequest']    = 'eppCreateResponse';
    self.responses['eppDeleteRequest']    = 'eppDeleteResponse';
    self.responses['eppUpdateRequest']    = 'eppUpdateResponse';
    self.responses['eppRenewRequest']     = 'eppRenewResponse';
    self.responses['eppTransferRequest']  = 'eppTransferResponse';
  
  
  def __del__(self):
    if self.logging:
      self.showLog()
  
  
  def enableLogging(self):
    pass
  
  def showLog(self):
    pass
    
  