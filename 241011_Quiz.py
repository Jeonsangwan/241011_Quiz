name = input("이름을 입력하세요.")
age = input("나이를 입력하세요")
number = input("연락처를 입력하세요.")
class User :
    def __init__(self, name, age, number):
        self.name = name
        self.age = (age)
        self.number = (number)

    def show_info(self):
        print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.number}입니다.")

member = User(name, age, number)
member.show_info()