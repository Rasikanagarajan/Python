class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[ [] for _ in range(size)]
    
    def hashing(self,key):
        return hash(key)% self.size
    
    def insert(self,key, value):
        index=self.hashing(key)
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i]=(key,value)
            return
        self.table[index].append((key,value))
    def get(self,key):
        index=self.hashing(key)
        for k,v in self.table[index]:
            if k == key:
                return v
            return None
    def delete(self,key):
        index=self.hashing(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
            return False

    def print(self):
        for i, bug in enumerate(self.table):
            if bug:
                print(f"{i},{bug}")        

ha=Hash(10)
ha.insert("Name","indhu")
ha.insert("Name1","mathi")
ha.insert("Name2","rasi")
ha.insert("Name3","vino")
ha.insert("Name4","sai")
ha.insert("Name5","saiprasanna")
ha.insert("Name6","kishor")
ha.insert("Name7","nakul")
ha.print()
ha.delete("name7")
