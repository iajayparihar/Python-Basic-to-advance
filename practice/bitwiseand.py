def bit():
    for i in range(20):
        # if i%5==0:
            c = i ^ i+1
            print(i," ",i+1," Answer = ",c)
            print()

bit()
