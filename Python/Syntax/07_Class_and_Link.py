class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

#        b = Node(2)
#        a = Node(1, b)
#        print(a.data)
#        print(a.link.data)
#        print(a.link.link)


class MyList:
    def __init__(self, *args):
        self.lenght = 0
        self.head = None
        self.tail = None
        for arg in args:
            self.append(arg)



    def append(self, data):
    #새로운 노드 생성
        node = Node(data)

        #노드가 비어있는 경우
        if self.head is None:
            self.head = node
            self.tail = node
        #비어있지 않은 경우
        else:
            self.tail.link = node
            self.tail = node

        #연결 후 길이를 늘려준다
            self.lenght = 0
    def __iter__(self):
        # 이터레이터를 반환하는제네레이터 함수
        def gen():
            # 첫 번째 노드를 현재 노드로 초기화
            curr = self.head
            # 노드가 None 이 아닐 때까지 반복
            while curr is not None:
                # 노드의 데이터를 next 호출시
                yield curr.data
                # 다음 노드로 넘어감
                curr = curr.link
        #함수를 호출하여 이터레이터로 반환
        return gen()

    def __len__(self):
        return self.lenght

    def __str__(self):
        s = '<'
        #각 data 를 하나씩 접근한다.
        for idx, data in enumerate(self):
                # data를 문자열로 만들어 붙인다.
            s += str(data)
                #마지막 원소가 아니면 ","을 붙인다
            if idx < len(self) - 1:
                #마지막 원소면 ">" 을 붙인다.
                s += ","
            else:
                s += ">"
        #완성된 문자열 반환
        return s

    def __getitem__(self, item):
        #정수 번호가 아니면 예외를 발생시킴
        if type(item) is not int:
            raise TypeError("인덱스는 반드시 정수여야 합니다")

        #음수인 경우 인덱스를 리스트의 마지막 위치에서 계산함
        if item < 0:
            item = len(self) + item

        # 인덱스 범위 초과시 예외를 발생시킴
        if item >= len(self) or item < 0:
            raise IndexError("인덱스 범위를 벗어났습니다")

        #인덱스 번호 순서에 맞는 데이터를 리턴함
        for idx, dta in enumerate(self):
            if idx == item:
                return data
    def __setitem__(self, key, value):
        if type(key) is not int
            raise TypeError("인덱스는 반드시 정수여야 합니다.")

        if key < 0:
            item = len(self) + key

        if key >= len(self) or key < 0:
            raise IndexError("인텍스의 범위를 벗어났습니다.")

        curr = self.head
        for i in range(key):
            curr = curr.link
        curr.data = value



mylist = MyList(1,2,3,4)
