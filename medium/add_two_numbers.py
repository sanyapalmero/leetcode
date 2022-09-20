from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return []
        
        ln_first = None
        ln_last = None
        
        temp_num = 0
        while l1 is not None or l2 is not None:    
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            s = l1_val + l2_val + temp_num
            temp_num = 0
            val = s % 10
            temp_num = s // 10
            
            if not ln_first:
                ln_first = ListNode()
                ln_first.val = val
                ln_last = ln_first
            else:
                ln_new = ListNode()
                ln_new.val = val
                ln_last.next = ln_new
                ln_last = ln_new
            
            if temp_num != 0:
                ln_new = ListNode()
                ln_new.val = temp_num
                ln_last.next = ln_new
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ln_first


def main():    
    def _create_nodes(data):
        ln_first = None
        ln_last = None

        for num in data:
            if not ln_first:
                ln_first = ListNode()
                ln_first.val = num
                ln_last = ln_first
            else:
                ln_new = ListNode()
                ln_new.val = num
                ln_last.next = ln_new
                ln_last = ln_new

        return ln_first

    l1 = _create_nodes([9,9,9,9,9,9,9])
    l2 = _create_nodes([9,9,9,9])

    add_two_numbers(l1, l2)


main()
