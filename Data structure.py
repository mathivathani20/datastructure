# working-with-Data-structure
#union
def union(set1,set2):
    return set(set1)&(set2)
# driver code
Set1={0,2,3,4,5,6,8}
Set2={1,2,3,4,5}
Print(union(set1,set2))

#intersection
def intersection(set1,set2):
    return set(set1)&(set2)
#driver code
Set1={0,2,4,6,8}
Set2={1,2,4,4,5}
Print(intersection(set1,set2))

#difference
Set1={0,2,3,4,5,6,8}
Set2={1,2,3,4,5}
Set_difference=(set1)-(set2)
Set_difference=set(set_difference)
Print(set_difference)


#python code to find the symmetric_difference
#use of symmetric_difference()method
Set_A={0,2,4,6,8}
Set_B={1,2,3,4,5}
Print(set_A,symmetric_difference(set_B))
