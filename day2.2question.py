year=int(input("enter the value :"))
if(year<0):
   print("enter the valid inputs")
else:
   if(year!=int(year)):
      print("it is invalid")
   else:
      if(year%4==0 or year%400==0 or year%100==0):
         print("it is a leap year ")
      else:
         print("it is not a leap year ")
         b=int(year)
         while(b>0):
            b=b-1
            if(b%4==0):
               print(b)
               break;
