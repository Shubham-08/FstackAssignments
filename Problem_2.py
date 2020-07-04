def candyDistribution(numberOfBags,candies):
    idx1=0
    totalCandies=0
    time=0
    for idx in candies:
        totalCandies+=idx
    if totalCandies%numberOfBags!=0:
        return (-1)
    else:
        equalCandies=totalCandies/numberOfBags
        while(idx1<numberOfBags):
            if equalCandies==candies[idx1]:
                idx1+=1
                continue
            elif equalCandies<candies[idx1]:
                time+=(candies[idx1]-equalCandies)
            else:
                time+=(equalCandies-candies[idx1])
            idx1+=1
    return(time)


answer=candyDistribution(4,[9,7,8,0])
