class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        na, nb = len(nums1), len(nums2)
        n = na + nb

        def solve(k, astart, aend, bstart, bend):
            if astart > aend:
                return nums2[k - astart]
            elif bstart > bend:
                return nums1[k-bstart]
            else:
                ai = (astart + aend)//2
                bi = (bstart + bend)//2
                av = nums1[ai]
                bv = nums2[bi]
                if ai + bi < k:
                    if av < bv:
                        return solve(k, ai+1, aend, bstart, bend)
                    else:
                        return solve(k, astart, aend, bi+ 1, bend)
                else:
                    if av < bv:
                        return solve(k, astart, aend, bstart, bi - 1)
                    else:
                        return solve(k, astart, ai -1, bstart, bend)
        
        if n % 2:
            return solve(n//2, 0, na - 1, 0, nb-1)
        else:
            return (
                solve(n //2-1, 0, na - 1, 0 , nb -1)
                + solve(n //2, 0, na -1, 0, nb -1)
            )/2
