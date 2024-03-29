# def topkfrequent(nums,k):

#     elem_dict = {}
#     for i in nums:
#         if i in elem_dict:
#             elem_dict[i] +=1
#         else:
#             elem_dict[i] = 1

#     elem_list = []
#     for key,value in elem_dict.items():
#         elem_list.append([key,value])

#     elem_list = sorted(elem_list,key = lambda x : x[1], reverse=True)

#     result = []
#     for i in range(k):
#         result.append(elem_list[i][0])
    
#     print(result)

# topkfrequent([4,1,-1,2,-1,2,3],2)

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# METHOD 2

# Python3 program to find k numbers with most
# occurrences in the given array
 
from collections import Counter 
 
def print_N_mostFrequentNumber(nums, k, out):
    # Count the occurrences of each number
    counts = Counter(nums)
    print(counts)
 
    # Get the k numbers with the highest occurrences
    most_frequent = counts.most_common(k)
    print(most_frequent)
    
    # Extract the numbers from the most frequent pairs
    numbers = [num for num, _ in most_frequent]
    print(numbers)
 
    # Store the numbers in the output list
    for i, num in enumerate(numbers):
        out[i] = num
 
    return out
 
 
# Driver's code
arr = [3, 1, 4, 4, 5, 2, 6, 1]
K = 2
 
# Function call
ans = [0] * K
print_N_mostFrequentNumber(arr, K, ans)
print(K, "numbers with most occurrences are:")
print(ans[::-1])