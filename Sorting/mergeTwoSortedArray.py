a1 = [3, 5, 7, 9]
a2 = [2, 4, 6, 8, 8, 10]

# Lengths
l1 = len(a1)
l2 = len(a2)
l3 = l1 + l2
a3 = [0] * l3  # Initialize the array of length l1+l2

i, j, k = 0, 0, 0

# Merging the lists
while i < l1 and j < l2:
    if a1[i] < a2[j]:
        a3[k] = a1[i]
        i += 1
    else:
        a3[k] = a2[j]
        j += 1
    k += 1

# Adding remaining elements from a1
while i < l1:
    a3[k] = a1[i]
    i += 1
    k += 1

# Adding remaining elements from a2
while j < l2:
    a3[k] = a2[j]
    j += 1
    k += 1

print(a3)


##############without
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        k=n+m-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        