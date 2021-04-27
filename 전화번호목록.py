class Book:
    #init을 갖고 있으면 객체 생성될 때 자동으로 호출되는 함수가 있는 것을 생성자라고 함
    #정보 입력 받고 저장 O
    #성별 조건 지정 O
    #이름에 그만 입력 시 입력 중단 O
    #입력 완료 시마다 이전에 입력해둔 정보들 출력 O
    #입력 중단 시, 전체 정보 목록 출력 O
    #프로그램 종료 O
    def __init__(self, name, phone, sex):
        self.name=name
        self.phone=phone
        self.sex=sex
        if sex != 'male':
            if sex != 'female':
                self.sex='unkown'

    def save(self):
        sen='이름은 '+self.name+', 전화번호는 '+self.phone+', 성별은 '+self.sex+'입니다.'
        return sen

cnt=0

myList=list()   #리스트 생성 

while True:
    name=input('이름 입력하세요: ')
    if name=='그만':
        for i in myList[:cnt]:
            print(i)
        break
    phone=input('전화번호 입력하세요: ')
    sex=input('성별 입력하세요(male or female): ')
    user=Book(name,phone,sex)
    myList.append(user.save())
    cnt+=1
    for i in myList[:cnt]:
        print(i)