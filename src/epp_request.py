'''
Created on Aug 8, 2012

@author: berendi
'''
from epp_document import EppDocument
from uuid import uuid4


class eppRequest(object):
  
  epp           = None
  command       = None
  sessionid     = None
  domainobject  = None
  contactobject = None
  hostobject    = None
  
  
  
  def __init__(self):
    self.sessionid = uuid4()
    self.document = ()
    self.format_output = True
    
    self.document.appendChild(self.document.createElement("epp"))
    
  
    
  def add_extension(self, name, value):
    if self.document.hasElement("epp"):
      self.document.setAttribute("epp", name, value)
      
      
  def add_sessionid(self):
    # Remove old session IDs
    for elem in self.document.getElementsByTagName("clTRID"):
      self.document.removeChild(elem)

    self.document.appendChild(self.document.createTextElement("clTRID", self.sessionid))
  
  
  def add_namespaces(self, namespaces):
    
    for xmlns, namespace in namespaces.iteritems():
      
      targetobj = "{0}object".format(xmlns)
      
      if targetobj == 'secDNSobject':
        targetobj = 'domainobject' # Add SECDNS entry to domain object
      
      
      if not hasattr(self, targetobj):
        raise AttributeError()
      
      eppobj = getattr(self, targetobj)
      
      if not isinstance(eppobj, EppDocument):
        raise TypeError()

      eppobj.documentElement.setAttribute("xmlns:{0}".format(xmlns), namespace)
        
  
  
  def get_xml(self):
    return self.document.toprettyxml(encoding="utf8")

