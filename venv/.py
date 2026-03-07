def show_calendar():
    print("\n---SmartManajer Календары ---")
    print("Бугунку дата :2026-жыл,26-Февраль")
    print("Жакынкы иш-чаралар: Лабораториялык ишти тапшыруу.")

def add(a,b):
    return a+b
def test_add_success():
    assert add (2,3)==5
def test_add_wrong():
        assert add (2,2)!=5
def get_user_age():
    try:
        age=int(input('введите ваш возраст:'))
        print(f'Ваш возраст: {age}')
    except ValueError:
         print('Ошибка! Пожалуйста ,введите только число,а не буквы.')

if __name__=="__main__":
    show_calendar()
    get_user_age()
          
