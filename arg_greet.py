def greet(*args):
    for name in args:
        print('안녕하세요', name, '씨')
greet('홍길동', '양만춘', '이순신')
greet('James', 'Thomas')