class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = []
        dire_queue = []

        for index in range(len(senate)):
            if senate[index] == "R":
                radiant_queue.append(index)
            else:
                dire_queue.append(index)

        while radiant_queue and dire_queue:
            end_of_line = 1 + max(radiant_queue[-1], dire_queue[-1])
            if radiant_queue[0] < dire_queue[0]:
                radiant_queue.pop(0)
                radiant_queue.append(end_of_line)
                dire_queue.pop(0)
            else:
                dire_queue.pop(0)
                dire_queue.append(end_of_line)
                radiant_queue.pop(0)

        return "Radiant" if radiant_queue else "Dire"
