class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # bottom up approach
        # we start with one candidate, and keep on adding one candidate after another until
        # sum is either larger than target, in which case, we dont proceed further;
        # or if sum is equal to target, we append the sequence to output.
        
        self.out = []
        def combination(sum_until_now, seq_until_now, index):
            if sum_until_now > target: return
            if sum_until_now == target: 
                self.out.append(seq_until_now)
                return
            
            # this is the important part. we ignore the candidates smaller than the last appended candidate in the sequence
            # this naturally sorts the sequence in ascending order. and thus avoids repeating sequences
            for i in range(index, len(candidates)):
                combination(sum_until_now + candidates[i], seq_until_now + [candidates[i]], i)
                
        combination(0, [], 0)
        return self.out
    
    #the other way to solve this is backtracking. we take the target, and keep on substracting candidates, and check if 0
    # is reached and add the sequence into the out
    # we can also use dp to solve
