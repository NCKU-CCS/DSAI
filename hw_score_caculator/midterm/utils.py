import csv
import json

FINAL_DATE = 23
DISCOUNT = 0.93


def getStudentsIndex(studentsFilePath):
    with open(studentsFilePath, 'r') as students:
        students = csv.reader(students, delimiter=',')
        index = dict()
        for row in students:
            index[row[4]] = {
                "teamName": row[4],
                "name": row[2],
                "email": row[1],
                "id": row[3]
            }
        del index['teamName']
        return index


def getRankData(rankFilePath):
    rankJson = json.load(open(rankFilePath))
    return rankJson


def log(date, todayScore, todayWeight, weightScore):
    print('4/' + str(date) + ': ' + str(todayScore) +
          ' - ' + str(todayWeight) +
          ' - ' + str(weightScore)
    )


def getScore(index, rankData):
    for team in rankData['rank']:
        if (team['team_name'] in index):
            print('\n\n' +
                  team['team_name'] + ' - ' +
                  index[team['team_name']]['name']
            )
            total = 0.0
            for date in range(3, FINAL_DATE+1, 1):
                todayScore = float(team['A2018_4_' + str(date)])
                todayWeight = float((DISCOUNT**(23-date)))
                todayWeightScore = todayScore * todayWeight

                log(date, todayScore, todayWeight, todayWeightScore)
                total += todayWeightScore

            finalScore = total / (FINAL_DATE-2)

            print('Total: ' + str(total) + ' - Score: ' + str(finalScore))
            index[team['team_name']]['total'] = total
            index[team['team_name']]['score'] = finalScore

    return index


def writeScore(outputPath, score):
    with open(outputPath, 'w') as output:
        output.write('teamName,name,id,email,total,score\n')
        for student in score:
            output.write(student)
            output.write(',')
            output.write(score[student]['name'])
            output.write(',')
            output.write(score[student]['id'])
            output.write(',')
            output.write(score[student]['email'])
            if ('score' in score[student]):
                output.write(',')
                output.write(str(score[student]['total']))
                output.write(',')
                output.write(str(score[student]['score']))
            output.write('\n')
