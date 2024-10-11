#quiz5
class RealEstate:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def show_info(self):
        print(f"부동산 정보")
        print(f"위치: {self.location}")
        print(f"평수: {self.size}평")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price} 원")
        print(f"건축 연도: {self.year_built}년")

location = input("부동산 위치를 입력하세요: ")
size = input("평수를 입력하세요: ")
building_type = input("건물 종류를 입력하세요: ")
price = input("가격을 입력하세요: ")
year_built = input("건축 연도를 입력하세요: ")

property1 = RealEstate(location, size, building_type, price, year_built)

property1.show_info()