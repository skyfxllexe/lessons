n = int(input())
resultSet = set([i for i in range(1,n+1)])
while True:
    string = input()
    if string == 'HELP':
        print(*(sorted(resultSet)))
        break
    array = set(map(int, string.split()))
    answer = input()
  
    if answer == 'YES':
        resultSet &= array
    if answer == 'NO':
        resultSet -= array





