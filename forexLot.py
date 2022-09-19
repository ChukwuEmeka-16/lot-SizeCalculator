
from cmd import PROMPT
from operator import truth





def accurateLot ():
   risk = input("how much are you risking in $ for a normal pair" + ":")

   pips = input("how much are you risking in pips" + ":")
       
   sum = int(risk) / int (pips)
   print(sum/10)




def accurateLotjpy():
 risk2 = input("how much are you risking in $ for a jpy pair" + ":")
 print("how much are you risking in pips" + ":")
 pips2 = int(input()) /4 * 3  
 sum2 = int(risk2)/ int(pips2)
 print(sum2/10)
# print("your answer should be lowercase no space")
# questioN = str(input("Are you trading a jpy pair?"))


question= input("Are you trading a jpy pair?" + ":")


if(question ==("yes")):
   
   accurateLotjpy()
elif (question==("no")):
   accurateLot()









