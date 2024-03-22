x = "abcd"
jump = False
for i in x:
    if i == 'b' or jump:
        if jump:
            jump = False
        else:
            jump = True
        continue
    print("{}".format(i))
