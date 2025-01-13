import math
class Product:
    def __init__(self,name,price,stock,category):
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category
    def __str__(self):
        return f"name:{self.name} , price:{self.price} , stock:{self.stock} , category:{self.category}"    
    def update_stock(self,quantity):
        self.stock-=quantity    
    def is_in_stock(self,quantity):
        self.stock>=quantity

class Cart:
    def __init__(self):
        self.items={}
    def add_product(self,product, quantity):
        if product in self.items:
            self.items[product]+=quantity    
        else:
            self.items[product]=quantity    
    def remove_product(self,product):
        self.items.pop(product)
    def update_quantity(self,product,quantity):
        if self.items[product]<quantity:
            return f"you have only {self.items[product]} items of {product.name} in your cart "
        if self.item[product]==quantity:
            self.items.pop(product)
        else:    
            self.items[product]-=quantity
    def calculate_total(self):
        total=0
        for product in self.items:
            total+=product.price*self.items[product]
        return total    
    def checkout(self):
        self.items.clear()
        return self.calculate_total

class User:
    def __init__(self,username):
        self.username=username
        self.cart=Cart()       
    def add_to_cart(self,product, quantity):
        try:
            if quantity<=0:
                raise ValueError("quantity has to be greater then 0")
            else:
                self.cart.add_product(product,quantity)
        except ValueError as e:
            print(f"Error : {e}")

    def remove_from_cart(self,product):    
        self.cart.remove_product(product)
    def view_cart(self):
        for product,quantity in self.cart.items.items():
            print(f"{product.name} -> price: {product.price} , quantity: {quantity}")

        print(f"total price: {self.cart.calculate_total()}\n")        

class PreimumUser(User):
    def __init__(self,username,discount):
        super().__init__(username)
        self.discount=discount
    def add_to_cart(self,product, quantity):
        try:
            if quantity<=0:
                raise ValueError("quantity has to be greater then 0")
            else:
                product.price-=product.price*(self.discount/100)
                self.cart.add_product(product,quantity)
        except ValueError as e:
            print(f"Error : {e}")    


class Admin:
    def __init__(self):
        self.products={}
    def add_product(self,product):
        self.products[product]=product
    def remove_product(self,product):
        self.products.pop(product)
    def update_product(self,product, name=None, price=None, stock=None):
        self.products[product].name=name
        self.products[product].price=price
        self.products[product].stock=stock
    def view_catalog(self):
        print("catalog:")
        for product in self.products.values():
            print(f"{product.name} -> price: {product.price} , stock:{product.stock} , category:{product.category}")    
        print('\n')    



# class Solution:
#     def combine(self, n: int, k: int):
#         result = []
#         self.backtrack(1, n, k, [], result)
#         return result
    
#     def backtrack(self, start, n, k, combination, result):
#         if len(combination) == k:
#             result.append(combination[:])
#             return
        
#         for i in range(start, n + 1):
#             combination.append(i)
#             self.backtrack(i + 1, n, k, combination, result)
#             combination.pop()


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         index=-1
#         j=0
#         i=0
#         for i in range(len(haystack)):
#             if(haystack[i]==needle[0]):
#                 while (i+j)<len(haystack) and j<len(needle):
#                     if(haystack[i+j]!=needle[j]):
#                         break
#                     j+=1
#                 if j==len(needle):
#                     return i
#                 else:
#                     j=0
#         return -1                


# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         temp_list=[]
#         i=0
#         j=0
#         while i<m and j<n:
#             if nums1[i]==nums2[j]:
#                 temp_list.append(nums1[i])
#                 temp_list.append(nums1[i])
#                 i+=1
#                 j+=1
#             elif nums1[i]>nums2[j]:
#                 temp_list.append(nums2[j])
#                 j+=1
#             else:
#                 temp_list.append(nums1[i])
#                 i+=1
#         while i<m:        
#             temp_list.append(nums1[i])
#             i+=1
#         while j<n:        
#             temp_list.append(nums2[j])
#             j+=1    
#         nums1[:len(temp_list)]=temp_list


# class Solution:
#     def countNumbersWithUniqueDigits(self, n: int) -> int:
#         if n==0:
#             return 1
#         if(n==1):
#             return 10
#         sum=10
#         curr=9
#         for i in range(n,1,-1):
#             for j in range(i-1):
#               curr*=(9-j)
#             sum+=curr
#             curr=9
#         return sum      



# class Soluion:
#     def repeatedSubstringPattern(self,s):
#         current_string=''
#         flag=True
#         for i in range(1,len(s)//2+1):
#             if len(s)%i:
#                 continue
#             current_string=s[:i]
#             for j in range(i,len(s)-i+1,i):
#                 if current_string!=s[j:j+i]:
#                     flag=False
#                     break
#             if flag:
#                 return True
#             flag=True    
#             current_string=''
#         return False
        


# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         perimeter=0
#         for i in range(grid.length()):
#             for j in range(grid[0].length()):
#                 if grid[i][j]:
#                     perimeter+=4
#                     if i>0:
#                         perimeter-=grid[i-1][j]
#                     if i<grid.length()-1:
#                         perimeter-=grid[i+1][j]
#                     if j>0:
#                         perimeter-=grid[i][j-1]
#                     if j<grid[0].length()-1:
#                         perimeter-=grid[i][j+1]
#         return perimeter        

            


# class Solution:
#     def findComplement(self, num: int) -> int:
#         res=0
#         while num:
#             res=(res<<1) | ((num&1)^1)
#             num>>=1
#         return res    




# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         dict_letter_to_row={}
#         result=[]
#         first_row="qwertyuiop"
#         second_row="asdfghjkl"
#         third_row="zxcvbnm"
#         curr_row=-1
#         flag=True
#         for i in range(26):
#             letter = chr(ord('a') + i)
#             if letter in first_row:
#                 dict_letter_to_row[letter]=1
#             if letter in second_row:
#                 dict_letter_to_row[letter]=2
#             if letter in third_row:
#                 dict_letter_to_row[letter]=3
#         for i in range(len(words)):
#             curr_row=dict_letter_to_row[words[i][0].lower()]
#             for j in range(len(words[i])):
#                 if dict_letter_to_row[words[i][j].lower()]!=curr_row:
#                     flag=False
#                     break
#             if flag:
#                 result.append(words[i])
#             flag=True
#         return result       


# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         if num==1:
#             return False
#         count=1
#         for i in range(2,math.ceil(math.sqrt(num))):
#             if num%i==0:
#                 count+=i
#                 count+=num/i
#         if type(math.sqrt(num)) is int:
#             count+=math.sqrt(num)
#         return count==num
        
     
# class Solution:
#     def fib(self, n: int) -> int:
#         a=0
#         b=1
#         if n<=1:
#             return n
#         for i in range(1,n):
#             res=a+b
#             a=b
#             b=res
#         return res    



# class Solution:
#     def checkRecord(self, s: str) -> bool:
#         sum_A,sum_L=0,0
#         for i in range(len(s)):
#             if s[i]=='A':
#                 if sum_A==1:
#                     return False
#                 sum_A+=1
#                 sum_L=0
#             elif s[i]=='L':
#                 if sum_L==2:
#                     return False
#                 sum_L+=1
#             else:
#                 sum_L=0 
#         return True           
                


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         arr_of_words=s.split(' ')
#         s_reversed=''
#         for word in arr_of_words:
#             s_reversed+=word[::-1]
#             s_reversed+=' '
#         s_reversed=s_reversed.strip(' ')   
#         return s_reversed 


# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         g.sort()
#         s.sort()
#         i,j,count=0,0,0
#         while i<len(g) and j<len(s):
#             if s[j]>=g[i]:
#                 count+=1
#                 i+=1
#                 j+=1
#             else:
#                 j+=1
#         return count            
                
            


# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         start,end=0,len(nums)-1
#         max_height=None
#         while start<end:              
#             if nums[start]<nums[start+1] and nums[end]<nums[end-1]:
#                 break
#             if nums[start]>nums[start+1]:
#                 start+=1
#             if nums[end]>nums[end-1]:
#                 end-=1

#         if start==end:
#             return False
        

#         for i in range(start+1,end):
#             if nums[i]>nums[start] and nums[i]>nums[end]:
#                 if max_height==None or nums[i]>nums[max_height]:
#                     max_height=i    

#         end=len(nums)-1
#         max_left=None
#         while end>max_height:
#             if nums[end]<nums[max_height]:
#                if max_left==None or nums[end]>max_left:
#                    max_left=nums[end]
#             end-=1       


#         start=0
#         min_right=None
#         while start<max_height:
#             if nums[start]<nums[max_height]:
#                if min_right==None or nums[start]<min_right:
#                    min_right=nums[start]           
#             start+=1

#         if min_right==None or max_left==None:
#             return False
#         if min_right<max_left<nums[max_height]:
#             return True
#         return False

                

# class Solution:
#     def find132pattern(self, nums):
        
#         st = []
#         cur_min = nums[0]

#         for n in nums[1:]:
#             while st and n >= st[-1][0]:
#                 st.pop()
            
#             if st and n > st[-1][1]:
#                 return True
            
#             st.append([n, cur_min])
#             cur_min = min(cur_min, n)
        
#         return False




# class Solution:
#     def totalHammingDistance(self, nums: List[int]) -> int:
#         total_count=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 total_count+=self.HammingDistance(nums[i],nums[j])
#         return total_count   
#     def HammingDistance(self,num1,num2):
#         num1=num1^num2
#         count=0
#         while(num1):
#             count+=num1&1
#             num1>>=1
#         return count    



# class Solution:
#     def nextGreaterElement(self, nums1, nums2):
#         num_to_greater={}
#         ans=[]
#         num_to_greater[nums2[-1]]=-1

#         stack=[]
#         stack.append(nums2[-1])

#         for i in range(len(nums2)-2,-1,-1):
#             while stack:
#                 if nums2[i]<stack[-1]:
#                     num_to_greater[nums2[i]]=stack[-1]    
#                     break
#                 stack.pop()    
#                 if not stack:
#                     num_to_greater[nums2[i]]=-1
#                     break    
#             stack.append(nums2[i])
#         for i in range(len(nums1)):
#             ans.append(num_to_greater[nums1[i]])
#         return ans
        

# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         sorted_score=sorted(score,reverse=True)
#         nums_to_places={}
#         result=[]
#         for i,num in enumerate(sorted_score):
#             nums_to_places[num]=i+1
#         for num in score:
#             if nums_to_places[num]==1:
#                 result.append("Gold Medal")
#             elif nums_to_places[num]==2:
#                 result.append("Silver Medal")  
#             elif nums_to_places[num]==3:
#                 result.append("Bronze Medal")        
#             else:
#                 result.append(f"{nums_to_places[num]}")
#         return result                



# class Solution:
#     def min_magistic(self,s):
#         curr=0
#         set_totals=set()
#         set_totals.add(0)
#         for i in range(len(s)):
#             if s[i]=='<':
#                 curr-=1
#                 set_totals.add(curr)
#             elif s[i]=='>':
#                 curr+=1
#                 set_totals.add(curr)
#         return len(set_totals)
                

 #!/usr/bin/python


class TestImpl:        
    def validatePasswords(self,passwords):
        passwords_list=[]
        valid_passwords=''
        lower_exist=False
        upper_exist=False
        char_exist=False
        int_exist=False
        passwords_list=passwords.split(',')
        for i,password in enumerate(passwords_list):
            if len(password)<6 or len(password)>12:
                continue
            for char in password:
                if char.isupper():
                    upper_exist=True
                elif char.islower(): 
                    lower_exist=True
                elif char=='$' or char=='#' or char=='@':
                    char_exist=True
                elif char in "0123456789":             
                    int_exist=True
            
            if upper_exist and lower_exist and char_exist and int_exist:
                valid_passwords+=password
                if i!=len(passwords_list)-1:
                    valid_passwords+=','
            upper_exist=False
            lower_exist=False
            char_exist=False
            int_exist=False
        return valid_passwords             


def main():
    sol=TestImpl()
    password="gilad"
    sol.validatePasswords(password)







if __name__ == "__main__":
    main()
