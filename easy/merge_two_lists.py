from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        merged_list = None
        last_node = None
                
        while list1 or list2:
            l1_val = list1.val if list1 else None
            l2_val = list2.val if list2 else None
            
            if l1_val is None and l2_val is None:
                return merged_list

            low_val = None
            if l1_val is not None and l2_val is not None:
                low_val = l1_val if l1_val < l2_val else l2_val
            
            if l1_val is None and l2_val is not None:
                low_val = l2_val
            elif l1_val is not None and l2_val is None:
                low_val = l1_val
            
            new_node = ListNode(val=low_val)
            if not merged_list:
                merged_list = new_node
                last_node = merged_list
            else:
                last_node.next = new_node
                last_node = new_node
            
            if l1_val is not None and l2_val is not None and l1_val >= l2_val:
                list2 = list2.next if list2 else None
            elif l1_val is not None and l2_val is not None and l1_val < l2_val:
                list1 = list1.next if list1 else None
            elif l1_val is not None and l2_val is None:
                list1 = list1.next if list1 else None
            elif l1_val is None and l2_val is not None:
                list2 = list2.next if list2 else None
                
        return merged_list


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

    l1 = _create_nodes([-10, -9, -6, -4, 1, 9, 9])
    l2 = _create_nodes([-5, -3, 0, 7, 8, 8])

    merge_two_lists(l1, l2)


main()
