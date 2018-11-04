from datetime import datetime

def timeToStamp(t):
    date1 = "2018-01-01 "+t
    return datetime.strptime(date1, "%Y-%m-%d %H:%M").timestamp()+32400 #9시간


def stampToTime(s):
    return datetime.utcfromtimestamp(9).utcfromtimestamp(s).strftime('%H:%M')


def solution(n, t, m, timetable):
    answer = ''
    n = int(n)
    t = int(t)
    m = int(m)
    

    for i in range(len(timetable)):
        timetable[i] = timeToStamp(timetable[i])

    timetable = sorted(timetable)
    # print(timetable)

    successCount = 0
    maxSuccessTime = timeToStamp("23:59")

    for i in range(1,n+1):
        successCount = 0
        maxSuccessTime = timeToStamp("23:59")
        lastTime = timeToStamp("09:00") + (t*(i-1))*60
        loopRange = len(timetable)
        # print(timetable)
        for j in range(loopRange):
            # print(timetable[j] <= lastTime , successCount < m)
            if timetable[j] <= lastTime and successCount < m:
                successCount += 1
                maxSuccessTime = timetable[j]
            else:
                if maxSuccessTime > timetable[j]:
                    maxSuccessTime = timetable[j]

        #성공한 수 제거
        for j in range(successCount):
            timetable.pop(0)

    # print(successCount, maxSuccessTime)
    if successCount < m: #자리가 남는다면 가장 마지막 운행시간을 리턴
        answer = stampToTime(lastTime)
    else: #자리가 없다면 가장 마지막 사람의 바로 앞으로 시간을 조정
        answer = stampToTime(maxSuccessTime-60)

    # print(answer)
    return answer


# solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
# solution(2, 10, 2, ["09:10", "09:09", "08:00"])
# solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
# solution(1, 1, 5, ["00:01","00:01","00:01","00:01","00:01"])
# solution(1, 1, 1, ["23:59"])
# solution(10, 60, 45, ["23:59","23:59","23:59","23:59",
#                       "23:59","23:59","23:59","23:59",
#                       "23:59","23:59","23:59","23:59",
#                       "23:59","23:59","23:59","23:59"])
# solution(1, 1, 1, ["00:01"])
