# class Solution(object):
#     def sortColors(self, nums):
#         last=0
#         if len(nums)==1:
#             return
#         for i in range(1,len(nums)):
#             if nums[last]==0:
#                 last+=1
#                 continue
#             if nums[i]==0:
#                 nums[i]=nums[last]
#                 nums[last]=0
#                 last+=1
                
#         for i in range(last,len(nums)):
#             if nums[last]==1:
#                 last+=1
#                 continue
#             if nums[i]==1:
#                 nums[i]=nums[last]
#                 nums[last]=1    
#                 last+=1    
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         if not head:
#             return None
#         res_node=head
#         runner_node=head
#         while(runner_node.next is not None):
#             if runner_node.next.val!=runner_node.val:
#                 res_node.next=runner_node.next
#                 res_node=res_node.next              
#             runner_node=runner_node.next 
#         res_node.next=None    
#         return head       

         
# class Solution(object):
#     def mySqrt(self, x):
#         i=1
#         while(i*i<=x):
#             i+=1
#         return i-1;    
        

# class Solution(object):
#     def plusOne(self, digits):
#         for i in range(len(digits)-1,-1,-1):
#             if digits[i]<9:
#                 digits[i]+=1
#                 return digits
#             else:
#                 if i>0:
#                     digits[i]=0
#                 else:
#                     digits[i]=0
#                     digits.insert(0,1)
#                     return digits    

        
                 
# class Solution:
#     def numTrees(self, n: int) -> int:
#         uniq_tree = [1] * (n + 1)
        
#         for nodes in range(2, n + 1):
#             total = 0
#             for root in range(1, nodes + 1):
#                 total += uniq_tree[root - 1] * uniq_tree[nodes - root]
#             uniq_tree[nodes] = total
        
#         return uniq_tree[n]



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         # Helper method to print the linked list
#         result = []
#         current = self
#         while current:
#             result.append(str(current.val))
#             current = current.next
#         return " -> ".join(result)

# # Create the linked list from a list of values
# def create_linked_list(values):
#     if not values:
#         return None
#     head = ListNode(values[0])
#     current = head
#     for value in values[1:]:
#         current.next = ListNode(value)
#         current = current.next
#     return head





class Solution(object):
    def search(self, nums, target):
        start=0
        end=len(nums)-1
        mid=0
        while start<=end:
            mid=start + (end-start)//2
            if nums[mid]==target:
                return True
            
            if nums[start]==nums[mid] and nums[end]==nums[mid]:
                start+=1
                end-=1
                continue
        
            if nums[start]<=nums[mid]:
                if target<nums[mid] and nums[start]<=target:
                    end=mid-1
                else:
                    start=mid+1

            else:            
                if target>nums[mid] and nums[start]>target:
                    start=mid+1
                else:
                    end=mid-1
                    
                 
        return False                







# Main function to test the Solution class
def main():
   sol=Solution()
   nums=[1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
   res=sol.search(nums,13)
   print(res)

if __name__ == "__main__":
    main()   