'''
Created on Aug 7, 2012

@author: berendi
'''
import socket
import time


class EppProtocol(object):
  
  
  connection = ''
  timeout = ''
  
  
  def connect(self, address, port, timeout):
    self.connection = socket.create_connection("{0}:{1}".format(address, port), timeout)
    self.timeout = timeout
  
  
  # Read a response
  def read(self):
    timeout = time.time() + self.timeout
    output = ''
      
    # Get the first 4 bytes; as these contain the content-length
    read = self.connection.recv(4)
    if len(read) == 0:
      raise RuntimeError("Socket connection broken.")
    
    # Message length
    msg_len = self.read_int(read)
    
    # Receive the rest
    recv_len = 0
    while recv_len < msg_len:
      if time.time() >= timeout:
        return False
      
      timeout = time.time() + 5
      read = self.connection.recv(1024)
      
      if len(read) == 0:
        raise RuntimeError("Socket connection broken.")
        
      recv_len += len(read)
      output += read
  
    return output
          
          
  def read_int(self, content):
    intval = content[0:4]
    intval = ord(intval[3])+256*(ord(intval[2])+256*(ord(intval[1])+256*(ord(intval[0]))))
    
    return intval
  
  
  def add_int(self, content):
    length = len(content)+4;
    int3   = chr(length%256);
    length = length/256;
    int2   = chr(length%256);
    length = length/256;
    int1   = chr(length%256);
    length = length/256;
    int0   = chr(length%256);
    
    return "{0}{1}{2}{3}{4}".format(int0, int1, int2, int3, content)

  
  
  def write(self, content):
    content = self.add_int(content)
    
    sent_len = 0
    
    while sent_len < len(content):
      sent = self.connection.send(content[sent_len:])
      
      if sent == 0:
        raise RuntimeError("Socket connection broken.")
      
      sent_len += sent
      
    return True
    
    
  
  