#Relative Ranks : array of interger representing score of athletes will be given you need to return ranks
#Input : [5,4,3,2,1] , Output:["Gold Medal","Silver Medal","Bronze Medal",4,5]

def RankCard(Score):
    Score = sorted(Score)
    Rank = []

    for i in Score:
        if i == 1:
            Rank.append("Gold Medal")
        elif i == 2:
            Rank.append("Silver Medal")
        elif i == 3:
            Rank.append("Bronze Medal")
        else:
            Rank.append(i)

    return Rank

def main():

    Players = int(input("Enter the Number of Players :"))

    Score_Card = []

    for i in range(Players):
        Score_Card.append(int(input(f"Enter the Score of {i+1}th Player :")))

    Ranking = RankCard(Score_Card)
    print("Ranking :", Ranking)

if __name__ == "__main__":
    main()