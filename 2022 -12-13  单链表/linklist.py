class ListNode:                             #定义一个节点类
    def  __init__(self,val):                #self代表函数本身，这里不用细究，init为一个构造函数
        self.val = val                      #val代表节点中的数值域
        self.next = None                    #next是指针域，指向下一个节点的位置

class linklist:                             #定义链表类
    def __init__(self):
        self.size = 0                       #初始链表的大小为0
        self.head = ListNode(0)             #listnode为节点类创建的对象，head头指针指向第一个节点

#获取链表中第index个节点的值，若索引无效，返回-1
    def get(self,index:int) -> int:          #第一个int为传入参数的类型，第二个为返回值的类型
        if index < 0 or index >= self.size:  #index为获取对应索引的元素，如链表的第3个位置存了一个5，则linklist.get(3),会返回5
            return -1                        #若输入的索引小于0或大于链表的长度，则返回-1
        cur = self.head                      #cur首先指向链表的头节点，cur此时就是头节点
        for _ in range(index+1):             #循环遍历到索引对应的元素
            cur = cur.next                   #cur的指针域指向下一个节点，cur自己的指针next指向自己的子节点（下一节点）
        return cur.val                       #返回索引的值

#头插法
    def addhead(self,val:int) -> None:       #传入参数类型为int,无返回类型
        self.addIndex(0,val)                 #在链表的第一个结点之前插入值为val的节点（也就是头节点之后）

#尾插法
    def addtail(self,val:int) -> None:       #传入参数类型为int,无返回类型
        self.addIndex(self.size,val)         #将值为val的节点插入链表的末尾

#具体插入实现
    def addIndex(self,index:int, val:int) ->None:
        if index > self.size:                #若索引大于链表的长度，则不会插入节点，无返回值
            return
        index = max(0,index)                 #若索引等于链表的长度
        self.size += 1                       #将插入的节点放在链表末尾，链表长度+1
        pred = self.head                     #前驱节点指向链表的头节点
        for _ in range(index):               #循环遍历到索引前面一个元素
            pred = pred.next                 #pred头节点指向下一个节点
        to_add = ListNode(val)               #添加值为val的节点
        to_add.next = pred.next              #将头节点后的第一个节点赋给插入的结点之后
        pred.next = to_add                   #将插入的节点放在头节点之后

#删除节点
    def deleteIndex(self,index:int) ->None:
        if index < 0 or index > self.size:   #若输入的索引小于0或大于链表的长度，则返回-1
            return
        self.size -= 1                       #删除后链表长度-1
        pred = self.head                     #pred指向链表的头节点
       #循环遍历重新连接链表
        for _ in range(index):            
            pred = pred.next                   
            pred.next = pred.next.next

lk = linklist.addhead(0,2)
print(lk)
