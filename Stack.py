from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# s = Stack()
# def reverse_string(container):
#     for char in container:
#         return char[::-1]
#
# s.push("We will conquere COVID-19")
#
# print(f"Original: {s.container}\nReversed: {reverse_string(s.container)}")

# Function in python that can reverse a string using stack data structure.
def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
        # print(stack.container)
    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()
    return rstr

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    # print(reverse_string("We will conquere COVID-19"))
    # print(reverse_string("I am the king"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


