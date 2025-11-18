class quick:
    def __init__(self,data):
        self.data=data
    def sort(self):
        self._quicksort(self.data,0,len(self.data)-1)
    def _quicksort(self,arr,low,high):
        if low<high:
            pi=self._partition(arr,low,high)
 
            self._quicksort(arr,low,pi-1)
            self._quicksort(arr,pi+1,high)
    def _partition(self,arr,low,high):
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
   
    def sorted(self):
        return self.data
num=[67,34,9,28,19,78]
s=quick(num)
print(s.sorted())
s.sort()
print(s.sorted())