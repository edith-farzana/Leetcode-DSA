class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
#
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        half = (m + n + 1) // 2

        while left <= right:

            partitionA = (left + right) // 2
            partitionB = half - partitionA
            if partitionA == 0:
                Aleft = float('-inf')
            else:
                Aleft = nums1[partitionA - 1]

            if partitionA == m:
                Aright = float('inf')
            else:
                Aright = nums1[partitionA]

            if partitionB == 0:
                Bleft = float('-inf')
            else:
                Bleft = nums2[partitionB - 1]

            if partitionB == n:
                Bright = float('inf')
            else:
                Bright = nums2[partitionB]
            if Aleft <= Bright and Bleft <= Aright:


                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)
           
                return (max(Aleft, Bleft) +
                        min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                right = partitionA - 1

            else:
                left = partitionA + 1
