def middleNode(self, head):
    """                       
    :type head: ListNode
    :rtype: ListNode
    """ 
    #NOTE: In case where there are 2 middle nodes,
    #      to return left middle: slow, fast = head, head.next  (USE DUMMY HEAD TO AVOID NULLPTR PROBLEMS)
    #      to return right middle: slow, fast = head, head
    slow, fast = head, head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    return slow
