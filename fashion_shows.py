def main():
    """
    input: stdin
    output: the sum of hotness bonds for each trial
    """
    tests = int(input())
    while tests > 0:
        num_couples = int(input())
        women = input().split(" ")
        men = input().split(" ")
        hotness_bond = 0
        for i in range(len(women)):
            hotness_bond += int(women[i])*int(men[i])
        print(hotness_bond)
        tests -= 1

main()
