feet=420.0
notebook=1.8
pencil=1.9
small_tool=2.1
i=0
sum=0
sum_count=0
max=0
max_count=0
max_notebook=0
max_pencil=0
max_small_tool=0
j=0
while i<=233:
    j=0
    while j <= int((420-1.8*i)/1.9):
        if int((420-1.8*i-1.9*j)/2.1)>=0:  
            sum=1.9*i+1.8*j+int((420-1.8*i-1.9*j)/2.1)*2.1
            sum_count=i+j+int((420-1.8*i-1.9*j)/2.1)
            if (max<sum) & (int(max_count)<int(sum_count)):
                max=sum
                max_count=sum_count
                max_notebook=i
                max_pencil=j
                max_small_tool=int((420-1.8*i-1.9*j)/2.1)
        j+=1
    i+=1
print('%.1f' % float((max_notebook+100)*1.8+(max_pencil+100)*1.9+(max_small_tool+100)*2.1),max_notebook+100,max_pencil+100,max_small_tool+100)