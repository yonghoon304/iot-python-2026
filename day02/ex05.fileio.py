# 파일 입출력 

print("파일 입출력")

# 파일쓰기
## 파일 경로 주의요망!
f = open('./day02/test.txt','w')
f.write("덱스트를 한 줄 씁니다.\n")
f.write("덱스트를 두 줄 씁니다\n")

f.close()

# with를 사용하면 close() 생략가능
# with open("test.txt",'+w') as f:

with open('./day02/test.txt','r') as f:
    content = f.read()
    print(content)
