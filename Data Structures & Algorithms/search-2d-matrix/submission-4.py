class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 0. set the variables
        lowm = 0
        highm = len(matrix) - 1

        # check if its just a single row
        if(len(matrix)==1):
            print("single row detected just do normal binary search")

            # we're gonna do binary search on this row specifically
            low = 0
            high = len(matrix[0]) - 1
            #midn = (low+high) // 2
            while low <= high:
                midn = (low+high) // 2
                print(midn)
                if(matrix[0][midn] == target):
                    return True
                elif(matrix[0][midn] < target):
                    # need update the low
                    low = midn + 1
                elif(matrix[0][midn] > target):
                    # need to update the high
                    high = midn - 1

            return False
        

        while lowm <= highm:
            mid = (lowm + highm) // 2
            n = len(matrix[mid])
            # check if this row would have the target
            if(matrix[mid][0] > target):
                # need to update the highm
                highm = mid - 1
            elif(matrix[mid][n-1] >= target or len(matrix) == 1):
                # should be in this row (either by deduction or the row being 0)

                # we're gonna do binary search on this row specifically
                low = 0
                high = n-1
                while low <= high:
                    midn = (low+high) // 2
                    if(matrix[mid][midn] == target):
                        return True
                    elif(matrix[mid][midn] < target):
                        # need update the low
                        low = midn + 1
                    elif(matrix[mid][midn] > target):
                        # need to update the high
                        high = midn - 1

                return False
                
                # if this loop ends that means theres n
            elif(matrix[mid][n-1] < target):
                # need to update the lowm
                lowm = mid + 1
            

        return False