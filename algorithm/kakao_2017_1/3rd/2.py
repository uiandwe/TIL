https://programmers.co.kr/learn/courses/30/lessons/17683?language=python3

scaleInt = {
    "C#": 'b',
    "C": 'a',
    "D#": 'd',
    "D": 'c',
    "E": 'e',
    "F#": 'g',
    "F": 'f',
    "G#": 'i',
    "G": 'h',
    "A#": 'k',
    "A": 'j',
    "B": 'l'
}


def scaleToInt(scale):

    for i in scaleInt.keys():
        scale = scale.replace(i, scaleInt[i])

    return scale


def timeToInt(time):
    str = time.split(":")
    return int(str[0])*60+int(str[1])


def playToScoreByTime(startTime, endTime, score):
    playTime = timeToInt(endTime) - timeToInt(startTime)
    playScale = []
    score = list(score)

    for j in range(playTime):
        tempScore = score.pop(0)
        playScale.append(tempScore)
        score.append(tempScore)
    return playScale


def solution(m, musicinfos):
    answer = ''
    answerArray = []
    m = ''.join(scaleToInt(m))

    musics = []
    for i in musicinfos:
        temp = i.split(",")
        score = temp[3]
        temp[3] = ''.join(scaleToInt(score))
        temp.append(''.join(playToScoreByTime(temp[0], temp[1], temp[3])))
        musics.append(temp)

    for i in musics:
        if m in i[4]:
            answerArray.append(i)

    if len(answerArray) == 0:
        answer = None
    elif len(answerArray) == 1:
        answer = answerArray[0][2]
    else: # 같은게 두개 이상이면
        count = 0
        playTime = 0
        tempAnswerIndex = []
        for i in range(len(answerArray)):
            if playTime >= len(answerArray[i][4]):
                playTime = len(answerArray[i][4])
                count += 1
                tempAnswerIndex.append(i)

        answer = answerArray[tempAnswerIndex[0]][2]

    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
