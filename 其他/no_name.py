


row = 4
column = 4 
res = [ ["" for i in range(row)] for j in range(column)]

def solve():

    # print(res)

    direction = 0 # left 
    start = [1, 0]
    cur = [1, 0]
    route = [cur,]

    while True:
        if direction == 0 :
            # left 
            for i in range(column-1):
                cur = [cur[0], cur[1] + 1]
                route.append(cur)
                # print(route)

            # left end 
            if cur[0] == row - 1 or cur[0] == row - 2:
                pass
                
            else :
                cur = [cur[0] + 1, cur[1]]
            route.append(cur)
            direction = 1
        
        else :
            for i in range(column-1):
                cur = [cur[0], cur[1] - 1]
                route.append(cur)
            # right end 
            if cur[0] == row - 1 or cur[0] == row - 2:
                while cur != start:
                    print(cur)
                    cur = [cur[0] - 1, cur[1]]
                    route.append(cur)
                return route
            else :
                cur = [cur[0] + 1, cur[1]]
            route.append(cur)
            direction = 0
        


                    



if __name__ == "__main__":
    print("hello")

    r = solve()

    print(r)