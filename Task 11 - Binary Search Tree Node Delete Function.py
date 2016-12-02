class Node(object):
  def __init__(self, value):
    self.value=value
    self.next=None
    self.prev=None

class List(object):
  def __init__(self):
    self.head=None
    self.tail=None
    
  def insert(self,n,x):
    if n!=None:
      x.next=n.next
      n.next=x
      x.prev=n
      if x.next!=None:
        x.next.prev=x              
    if self.head==None:
      self.head=self.tail=x
      x.prev=x.next=None
    elif self.tail==n:
      self.tail=x
      
  def display(self):
    values=[]
    n=self.head
    while n!=None:
      values.append(str(n.value))
      n=n.next
    print ("List: ",",".join(values))
  
  def remove(self, n):                                 #function remove   
    head = self.head                                   #head = self.head
    while head:                                        # while loop
      if head.value == n:                              #if value of head == n do the following
        if head.prev != None:                          #if head.prev not = none do the following
          head.prev.next = head.next                   #head.prev.next = head.next
        if head.next!= None:                           #if head.next not =none do the following
          head.next.prev=head.prev                     #head.next.prev=head.prev
        else:                                          #else
          self.head = head.next                        #self.head = head.next
        return True                                    #return True
      else:                                            #else
        head = head.next                               #head=head.next
    return False                                       #return false
    
          
if __name__ == '__main__':
  l=List()
  l.insert(None, Node(4))
  l.insert(l.head,Node(6))
  l.insert(l.head,Node(8))
  l.insert(l.head,Node(10))
  l.insert(l.head,Node(13))
  l.remove(13)
  l.display()
