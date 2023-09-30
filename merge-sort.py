"""Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2."""




def merge(nums1, m, nums2, n):
  # initalize 2 pointers
  p1, p2 = m - 1, n - 1
  #start from the end of nums1 where elements should be placed
  idx = m + n - 1

  # While there are elements to consider in both arrays
  while p1 >= 0 and p2 >= 0:
    if nums1[p1] > nums1[p1]:
      nums1[idx] = nums1[p1]
      p1 -= 1
  else:
    nums1[idx] = nums2[p2]
    p2 -= 1
  idx -= 1

# If there are any remaining elements in nums2
# Copy them directly to nums1
# No need to check for remaining elements in nums1 because we're merging into nums1

  while p2 >= 0:
    nums1[idx] = nums2[p2]
    p2 -= 1
    idx -= 1