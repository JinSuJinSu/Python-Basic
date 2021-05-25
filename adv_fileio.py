# action : r(읽기:default), w(쓰기), a(추가)
# type : t(텍스트:default), b(바이너리)
import pickle


def write01():
    f = open(r'C:\sample\test.txt', 'w', encoding='UTF-8')
    write_size = f.write("Life is too short, you need Python")
    print(write_size)
    f.close()


def write02():
    f = open(r'C:\sample\multilines.txt', 'w', encoding='UTF-8')

    for i in range(10):
        f.write("Line %d\n" % i)

    print(f)

    f.close()


def read01():
    f = open(r'C:\sample\multilines.txt', 'r', encoding='UTF-8')
    text = f.read()
    print(text)
    f.close()


def read02():
    f = open(r'C:\sample\multilines.txt', 'r', encoding='UTF-8')
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

    f.close()


def read03():
    f = open(r'C:\sample\multilines.txt', 'r', encoding='UTF-8')
    lines = f.readlines()

    for line in lines:
        print(line)

    f.close()


def copy_binary():
    f_src = open(r'C:\sample\rose-flower.jpeg', 'rb')
    data = f_src.read()
    print(type(data))
    f_src.close()

    f_dest = open(r'C:\sample\rose-flower-copy.jpeg', 'wb')
    f_dest.write(data)
    f_dest.close()


def pickle_dump():
    with open(r'C:\sample\players.bin', 'wb') as f:
        data = {'baseball': 9}
        pickle.dump(data, f)
    print('덤프 완료')


def pickle_load():
    #개체 역직렬화 : 2진 데이터 -> 파이썬 객체로 복원
    with open(r'C:\sample\players.bin', 'rb') as f:
        data = pickle.load(f)
        print(data, type(data))
    print('로드 완료')

def pickle_dump_multi():
    # dump 메서드를 중복 실행하면 여러 객체를 dump 가능
    with open(r'C:\sample\players.bin', 'wb') as f:
        pickle.dump({'baseball':9}, f, 1) # 프로토콜의 버전 명시 가능 버전 1
        pickle.dump({'basketball':5},f, 2) # 프로토콜 버전 2
        pickle.dump({'horse_riding': 7}, f, pickle.HIGHEST_PROTOCOL) # 가장 최신의 프로토콜
        pickle.dump({'soccer':11},f) # 프로토콜 명시를 안하면 가장 최신 버전 실행

    print('중복 덤프 완료됬음')

def pickle_load_multi():
    with open(r'C:\sample\players.bin', 'rb') as f:
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))


def pickle_easy_load_multi():
    # EOF 에러가 발생할 때까지 loop를 돌면서 load

    with open(r'C:\sample\players.bin', 'rb') as f:
        data_list = []

        while True:
            try:
                data = pickle.load(f)
            except EOFError:  # 더 이상 읽을 피클이 없다
                break
            data_list.append(data)

    print(data_list)

def slamdunk_read():
    # sangbuk.csv
    # 한 줄 단위로 읽은 후 dict, list 후에 pickle에 덤프

    players = []

    with open(r'C:\sample\sangbuk.csv', 'rt',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            # 읽은 데이터를 사전화 시킨다
            line = line.strip().replace(' ','')
            info = line.split()

            member = {'name': info[0],'backno': info[1],'height': info[2],'position': info[3],}

            players.append(member)

        print(players)

        with open(r'C:\sample\sangbuk_players_bin', 'wb') as f:
            pickle.dump(players,f)

        print('피클 덤프 완료')





if __name__ == '__main__':
     write01()
    # write02()
    # read01()
    # read02()
    # read03()
    # copy_binary()
    # pickle_dump()
    # pickle_load()
    # pickle_dump_multi()
    # pickle_load_multi()
    # pickle_easy_load_multi()
    # slamdunk_read()
