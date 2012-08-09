'''
Created on Aug 8, 2012

@author: berendi
'''
from xml.dom import minidom
import xml.dom


class EppDocument(minidom.Document):
  
  
  def hasElement(self, elem):
    for x in self.childNodes:
      if x.nodeName == elem:
        return True
    
    return False
  
  def setChildNodeAttribute(self, elem, attr, value):
    if not self.hasElement(elem):
      raise xml.dom.NotFoundErr()
    
    for x in self.childNodes:
      if x.nodeName == elem:
        x.setAttribute(attr, value)
        
    return True