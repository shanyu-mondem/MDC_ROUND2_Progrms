def CombinationSum(candidates, target):
    All_combinations, combination = [], []
    
    def backtrack(i,  total):
        if total == target:
            All_combinations.append(combination[:])
            return
        if total > target or i == len(candidates):
            return
        
        backtrack(i+1, total)
        combination.append(candidates[i])
        backtrack(i, total+candidates[i])
        combination.pop()
        
    backtrack(0, 0)
    return All_combinations
    
Candidates = list(map(int, input().strip().split()))
Target = int(input())
All_Combinations_Target = CombinationSum(Candidates, Target)
print(All_Combinations_Target)