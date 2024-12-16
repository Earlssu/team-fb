for i in range(21):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 15 == 0:
        # 15의 배수일 경우
        print('fizzbuzz')
    else:
        print(i)

