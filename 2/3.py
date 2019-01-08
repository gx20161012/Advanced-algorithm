class Node(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class LinkList():
    def __init__(self):
        self.head=Node(" ")
        self.length=0

    def initlist(self,data):
        self.data=data
        self.length=len(data)
        p=self.head
        for i in data:
            node=Node(i)
            p.next=node
            p=p.next
    def reverse(self,k):
        if self.length < k:
            return self.head
        else:
            p=self.head
            f=p.next
            s=f.next
            time=self.length // k
            m=0
            while m<time:
                m +=1
                for j in range(k-1):

                    f.next=s.next
                    s.next=p.next
                    p.next=s
                    s=f.next
                if s!= None:
                    p=f
                    f=s
                    s=f.next
    def myprint(self):
        p=self.head
        while p.next!=None:
            p = p.next
            if p.next == None:
                print(p.value)
            else:
                print(p.value,end=" ")
while True:
    try:
        input_ls=input().strip().split()
        count=input_ls[0]
        num_ls=input_ls[1:-1]
        k=int(input_ls[-1])

        lk=LinkList()
        lk.initlist(num_ls)
        lk.reverse(k)
        lk.myprint()
        del lk
    except:
        break