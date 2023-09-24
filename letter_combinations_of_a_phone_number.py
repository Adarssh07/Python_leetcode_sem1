class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone_map={
                '2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'
                    }
        combination=[""]
        for dig in digits:
            n_combi=[]
            for combi in combination:
                for letter in phone_map[dig]:
                    n_combi.append(combi+letter)
            combination=n_combi
        return combination