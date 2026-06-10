# Alice, Bob and Carol have agreed to pool their Halloween candy and split it even among 
# themselves. For the sake of their friendship, any candies left over will be smashed. For 
# example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

# Write an arithmetic expression below to calculate how many candies they must smash for a 
# given haul.
alice_candies = 121
bob_candies = 77
carol_candies = 109

total = alice_candies + bob_candies + carol_candies
to_smash = total % 3

print("Total count of candies:", total)
print("Total count between each friend:", total // 3)
print("How many candies to smash?", to_smash)
