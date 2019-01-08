class Node(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class LinkList():
    def __init__(self):
        self.head=Node(" ")
        self.copy_head = Node(" ")
    def initlist(self,data):
        self.data=data
        p=self.head
        for i in data:
            node=Node(i)
            p.next=node
            p=p.next
    def reverse(self):
        p=self.head
        f=p.next
        s=f.next
        while f.next != None:

            f.next=s.next
            s.next=p.next
            p.next=s
            s=f.next
    def mycopy(self):
        ls=self.data
        p=self.copy_head
        for i in ls:
            node = Node(i)
            p.next = node
            p = p.next
    def huiwen(self):
        p=self.head
        q=self.copy_head
        flag=True
        while p.next != None:
            p=p.next
            q=q.next
            if p.value != q.value:
                flag=False
                break
        if flag:
            return "true"
        else:
            return "false"

while True:
    try:
        input_ls=input().strip().split()
        num=input_ls[1:]

        link = LinkList()
        link.initlist(num)
        link.mycopy()
        link.reverse()
        print(link.huiwen())
        del link
    except:
        break

# ls=[]
# while True:
#     input_ls = input().strip().split()
#     if len(input_ls) == 0:
#         break
#     num = input_ls[1:]
#     ls.append(num)
#
# for i in ls:
#     link=LinkList()
#     link.initlist(i)
#     link.mycopy()
#     link.reverse()
#     print(link.huiwen())
#     del link
