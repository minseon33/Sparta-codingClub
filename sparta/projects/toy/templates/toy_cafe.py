print("----------<메뉴판>----------")
menu = {'아메리카노':1000 , '카페라떼':1500, '밀크티':2000,'밀크쉐이크':3000,'캐모마일':4000 }
topping = {'샷추가':500,'휘핑크림':1000,'우유추가':1000,'추가안함':0}
menu_stock = {'아메리카노':10 , '카페라떼':15, '밀크티':20,'밀크쉐이크':30,'캐모마일':40 }

for x in menu:
    print(f'     {x} : {menu.get(x)}')

choice_menu = input('메뉴를 입력하세요-> ')

for key, value in menu_stock.items():
    if choice_menu == key:
        if value > 0:
            print("재고가 있습니다.")
        else:
            print("재고가 없습니다.")
    else:
        continue

# for x in menu_index:
#     if choice_menu != x:
#         continue
#     else:
#         print("재고 있습니다.")
