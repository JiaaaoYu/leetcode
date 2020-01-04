class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        lookup = {}
        for word in dict:
            tree = lookup
            for c in word:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]
            tree['end'] = True
        
        def helper(word):
            tree = lookup
            for i, c in enumerate(word):
                if 'end' in tree:
                    return word[:i]
                elif c not in tree:
                    break
                tree = tree[c]
            
            return word
        
        return ' '.join(map(helper, sentence.split(' ')))