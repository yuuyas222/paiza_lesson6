# coding:UTF-8

# 2次元リスト
player = "忍者"
team =[player ,"勇者","戦士","魔法使い"]

# print(team)

team_a =[player ,"勇者","戦士","魔法使い"]
team_b = [team[0],team[1],team[2],team[3]]
team_c = ["ドラゴン","スライム","魔王","うんち"]
teams = [team_a,team_b, team_c] #二次元リスト
# print(team_b)
# print(teams[1])
# print(teams[1][2])
print(teams)
# print(teams[0])
# print(teams[0][0])
# print(teams[0][1])
# print(teams[0][2])

teams[0][0] = "魔道士"
print(teams)
print(len(teams[1]))

# int = int(input())
# print(teams[int])

teams.append(["unnti","metal","dragon"])
print(teams)

