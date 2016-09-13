#ex1.4
def find_the_smaller_number(a,b)
 if a < b
  return(a)
 else
  return(b)

def find_all_substrings(string1,substring_len)
number_of_substrings=len(string1)-substring_len+1
list_of_substrings=list[]
for i in range(number_of_substrings)
 list_of_substrings[i]=string1[i:i+substring_len-1]
 return(list_of_substrings)


 def longest_common_substring(seq1,seq2)
 len1=len(seq1)
 len2=len(seq2)
 max_substring_len=find_the_smaller_number(len1,len2)
 substring_ite=reversed(range(max_substring_len))
 longest_common_substring=''
for j in substring_ite
for k in range(max_substring_len+j)
