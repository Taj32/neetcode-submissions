class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0. variables
        fleets = 0
        cars = []
        stack = []
        
        # 1. sort the positions and speeds in descending order (highest position, lowest position)
        # for i, e in position:
        #    cars.append()

        # sort by the biggest position:
        for i , e in enumerate(position): # O(n)
            cars.append([e, speed[i]])

        # Sort in-place using the first item (index 0) of each sublist
        cars.sort(key=lambda x: x[0], reverse=True) # O(nlogn)
        #print(cars)

        for i, e in enumerate(cars): # O(n)
            time_to_reach = (target - e[0]) / e[1]
            #print("--- " + str(i) + " ---")
            if stack and time_to_reach <= stack[-1]: 
                fleets = fleets # this will catchup so dont make a seperate fleet
                time_to_reach = stack[-1]
                #print("this will catchup to something")
            else:
                fleets += 1 # make a seperate fleet
                #print("this isnt catching up so make it do its own thing")
        
            stack.append(time_to_reach)

        return fleets

# Attempt 1 - O(nlogn) time ; O(n) space