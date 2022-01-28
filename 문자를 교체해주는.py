# 문자를 교체해주는 문제
word = "English"
letter ="li"

# 결과 출력 : EngliSH

before= word[:word.find(letter)]
after = word[word.find(letter)+len(letter):]
result = before + letter.upper() + after

print(result)
#결과출력 EnglSH
