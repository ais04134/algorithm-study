# -*- coding: utf-8 -*-
'''

방금그곡
라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다. 그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다.
그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다. 반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다. 그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
음악이 00:00를 넘겨서까지 재생되는 일은 없다.
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
입력 형식
입력으로 네오가 기억한 멜로디를 담은 문자열 m과 방송된 곡의 정보를 담고 있는 배열 musicinfos가 주어진다.

m은 음 1개 이상 1439개 이하로 구성되어 있다.
musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.
음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.
출력 형식
조건과 일치하는 음악 제목을 출력한다.

입출력 예시
m	musicinfos	answer
"ABCDEFG"	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"HELLO"
"CC#BCC#BCC#BCC#B"	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	"FOO"
"ABC"	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"WORLD"
설명
첫 번째 예시에서 HELLO는 길이가 7분이지만 12:00부터 12:14까지 재생되었으므로 실제로 CDEFGABCDEFGAB로 재생되었고, 이 중에 기억한 멜로디인 ABCDEFG가 들어있다.
세 번째 예시에서 HELLO는 C#DEFGABC#DEFGAB로, WORLD는 ABCDE로 재생되었다. HELLO 안에 있는 ABC#은 기억한 멜로디인 ABC와 일치하지 않고, WORLD 안에 있는 ABC가 기억한 멜로디와 일치한다.

'''

m = "CCB"
musicinfos = ["03:00,03:10,FOO,CC#BCCB", "04:00,04:08,BAR,ABC"]
#
# def solution(m, musicinfos):
#     same_pitch = []
#     m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
#     for i in musicinfos:
#         music_info = i.split(',')
#         music_info[-1] = music_info[-1].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
#         time_1 = music_info[0][:2]*60+music_info[0][3:5]
#         time_2 = music_info[1][:2]*60+music_info[1][3:5]
#         time = int(time_2) - int(time_1)
#         music_info[-1] = music_info[-1]*((time//len(music_info[-1]))+1)
#         if music_info[-1].find(m) != -1:
#             same_pitch.append(music_info)
#
#     if same_pitch == []: return "(None)"
#     else:
#         same_pitch_time = []
#         for z in same_pitch:
#             time_1 = z[0][:2] * 60 + z[0][3:5]
#             time_2 = z[1][:2] * 60 + z[1][3:5]
#             time = int(time_2) - int(time_1)
#             same_pitch_time.append(time)
#         answer = same_pitch_time.index(max(same_pitch_time))
#         return same_pitch[answer][2]
#
#
# print(solution(m,musicinfos))



import itertools

def solution(m, musicinfos):
    same_pitch = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    for i in musicinfos:
        music_info = i.split(',')
        music_info[-1] = music_info[-1].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        time_1 = music_info[0][:2]*60+music_info[0][3:5]
        time_2 = music_info[1][:2]*60+music_info[1][3:5]
        time = int(time_2) - int(time_1)
        music_info.append(time)
        emp_pool = itertools.cycle(music_info[-2])
        if time > len(music_info[-2]):
            for _ in range(time-len(music_info[-2])):
                music_info[-2] = music_info[-2] + next(emp_pool) # 반복자를 통하여 재생된 시간만큼 멜로디 추가
                print(music_info)
        if music_info[-2].find(m) != -1:
            same_pitch.append(music_info)
    if same_pitch == []:
        return "(None)"
    else:
        answer = max(same_pitch, key=lambda x: x[-1])[2]
        return answer



def solution(m, musicinfos):
    same_pitch = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    for i in musicinfos:
        music_info = i.split(',')
        music_info[-1] = music_info[-1].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        time_1 = music_info[0][:2]*60+music_info[0][3:5]
        time_2 = music_info[1][:2]*60+music_info[1][3:5]
        time = int(time_2) - int(time_1)
        music_info.append(time)
        if time > len(music_info[-2]):
            music_info[-2] = music_info[-2]*(time//len(music_info[-2])) + music_info[-2][:time% len(music_info[-2]) +1]
        if m in music_info[-2]:
            same_pitch.append(music_info)
    if same_pitch == []:
        return "(None)"
    elif len(same_pitch) == 1:
        return same_pitch[0][2]
    else:
        return sorted(same_pitch, key=lambda x: x[-1])[2] # 용의 천재적인 한줄

# emp_pool ~~ 이런식으로 처리해준걸 다르게 처리해야되나?... 이게 시간 복잡도가 매우 높은가 싶기도하고
print(solution(m,musicinfos))


def solution(m, musicinfos):
    dic = {}
    # 사용되는 음이 아닌 문자로 변환
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    for info in musicinfos:
        # 콤마를 기준으로 변수에 저장
        start, end, title, music = info.split(',')
        start = [int(i) for i in start.split(':')]
        end = [int(i) for i in end.split(':')]
        # 끝난시각-시작시간을 분단위로 저장
        time = (end[0] - start[0]) * 60 + (end[1] - start[1])
        music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        # 몫, 나머지를 이용해 실제로 재생된 멜로디 저장
        music = music * (time // len(music)) + music[:time % len(music) + 1]
        dic[title] = music

    answer = ["", ""]
    for key, value in dic.items():
        if m in value:
            if len(answer[1]) < len(value):
                answer[0] = key
                answer[1] = value

    return "(None)" if len(answer[0]) == 0 else answer[0]  # 내 코드랑 거진 유사한데 시간 복잡도가 낮다...
