## this turned out kinda jank xD


## just some constant strings to check against later
nums = "123456789"
spelled = "one,two,three,four,five,six,seven,eight,nine".split(",")
numsMap = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

with open("../tests.txt", "r") as file:
    txt = file.read().strip().split("\n") ## split up the file into an easy to use list

    sum = 0 # the sum of all the codes

    for line in txt: # loop through each line in the list

        # for each line store all the found digits in another list
        digits = []

        ## loop through every character in the line
        for i in range(len(line)):
            if line[i] in nums: # check if its a digit
                digits.append([line[i], i]) # append that digit along with it's index to the digits list
        

        ################ PART 2 ################
        # this section can be commented out to answer part 1
        for s in spelled: # loop through all possible spelled out numberes
            if s in line: # identify whether it exists in the line

                indices = [index for index in range(len(line)) if line.startswith(s, index)] # get the index of all of them

                ## add the first and last one to the digits list
                digits.append([str(numsMap[s]), indices[0]])
                digits.append([str(numsMap[s]), indices[-1]])
        ################ PART 2 ################


        ## sort the array of digits
        digits = sorted(digits,key=lambda digits:digits[1])

        ## create a number with the first and last digits in the array and add it to the list
        sum += int(digits[0][0] + digits[-1][0])

    print(sum) # answer :)