"""
Method:
    generate a random set of n heaps with size m

player enters 2 numbers: heap to remove from; how many to remove
game continues until heaps are all empty

if the computer is in a losing state: remove from a random heap 
if in a winning state it plays the winning move.
initialised state cannot be a losing state
"""
from random import randint
from typing import List, Tuple


class Game:
    colours = {
            'blue': '\033[94m',
            'cyan': '\033[96m',
            'green': '\033[92m',
            'warning': '\033[93m',
            'fail': '\033[91m',
            'end': '\033[0m'
        }
    def __init__(self):
        self.getGameSettings()
        self.heaps = [randint(1,self.maximumSticks) for i in range(self.numberOfHeaps)]
        self.run()
        

    def getGameSettings(self):
        """Prompts the user to enter the desired number of heaps and maximum heap size."""
        numberOfHeaps, maximumSticks = 0, 0

        while numberOfHeaps < 1 or maximumSticks < 1:
            # does this count as bad code? -> ye
            try:
                numberOfHeaps = int(input("Please enter the number of you heaps would like to play with: ").strip())
            except ValueError:
                print(f"{self.colours['warning']} ERROR: It appears that you have entered an invalid number of heaps.{self.colours['end']}")
                print(f"{self.colours['warning']} Please try again, and note that: \n\n \t-\t Only arabic numerals may be entered.\n\n \t-\t The number of heaps must be a positive number.{self.colours['end']}")
                continue

        
            try:
                maximumSticks = int(input("What should be the maximum number of sticks in a heap? ").strip())
            except ValueError:
                print(f"{self.colours['warning']} ERROR: It appears that you have entered an invalid limit for the maximum number of sticks.{self.colours['end']}")
                print(f"{self.colours['warning']} Please try again, and note that: \n\n \t-\t Only arabic numerals may be entered.\n\n \t-\t The number of sticks must be a positive number.{self.colours['end']}")
                    
        self.numberOfHeaps = numberOfHeaps
        self.maximumSticks = maximumSticks
        
        return

    def getComputerMove(self)->Tuple[int, int]:
        """Plays the first winning move by heap index, if said move exists."""
        winning = 0
        for heap in self.heaps:
            winning ^= heap

        if winning:
            for i, heap in enumerate(self.heaps):
                if heap^winning < heap:
                    return i, heap - (heap^winning)
        
        heap = randint(1, len(self.heaps)-1)
        return heap, randint(1,self.heaps[heap])

    def getUserMove(self)->Tuple[int,int]:
        """Gets the move from the user"""
        heap, number = -1, 0

        while heap < 0 or number < 1:
            print(f"{self.colours['green']}The heaps to pick from are:{self.colours['end']} {self.heaps}")

            try:
                heap = int(input("Please select a heap to pick up from: ").strip()) - 1
                if heap > len(self.heaps):
                    heap = -1
                    print(f"{self.colours['warning']} ERROR: There aren't that many heaps.{self.colours['end']}\n\n")
                    continue

            except ValueError:
                print(f"{self.colours['warning']} ERROR: It appears that you have entered an invalid heap value.{self.colours['end']}")
                print(f"{self.colours['warning']} Please try again, and note that: \n\n \t-\t Only arabic numerals may be entered.\n\n \t-\t The heap must be a positive number.{self.colours['end']}\n\n")
                continue

            try:
                number = int(input("Please select a number of sticks to pick up from the specified heap: ").strip())
                if self.heaps[heap] < number:
                    number = 0
                    print(f"{self.colours['warning']} ERROR: The specified heap does not contain that many sticks.{self.colours['end']}\n\n")

            except ValueError:
                print(f"{self.colours['warning']} ERROR: It appears that you have entered an invalid heap value.{self.colours['end']}")
                print(f"{self.colours['warning']} Please try again, and note that: \n\n \t-\t Only arabic numerals may be entered.\n\n \t-\t The heap must be a positive number.{self.colours['end']}\n\n")
                
        return heap, number

    def run(self):
        while self.heaps:
            userHeap, userNumber = self.getUserMove()
            self.heaps[userHeap] -= userNumber

            if not self.heaps[userHeap]: 
                del self.heaps[userHeap]

            if not self.heaps:
                break

            computerHeap, computerNumber = self.getComputerMove()
            
            print(f"{self.colours['blue']}The computer removes {computerNumber} sticks from heap {computerHeap + 1}{self.colours['end']}.\n")
            self.heaps[computerHeap] -= computerNumber

            if not self.heaps[computerHeap]:
                del self.heaps[computerHeap]

        else:
            print(f"{self.colours['fail']}Unlucky, you lost!{self.colours['end']}")
            return
        print(f"{self.colours['cyan']}Congratulations, you won!{self.colours['end']}")
        return            

    
if __name__ == "__main__":
    Game()
