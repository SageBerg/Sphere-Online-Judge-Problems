"""
CandyI.py
SPOJ: 2123: Candy I
Sage Berg
5 Dec 2014
"""


def main():
    """
    input:  stdin
    output: prints either number of operations to needed to
            make all candy bags equal or -1 if fair distribution
            of candy is impossible
    """
    candy_bags = 0  # a default vaule to get the loop going
    while candy_bags != -1:
        candy_bags = int(input())
        if candy_bags != -1:
            bag_list = list()
            for _ in range(candy_bags):
                bag_list.append(int(input()))
            fair_amount = sum(bag_list)//candy_bags
            if fair_amount != sum(bag_list)/candy_bags:
                print(-1)
            else:
                ops = 0
                for bag in bag_list:
                    if bag > fair_amount:
                        ops += bag - fair_amount
                print(ops)

main()
