class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        if len(digits) == 0:
            return []
        
        
        
        letterHash = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
            }
        
        def dfsHelper(i,word):
            
            if len(word) == len(digits):
                result.append("".join(word))
                return 
            
            curLetters = letterHash[digits[i]]
            
            for k in curLetters:
                
                word.append(k)
                
                dfsHelper(i+1,word)
                
                word.pop()      
                
        result = []
        dfsHelper(0,[])
        return result