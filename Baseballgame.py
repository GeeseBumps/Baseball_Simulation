import random
import math
class ScoreBoard:
    def __init__(self):
        self.inning = 1
        self.outcount = 0
        self.score = 0
        self.base = [0,0,0]

    def getinning(self):
        return self.inning
    def getoutcount(self):
        return self.outcount
    def getscore(self):
        return self.score
    def getbase(self):
        return self.base
    def clearoutcount(self):
        self.outcount = 0
    def clearbase(self):
        self.base = [0,0,0]
    def addscore(self,n):
        self.score = self.score + n
    def addinning(self):
        self.inning = self.inning + 1
        self.clearbase()
        self.clearoutcount()
    def baserule(self,n):
        if n==0: #out
            self.outcount = self.outcount + 1
        elif n==1:
            if self.base == [0,0,0]:
                self.base = [1,0,0]
            elif self.base == [0,0,1]:
                self.base = [1,0,0]
                self.addscore(1)
            elif self.base == [1,0,0]:
                self.base = [1,1,0]
            elif self.base == [1,0,1]:
                self.base = [1,1,0]
                self.addscore(1)
            elif self.base == [0,1,0]:
                self.base = [1,0,1]
            elif self.base == [1, 1, 0]:
                self.base = [1,1,1]
            elif self.base == [1, 1, 1]:
                self.addscore(1)
                self.base=[1,1,1]
            elif self.base == [0,1,1]:
                self.addscore(1)
                self.base = [1,0,1]

        elif n==2: #2hit
            if self.base == [0,0,0]:
                self.base = [0,1,0]
            elif self.base == [0,0,1]:
                self.base = [0,1,0]
                self.addscore(1)
            elif self.base == [1,0,0]:
                self.base = [0,1,1]
            elif self.base == [1,0,1]:
                self.base = [0,1,1]
                self.addscore(1)
            elif self.base == [0,1,0]:
                self.addscore(1)
            elif self.base == [1, 1, 0]:
                self.base = [0,1,1]
                self.addscore(1)
            elif self.base == [1, 1, 1]:
                self.addscore(2)
                self.base=[0,1,1]
            elif self.base == [0, 1, 1]:
                self.addscore(2)
                self.base = [0,1,0]

        elif n == 3:  # 3hit
            self.addscore(sum(self.base))
            self.base = [0,0,1]
        elif n == 4:  # hr
            self.addscore(sum(self.base) + 1)
            self.clearbase()
        elif n == 5:  # 4ball
            if self.base[0] == 0:
                self.base[0] = 1
            elif self.base == [1, 0, 0]:
                self.base = [1,1,0]
            elif self.base == [1, 1, 0]:
                self.base = [1,1,1]
            elif self.base == [1, 1, 1]:
                self.addscore(1)
            elif self.base == [1, 0, 1]:
                self.base = [1,1,1]


players1 = [[0.285, 0.331, 0.331, 0.339, 0.387,1],[0.247,0.275,0.283,0.287,0.336,1],[0.284,0.328,0.331,0.343,0.443,1]
,[0.253,0.311,0.312,0.344,0.501,1],[0.281,0.364,0.365,0.387,0.484,1],[0.236,0.291,0.293,0.306,0.431,1]
,[0.201,0.234,0.237,0.248,0.345,1],[0.185,0.230,0.242,0.246,0.310,1],[0.263,0.314,0.314,0.320,0.419,1]]#원래 순서

players2 = [[0.285, 0.331, 0.331, 0.339, 0.387, 1], [0.247, 0.275, 0.283, 0.287, 0.336, 1],
            [0.284, 0.328, 0.331, 0.343, 0.443, 1]
    , [0.253, 0.311, 0.312, 0.344, 0.501, 1], [0.281, 0.364, 0.365, 0.387, 0.484, 1],
            [0.236, 0.291, 0.293, 0.306, 0.431, 1]
    , [0.201, 0.234, 0.237, 0.248, 0.345, 1], [0.185, 0.230, 0.242, 0.246, 0.310, 1],
            [0.263, 0.314, 0.314, 0.320, 0.419, 1]]

players2 = [[0.285, 0.331, 0.331, 0.339, 0.387,1],[0.247,0.275,0.283,0.287,0.336,1],[0.284,0.328,0.331,0.343,0.443,1]
,[0.253,0.311,0.312,0.432,0.569,1],[0.281,0.364,0.365,0.387,0.484,1],[0.236,0.291,0.293,0.306,0.431,1]
,[0.201,0.234,0.237,0.248,0.345,1],[0.185,0.230,0.242,0.246,0.310,1],[0.263,0.314,0.314,0.320,0.419,1]]
#4번타자의 장타율이 엄청 높을 때(우리나라 최고 기록)

players3 = [[0.285, 0.331, 0.331, 0.339, 0.387,1],[0.247,0.275,0.283,0.287,0.336,1],[0.284,0.328,0.331,0.412,0.492,1]
,[0.253,0.311,0.365,0.412,0.569,1],[0.281,0.364,0.365,0.387,0.484,1],[0.236,0.291,0.293,0.306,0.431,1]
,[0.201,0.234,0.237,0.248,0.345,1],[0.185,0.230,0.242,0.246,0.310,1],[0.263,0.314,0.314,0.320,0.419,1]]
#좋은 타자 두명 있을 때

players4 = [[0.329, 0.383, 0.383, 0.392, 0.442,1],[0.285,0.319,0.327,0.331,0.383,1],[0.345,0.401,0.403,0.417,0.528,1]
,[0.329,0.404,0.406,0.443,0.629,1],[0.342,0.443,0.443,0.468,0.574,1],[0.295,0.362,0.365,0.38,0.522,1]
,[0.243,0.283,0.287,0.299,0.406,1],[0.216,0.267,0.280,0.284,0.353,1],[0.320,0.381,0.381,0.388,0.497,1]]
#모든 타자가 평균적으로 10퍼센트 정도 더 칠 때
p1=[]

for player1 in players4:
    for player2 in players1:
        player=[]
        for i in range(4):
            stat=player2[i]+0.2*(player1[i]-player2[i])
            player.append(stat)
        player.append(player[3]+(player1[4]-player1[3]))
        player.append(1)
        p1.append(player)
print(p1)


players5 = [[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1]
    ,[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1]
            ,[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1]] #장타자

players6 = [[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1]] #단타자

players7 = [[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1]] #장타자1 단타자8

players8 = [[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1]] #장타자2 단타자7

players9 = [[0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],
           [0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1]] #장타자3 단타자 3

players10 = [[0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],
           [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1]] #장타자5 단타자 4

players11 = [[0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],
           [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1]] #장타자4 단타자 5

players12 = [[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],
           [0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1]] #장타자6 단타자 3

players13 = [[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.300,0.340,0.345,0.350,0.450,1],
            [0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],
           [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1]] #장타자7 단타자 2


players14 = [[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],
            [0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],
           [0.300,0.340,0.345,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1],[0.250,0.275,0.300,0.350,0.450,1]] #장타자7 단타자 2

score = 0
scorelist = []
for j in range(10000):
    board = ScoreBoard()
    i = 0
    while board.getinning() != 10:
        if i == 9:
            i = 0
        player = players1[i]
        prob = random.random()
        #print(" ------------------------", board.getinning(), "INNING------------------------")
        #print("Player ", i + 1)
        if prob <= player[0]:  # 1basehit
            board.baserule(1)
            #print("1basehit")
        elif prob <= player[1]:  # 2basehit
            board.baserule(2)
            #print("2basehit")
        elif prob <= player[2]:  # 3basehit
            board.baserule(3)
            #print("3basehit")
        elif prob <= player[3]:  # homerun
            board.baserule(4)
            #print("HomeRun!!!")
        elif prob <= player[4]:  # 4ball
            board.baserule(5)
            #print("4 BAll")
        elif prob <= player[5]:  # out
            board.baserule(0)
            #print("Out")
        i = i + 1
        #print("Base : ", board.getbase(), " Outcount : ", board.getoutcount(), " Score : ", board.getscore(), )
        if board.getoutcount() == 3:
            board.addinning()
#print("GAME OVER")


    scorelist.append(board.getscore())
    score = score + board.getscore()

mean = score/10000
sum=0
for s in scorelist:
    sum+=(s-mean)*(s-mean)
var = sum/9999
std = math.sqrt(var)
print("Mean : ", mean, " Standard deviation :", std, " Number of samples : 10000")


