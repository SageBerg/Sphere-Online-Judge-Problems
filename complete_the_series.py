def main():
    test_cases = int(input)
    for _ in range(test_cases):
        numbers = input().split(" ") 
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        third = numbers[0]
        third_from_back = numbers[1]
        sum_of_series = numbers[2]
        #ideas: 
        
        #we know the step is <= half the distances beween 
        #third and third from last

main()
