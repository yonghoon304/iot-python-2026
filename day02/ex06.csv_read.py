# csv read

with open("./day02/부산시_해운대구_도서정보.csv",'r',encoding='UTF-8') as f :
    # line = f.read()
    for line  in f:
        print(line.strip()) # \n 줄바꿈 제거