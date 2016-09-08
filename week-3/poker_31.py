import sys 

def count(hands):
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in hands:
        numbers = n.split(",")
        nums[int(numbers[-1])] += 1 
    return nums

def main():
    hands = sys.stdin.readlines()
    nums = count(hands)
    
    print("The probability of nothing is {:.4f}%".format((nums[0]/sum(nums) * 100)))
    print("The probability of one pair is {:.4f}%".format((nums[1]/sum(nums) * 100)))
    print("The probability of two pairs is {:.4f}%".format((nums[2]/sum(nums) * 100)))
    print("The probability of three of a kind is {:.4f}%".format((nums[3]/sum(nums) * 100)))
    print("The probability of a straight is {:.4f}%".format((nums[4]/sum(nums) * 100)))
    print("The probability of a flush is {:.4f}%".format((nums[5]/sum(nums) * 100)))
    print("The probability of a full house is {:.4f}%".format((nums[6]/sum(nums) * 100)))
    print("The probability of four of a kind is {:.4f}%".format((nums[7]/sum(nums) * 100)))
    print("The probability of a straight flush is {:.4f}%".format((nums[8]/sum(nums) * 100)))
    print("The probability of a royal flush is {:.4f}%".format((nums[9]/sum(nums) * 100)))
    
if __name__ == "__main__":
    main()
