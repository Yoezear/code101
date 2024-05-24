class solution: 
    def toh(self, N, fromm, to, aux):
        if N==1:
            print("move disk"+str(N)+ "from rod"+str(fromm)+ "to rod"+str(to))
            print("\n")
            return 1
        moves = 0
        moves += self.toh (N -1, fromm, aux, to)
        moves += 1
        print("move disk"+ str(N)+ "from rod"+ str(fromm)+"to rod"+str(to))
        moves += self.toh (N - 1, aux, to, fromm)
        return moves
s = solution()
print(s.toh(3,1,3,2))