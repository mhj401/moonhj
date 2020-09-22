import random

select_m = ['한식','일식','중식','양식','기타']
k_food = ['비빔밥','제육덮밥','김치찌개','된장찌개','냉면','돼지불백','칼국수','수제비','부대찌개','고등어조림','보쌈','뼈해장국','순대국']
j_food = ['초밥','우동','스끼야끼','냉모밀','냉우동','도미조림','규동','가츠동','오니기리','라멘','오야꼬동']
c_food = ['짜장면','짬뽕','탕수육','마파두부','깐풍기','라조기','마라탕','마라샹궈','고추잡채','볶음밥','양장피']
w_food = ['오믈렛','오므라이스','스테이크','햄버거','치킨커틀릿','포크커틀릿','까르보나라','비프스튜','토마토파스타','바베큐폭립']
etc_food = ['순대','떡볶이','김밥','라면','쌀국수','분짜','인도커리','팟타이','슈바인학센','다이어트는 어때...?','삼각김밥','편의점 도시락']


menu = []
def RandLunch():
    while True:
        ko = random.sample(k_food, 5)
        ja = random.sample(j_food, 5)
        ch = random.sample(c_food, 5)
        we = random.sample(w_food, 5)
        etc = random.sample(etc_food, 5)

        if '한식' == menu:
            print(ko)
            break

        elif '일식' == menu:
            print(ja)
            break

        elif '중식' == menu:
            print(ch)
            break

        elif '양식' == menu:
            print(we)
            break

        elif '기타' == menu:
            print(etc)
            break

def ReTry(): #다시뽑기 버튼
    while True:
        if '다시뽑기':
            RandLunch()

        else:
            print("프로그램을 종료합니다.")
            break

RandLunch()
ReTry()