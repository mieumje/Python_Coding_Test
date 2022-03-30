from audioop import reverse
from calendar import c


def solution(tickets):
    answer = []

    dict = {}
    for ticket in tickets:
        ticket_from = ticket[0]
        ticket_destination = ticket[1]
        try:
            dict[ticket_from].append(ticket_destination)
        except:
            dict[ticket_from] = [ticket_destination]
    stack = ["ICN"]
    for key in dict.keys():
        dict[key].sort(reverse=True)
    print(dict)

    while stack:
        current_from = stack[-1]

        try:
            stack.append(dict[current_from].pop())
        except:
            answer.append(stack.pop())

    answer.reverse()
    return answer


# 입출력 예
# tickets	                                                                        return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	                                ["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))
