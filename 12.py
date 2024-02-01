for a in range (2,21):
    with open(f"Table_of_{a}.txt" , 'w') as f:
        for b in range (1,11):
            f.write(f"{a} x {b} = {a*b}\n")            

          


 


    