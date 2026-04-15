class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        l=[]
        products.sort()
        for i in range(len(searchWord)):
            l.append([item for item in products if item.startswith(searchWord[:i+1])][:3])
        return(l)