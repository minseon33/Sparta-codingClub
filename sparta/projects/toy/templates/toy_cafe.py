
menu = {'아메리카노':1000 , '카페라떼':1500, '밀크티':2000,'밀크쉐이크':3000,'캐모마일':4000 }
topping = {'샷추가':500,'휘핑크림':1000,'우유추가':1000,'추가안함':0}
menu_stock = {'아메리카노':10 , '카페라떼':15, '밀크티':20,'밀크쉐이크':30,'캐모마일':40 }
cafe_amount = 0
final_buy = False



while True:
# 새로운 손님 올 때마다 초이스는 초기화
    choice_menu = ''
    choice_topping = ''
    final_buy = False
    user_money = 0
    payment  = 0

    # 메뉴판 출력
    print("----------<메뉴판>----------")
    for x in menu:
        print(f'     {x} : {menu.get(x)}')
# 고객님 메뉴입력
    choice_menu = input('메뉴를 입력하세요-> ')
# 메뉴 이름 바르게 입력되었는지 확인
    if choice_menu not in menu:
        print("메뉴이름을 바르게 입력해주세요.")
        break
# 재고 확인하기
    for key, value in menu_stock.items():
        if choice_menu == key:
            if value > 0:
                print("재고가 있습니다.")
                # 최종 금액에 선택한 메뉴 금액 집어넣기
                payment += menu[choice_menu]
                print(f'payment : {payment}')
            else:
                print("재고가 없습니다.")
                break
        else:
            continue
# 토핑추가 확인
    topping_check = input('토핑을 추가하시겠습니까? Y or N-> ')
    if topping_check.upper() == "Y":
        for x in topping:
            print(f'     {x} : {topping.get(x)}')
        choice_topping = input('추가할 토핑을 입력하세요-> ')
        # 최종 금액에 선택한 토핑 집어넣기
        payment += topping[choice_topping]
        print(f'payment : {payment}')

    elif topping_check.upper() == "N":
        print("토핑을 추가하지 않습니다.")
    else:
        print("Y 또는 N로 입력해주세요.")
        choice_topping = input('추가할 토핑을 입력하세요-> ')

    # 결제확인
    buy_check = input('결제하시겠습니까? Y or N-> ')

    if buy_check.upper() == "Y":
        final_buy = True

    elif buy_check.upper() == "N":
        final_buy = False
        print("결재를 취소합니다. 처음으로 돌아갑니다.")
        break
    else:
        print("Y 또는 N로 입력해주세요.")
        buy_check = input('결제하시겠습니까? Y or N-> ')

    # 결제진행
    if final_buy == True:
        user_money = int(input('현금을 숫자로만 입력해주세요.-> '))

        if user_money >= payment:
            print("결제가 완료되었습니다.")
            #카페 매상 올리기
            cafe_amount += payment
            # 재고 빼기
            c = {f'{choice_menu}': menu_stock[choice_menu] - 1}
            menu_stock.update(c)
            print(f'현재 재고 : {menu_stock}')
            print(f'카페 총 매출 : {cafe_amount}')
        else:
            print("잔액이 부족합니다.")
            print("결제가 완료 되지 못했습니다.")
            print(f'현재 재고 : {menu_stock}')
            print(f'카페 총 매출 : {cafe_amount}')




