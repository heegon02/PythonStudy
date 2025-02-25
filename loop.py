#while반복문, break
i = 0
input_text = int(input("반복 횟수 입력 >> "))
while True:
    print(f"{i}번째 반복.")
    i = i + 1
    if i == input_text:
        print("반복 종료")
        break
#break문은 '반복문 탈출'

#continue
numbers = [5, 15, 6, 20, 7, 25]
for number in numbers:
    if number < 10:
        continue
    print(number)

print("-----구분선-----")

for number in numbers:
    if number >= 10:
        print(number)
#두 for문은 같은 결과를 출력한다. 
#continue는 주로 for문 안에서 if문과 함께 사용되며, 
#'해당 조건 생략'이라고 생각하면 쉽다. 