"""
  Project: Homework 11.4
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 24, 2021
  Detail: 학생 정보를 검색할 수 있는 해시맵을 구현하고, 검색하고 출력하는
          프로그램을 작성
"""

class Entry:
    def __init__(self, k, v):
        self._key = k
        self._value = v
    def __str__(self):
        return str(self.value)

class Bucket(Entry):
    def __init__(self):
        self._bucket = []
    def _getitem(self, k):
        for item in self._bucket:
            if k == item._key:
                return item._value
        return None
    def _setitem(self, k, v):
        for item in self._bucket:
            if k == item._key:
                item._value = v
                return
        self._bucket.append(Entry(k, v))
    # def _delitem(self, k):
    #     for j in range(len(self.bucket)):
    #         if k == self._bucket[j]._key:
    #             self._bucket.pop(j)
    #             return 1
    #     return None
    def __len__(self):
        return len(self._bucket)
    def __iter__(self):
        for item in self._bucket:
            yield item._key

def CyclicShiftHashCode(str_key):
    mask = (1 << 32) -1
    h = 0
    for ch in str_key:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(ch)
    return h

class HashMap_Bucket(Bucket):
    def __init__(self, table_size = 7, prm = 109345121):
        self._hash_tbl = table_size * [None]
        self._hash_tbl_size = table_size
        self._num_entry = 0
        self._prime = prm
    def _hash_value(self, k):
        return CyclicShiftHashCode(k) % self._prime % self._hash_tbl_size
    def __len__(self):
        return self._num_entry
    def _getitem(self, k):
        hv = self._hash_value(k)
        bucket = self._hash_tbl[hv]
        if bucket is None:
            return hv, None
        return hv, bucket._getitem(k)
    def _setitem(self, k, v):
        hv = self._hash_value(k)
        if self._hash_tbl[hv] is None:
            self._hash_tbl[hv] = Bucket()
        bucket = self._hash_tbl[hv]
        bucket._setitem(k, v)
    def __str__(self):
        s = ''
        for h in range(len(self._hash_tbl)):
            bucket = self._hash_tbl[h]
            if bucket is not None:
                s += "bucket[{:2}] : ".format(h)
                for item in bucket:
                    s += str(item) + ", "
                s += "\n "
        return s

def main():
    print("Creating a HashMap of capacity (7)")
    hsMap = HashMap_Bucket()
    L_students = [
        ('Kim', 19345, 'ICE', 4.0),
        ('Park', 18234, 'CS', 4.2),
        ('Hong', 20456, 'EE', 3.9),
        ('Lee', 20987, 'ME', 3.8),
        ('Yoon', 21654, 'ICE', 3.7),
        ('Moon', 21001, 'CHEM', 4.1),
        ('Hwang', 21123, 'CE', 3.7),
        ('Choi', 19003, 'EE', 4.3),
        ('Yeo', 20234, 'ME', 3.8),
        ('Jeong', 18005, 'PH', 4.3),
    ]

    for i in range(len(L_students)):
        st = L_students[i]
        st_key = st[0]
        hsMap._setitem(st_key, st)
        print("Entry[{:2}] : {}".format(i, st))
    
    print("Current HashMap Internal Structure:\n", hsMap)
    
    print("Checking entry searching in HashMap")
    while True:
        key = input("Input student name to search (. to quit) : ")
        if key == '.':
            break
        hv, value = hsMap._getitem(key)
        print("key({}) => hash_tbl[{}]".format(key, hv))
        s ="key ({}) ".format(key)
        if value == None:
            s += "is not found in hashmap !!"
        else:
            s += ": Value ({})".format(value)
        print(s)

if __name__ == "__main__":
    main()