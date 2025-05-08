#List Comprehension
numbers = range(1, 20)
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")
# >> [4, 16, 36, 64, 100, 144, 196, 256, 324]
# range(시작값, 끝값) 함수는 시작값부터 끝값까지 연속된 값을 호출.
# 이때, (끝값 - 1) 까지만 작동한다. 
# comprehension 코드의 경우 3부분으로 나눌 수 있다. 
# 실행문 for문 if문.
# 복잡해 보이지만, for문, if문, 실행문 순서로 코드를 분석하면 쉽게 이해할 수 있다. 

#Dictionary Comprehension
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths : {word_lengths}")
# >> ‘apple’ : 5, ‘banana’ : 6, ‘cheery’ : 6, ‘data’ : 4

#Set Comprehension
duplicates = [1,2,2,3,4,4,5]
unique_squares = {x ** 2 for x in duplicates}
print(f"Unique squares:  {unique_squares}")
# >> 1, 4, 9, 16, 25
# set comprehension 은 set 성질을 가져와서, 중복된 값을 허용하지 않는다. 