class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def mergeListNode(l1,l2):
        dumy = res = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                res.next = ListNode(l2.val)
                l2 = l2.next
            else:
                res.next = ListNode(l1.val)
                l1 = l1.next
            res = res.next
        if l1:
            res.next = ListNode(l1.val)
            l1 = l1.next
        if l2:
            res.next = ListNode(l2.val)
            l2 = l2.next
        return dumy.next



