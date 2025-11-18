class merge_sort:
    def __init__(self,data):
        self.data=data
 
    def sort(self):
        if len(self.data)>1:
            self._merge(self.data)
    def _merge(self,arr):
        if len(arr)>1:
            mid=len(arr)//2;
            left=arr[:mid]
            right=arr[mid:]
 
            self._merge(left)
            self._merge(right)
 
            i=j=k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
    def sorted(self):
        return self.data
num=[67,34,9,28,19,78]
s=merge_sort(num)
print(s.sorted())
s.sort()
print(s.sorted())
 