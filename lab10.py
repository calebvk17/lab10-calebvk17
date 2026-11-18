# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.

def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9

    # The goal is to solve a math expression where the operator
    # comes after the numbers instead of between them.

    # Exmaple: ["2", "1", "+", "3", "*"]
    # First, 2 + 1 = 3, then 3 * 3 = 9.
    # The final answer would be 9.

    # A good way to solve this is by using a stack.
    # Go through each item in the list and push numbers onto the stack.
    # When an operator appears, pop the last two numbers and do the calculation.
    # Push the answer back onto the stack and continue until the list is done.
    # Return the final number left in the stack.
    
    stack = []
    
    for token in tokens:
        if token == "+" or token == "-" or token == "*" or token == "/":
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                result = int(a / b)
            
            stack.append(result)
            
        else:
            stack.append(int(token))
            
    return stack.pop()

def decode_string(s):
    # Outline:
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    
    # The goal is to decode a string by repeating the characters
    # inside brackets based on the number before them.
    
    # Example: "3[a2[c]]"
    # First, 2[c] becomes "cc".
    # Then a + cc becomes "acc".
    # Repeating it 3 times gives you "accacccacc"
    
    # A good way to solve this is by using a stack.
    # Go through the string one character at a time.
    # Save the current string and number when an opening bracket appears.
    # When a closing bracket appears, take them off the stack.
    # Repeat the current string the correct number of times and combine it.
    # Keep doing this until the whole string is decoded.
    
    stack = []
    currentStr = ""
    num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "[":
            stack.append((currentStr, num))
            currentStr = ""
            num = 0
        elif char == "]":
            previousStr, number = stack.pop()
            currentStr = previousStr + currentStr * number
        else:
            currentStr += char
            
    return currentStr  
            
            
def daily_temperatures(temps):
    # Outline:
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    
    # The goal is to find out how many days you have to wait until
    # a warmer temperature comes along for each day.

    # Example: [73, 74, 75, 71, 69, 72, 76]
    # 73 waits 1 day, 74 waits 1 day, and 75 waits 4 days.
    # The anaswer would be  [1, 1, 1, 4, 2, 1, 1, 0].

    # A good way to solve this is by using a stack.
    # Go through each temperature and compare it with previous days.
    # If the current temperature is warmer, then update the number of days
    # that the previous temperature had to wait.
    # Keep track of the days that still need a warmer temperature.
    # Return the list of waiting days when finished.
    
    stack = []
    result = [0] * len(temps)
    
    for i in range(len(temps)):
        while len(stack) > 0 and temps[i] > temps[stack[-1]]:
            previousDay = stack.pop()
            result[previousDay] = i - previousDay
            
        stack.append(i)
    
    return result

def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    
    # The goal is to count how many seperate islands of land
    # are in a grid. Land is represented by 1 and water by 0.
    
    # Example: ["11000", "11000", "00100", "00011"]
    # There are 3 seperate groups of land, so the answer is 3.
    
    # A good way to solve this is by using a stack or queue.
    # Go through each position in the grid and look for land.
    # When land is found, increase the island count.
    # Check the surrounding positions
    # to find any connected land and make sure that it isn't counted again.
    # Continue until the whole grid has been checked.
    # Return the total number of islands.
    
    if len(grid) == 0:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    visited = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                stack = [(r, c)]

                while len(stack) > 0:
                    row, col = stack.pop()

                    if (row, col) not in visited:
                        visited.add((row, col))

                        if row > 0 and grid[row - 1][col] == "1":
                            stack.append((row - 1, col))

                        if row < rows - 1 and grid[row + 1][col] == "1":
                            stack.append((row + 1, col))

                        if col > 0 and grid[row][col - 1] == "1":
                            stack.append((row, col - 1))

                        if col < cols - 1 and grid[row][col + 1] == "1":
                            stack.append((row, col + 1))

    return islands
    
def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    print(eval_rpn(["4", "13", "5", "/", "+"]))   # returns 6    (4 + 13 // 5)
    print(decode_string("3[a]2[bc]"))   # returns "aaabcbc"
    print(decode_string("3[a2[c]]"))    # returns "accaccacc"
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # returns [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60]))                   # returns [1, 1, 1, 0]
    print(num_islands(["11000", "11000", "00100", "00011"]))   # returns 3
    print(num_islands(["11110", "11010", "11000", "00000"]))   # returns 1)

if __name__ == "__main__":
    main()