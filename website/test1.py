from random import randrange

fruits=['apples','oranges','bananas','mangoes','grapes','strawberry','Pineapple','Melon','Avocado','Kiwi','lemon','coconut','juicerr','luice','peanut']

# print(len(fruits))
man=list()


for i in range(0,len(fruits)):
 
    rf=randrange(0,len(fruits)-1)  #0-9 ma koi pan number
    length = len(fruits[rf])//2  #apple aave to aeni length divide by 2
    que = fruits[rf][0:length]  #[0:3]=app
    print("here is your queston", i+1, que, "...")  #app....
    ans=input("fill the word :")
    
    final=que+ans
    if final not in fruits:
        if i<5:
          man.append('{}  {}'.format('|','|'))
          
        elif i==5:
            man.append('{}  {}'.format('|','0'))
        elif i==6:
          man.append('{}  {}'.format('|','-'))
        elif i==7:
          man.pop()
          man.append('{}  {}{}'.format('|','-','|'))
        elif i==8:
          man.pop()
          man.append('{}  {}{}{}'.format('|','-','|','-'))
        elif i==9:
         
          man.append('{}   {}'.format('|','/\\'))
          
        for r in man:
          print(r)
   
else:
      print("Game is finish")


