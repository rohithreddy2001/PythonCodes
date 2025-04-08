'''
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
'''
#Linear search

def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


#Binary search
# def test_location(cards, query, mid):
#     if cards[mid] == query:
#         return 'found'
#     elif cards[mid] < query:
#         return 'left'
#     else:
#         return 'right'
#
# def locate_card(cards, query):
#     lo, hi = 0, len(cards) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = test_location(cards, query, mid)
#         if result == 'found':
#             return mid
#         elif result == 'left':
#             lo = mid+1
#         elif result == 'right':
#             hi = mid-1
#     return -1

cards = [1,2,4,3,6,5]
cards.sort()
# print(cards)
query = int(input("Enter the query: "))
print(locate_card(cards, query))