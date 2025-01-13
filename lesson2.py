# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m == 1 or n == 1:  # Base case: Only one path if one dimension is 1
#             return 1
#         mat=[[1 if i==0 or j==0 else 0 for j in range(n)] for i in range(m)]
#         for i in range(1,m):
#             for j in range(1,n):
#                 mat[i][j]=mat[i-1][j]+mat[i][j-1]
#         return mat[m-1][n-1]        
    


# class Solution(object):
#     def insert(self, intervals, newInterval):
    #    if not intervals:
    #        return [newInterval]
    #    if newInterval[1]<intervals[0][0]: 
    #       intervals.insert(0,newInterval)
    #       return intervals
    #    if(newInterval[0]==intervals[-1][1]):
    #       intervals[-1][-1]=newInterval[1]

    #    if(newInterval[0]>intervals[-1][1]):
    #        intervals.append(newInterval)
    #        return intervals
       
    #    i=0
    #    res=[]
    #    for i in range(len(intervals)):
    #        if newInterval[0]<=intervals[i][0]:
    #            res.append([newInterval[0],0])
    #            break
    #        elif newInterval[0]<=intervals[i][1]:
    #            res.append([intervals[i][0],0])   
    #            break
    #        else:
    #            res.append(intervals[i])

    #    start_index=i       
    #    for i in range(start_index,len(intervals)):
    #        if newInterval[1]==intervals[i][0]:
    #            res[-1][-1]=intervals[i][1]
    #            break
    #        if newInterval[1]<intervals[i][0]:
    #            res[-1][-1]=newInterval[1]
    #            break
    #        elif newInterval[1]<=intervals[i][1]:
    #            res[-1][-1]=intervals[i][1]
    #            break
           
    #    start_index=i    
    #    if res[-1][-1]==0:
    #        res[-1][-1]=newInterval[1]
    #        return res             
       
    #    for i in range(start_index,len(intervals)):
    #        if res[-1][-1]<intervals[i][0]:
    #            res.append(intervals[i])

    #    return res    

       
        

                        

# class Solution(object):

#     def restoreIpAddresses(self, s):
#         if len(s)>12:
#             return []
#         result=[]
#         temp=[]
#         self.backtracking(s,temp,result)
#         return result
    
#     def convert_to_string(self,list1):
#         str=""
#         for value in list1:
#             str+=value+'.'
#         str=str.rstrip(".")
#         return str

#     def backtracking(self,num,temp,result):
#         if len(temp)==3:
#             if len(num)<=3 and len(num)>0 and not (num[0]=='0' and len(num)>1) and (int(num)>=0 and int(num)<=255):
#                 temp.insert(0,num)
#                 str=self.convert_to_string(temp)
#                 result.append(str)
#                 temp.pop(0)
#             return
#         for i in range(1,4):
#             curr=num[-i:]
#             if(len(curr)==0 or(curr[0]=='0' and len(curr)>1) or int(curr)<0 or int(curr)>255):
#                 continue
#             temp.insert(0,curr)
#             self.backtracking(num[:-i],temp,result)
#             temp.pop(0)






# class Solution():
#     def combinations(self,num_list,target):
#         temp=[]
#         result=[]
#         sum=0
#         self.backtracking(0,num_list,target,temp,sum,result)
#         return result
#     def backtracking(self,start,num_list,target,temp,sum,result):
#         if sum==target:
#             result.append(temp.copy())
#             return
#         for i in range(start,len(num_list)):
#             if sum+(num_list[i]*2)<=target:
#                 sum+=num_list[i]
#                 temp.append(num_list[i])
#                 self.backtracking(i,num_list,target,temp,sum,result)
#                 sum-=temp[-1]
#                 temp.pop()
#             elif sum+num_list[i]<=target: 
#                 sum+=num_list[i]
#                 temp.append(num_list[i])
#                 self.backtracking(i+1,num_list,target,temp,sum,result)
#                 sum-=temp[-1]
#                 temp.pop()
                



class Solution:
    def rotate(self, matrix):
        n=len(matrix[0])
        print(n)
        for i in range(n//2):
            for j in range(i,n-1-i):
                temp1=matrix[j][n-i-1]
                matrix[j][n-i-1]=matrix[i][j]
                temp2=matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1]=temp1
                temp1=matrix[n-j-1][i]
                matrix[n-j-1][i]=temp2
                matrix[i][j]=temp1
        
        






def main():
    sol=Solution()
    matrix=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ]
    sol.rotate(matrix)
    print(matrix)

if __name__ == "__main__":
    main()    
                
        