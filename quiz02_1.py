score1 = int(input())
score2 = int(input())

if score1 >=50 and score2>=50 and (score1+score2)/2>=60:
    print('합격')
else:
    print('불합격')