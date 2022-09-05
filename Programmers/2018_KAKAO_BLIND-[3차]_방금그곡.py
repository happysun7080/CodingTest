### level 2 ###

# 1차: 220905

'''
2018 KAKAO BLIND RECRUITMENT - [3차] 방금그곡 (17683)
'''


def getMelody(m):
    shap = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'E#': 'e'}
    size = len(m)
    melody = []
    for i in range(size):
        if m[i] != '#':
            if i+1 >= size:
                melody.append(m[i])
            elif m[i+1] == '#':
                melody.append(shap[m[i:i+2]])
            else:
                melody.append(m[i])
    return ''.join(melody)


def getFullMelody(m, t):
    melody = []
    i = 0
    for _ in range(t):
        if i+1 > len(m):
            i = 0
        melody.append(m[i])
        i += 1
    return ''.join(melody)


def getTime(s, e):
    start_h, start_m = map(int, s.split(':'))
    end_h, end_m = map(int, e.split(':'))

    start = start_h * 60 + start_m
    end = end_h * 60 + end_m
    return end - start


def solution(m, musicinfos):
    melody_neo = getMelody(m)
    music_list = []

    for i, musicinfo in enumerate(musicinfos):
        infos = musicinfo.split(',')
        name = infos[2]
        time = getTime(infos[0], infos[1])
        melody = getMelody(infos[3])
        if time > len(melody):
            melody = getFullMelody(melody, time)
        else:
            melody = melody[:time]
        music_list.append([i, name, time, melody])

    print(music_list)
    answer = []
    for music in music_list:
        if melody_neo in music[3]:
            answer.append([music[0], music[1], music[2]])

    if not answer:
        return '(None)'

    answer.sort(key=lambda x: (-x[2], x[0]))
    return answer[0][1]


# print(solution("ABCDEFG", [
#     "12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", [
#     "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", [
#     "12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
