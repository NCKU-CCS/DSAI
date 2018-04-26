from utils import (getStudentsIndex, getRankData, getScore, writeScore)


if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--students',
                        default='studentsData.csv',
                        help='input students data file name')
    parser.add_argument('--rank',
                        default='0424rank.json',
                        help='rank file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()

    index = getStudentsIndex(args.students)
    rankData = getRankData(args.rank)
    score = getScore(index, rankData)
    writeScore(args.output, score)
