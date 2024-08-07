#변수
a = 1
b = "python"
c = [1,2,3]
#파이썬에서 변수는 저장된 값을 스스로 판단해 자료형을 지정한다.
#파이썬은 객체지향이다. 파이썬에서의 변수는 객체를 생성하는 것이다.
#c = [1,2,3]을 예로 들면 리스트 자료형인 [1,2,3]이 메모리에 생성되고 변수 c는 저 리스트를 가리키는 변수이다.
print(id(c)) #메모리의 주소 값을 반환하는 함수
d = c #리스트 복사 이렇게 되면 d와 c는 완전히 동일한 변수다. d도 [1,2,3]의 주소를 가리키는 참조 변수가 된다.
print(id(d))
print(c is d) #c와 d가 같은 객체를 가리키는 지 확인하는 명령어인 is를 썼을 떄 True를 반환하게 된다.

c[1] = 4
print(d) #같은 리스트의 주소를 가리키고 있기 때문에 한 곳에서 리스트의 값을 바꾸면 두개 다 바뀌게 된다.

#아예 다른 주소를 가리키도록 복사하기
l1 = [1,2,3]
l2 = l1[:] #슬라이싱 ) 리스트의 처음부터 끝까지
print(l2)

from copy import copy
l1 = [1,2,3]
l2 = copy(l1)
print(l2)
print(l1 is l2) #서로 다른 객체를 가리키고 있기 때문에 False가 뜬다.

#변수 만드는 다양한 방법
a,b = ('python', 'life') #튜플로 a,b의 값을 대입할 수 있다.
(a,b) = 'python', 'life' #첫번째 예문과 같다.
[a,b] = ['python','life'] #리스트로 변수를 만들 수도 있다.
a = b = 'python' #여러 개의 변수에 같은 값을 대입할 수도 있다.

a = 3
b = 5
a, b = b, a #이렇게 두 변수의 값을 바꿀 수 있다.
print(a,b)