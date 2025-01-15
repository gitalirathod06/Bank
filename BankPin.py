class Bank:
    Bname='Swiss'
    ROI=0.01

    def __init__(self,name,Mobno,Aadhar,PAN,Bal,pin):
        self.name=name
        self.Mobno=Mobno
        self.Aadhar=Aadhar
        self.PAN=PAN
        self.Bal=Bal
        self.pin=pin


    def BalCheck(self):
        count=0
        print('total number of attempts is 3')

        while count<3:
            if self.checkPin()==self.pin:
                print(f'Available balance is {self.Bal}')
                break

            else:
                print('Incorrect passcode')
                print(f'attempt remaining {2-count}')
                count+=1

        else:
            
            print('Try after some time')


    def Deposite(self):
         count=0
         print('total number of attempts is 3')

         while count<3:
             if self.checkPin()==self.pin:

                 amount=int(input('Enter the amount to deposite:'))

                 if amount<=20000:
                     self.Bal+=amount
                     print('Amount credited successfully...')
                     print(f'Available balance is {self.Bal}')
                     break               

                 else:
                     print('deposite amount is upto 20000')
                     break

             else:
                  print('Incorrect passcode')
                  print(f'Remaining attempts {2-count}')
                  count+=1

         else:
            print('Try after some time')


    def WithDraw(self):

        count=0
        print('total number of attempts is 3')

        while count<3:

           if self.checkPin()==self.pin:
               amount=int(input('Enter the amount to withdraw:'))

               if amount<=20000:
                   if amount<=self.Bal:
                       self.Bal-=amount
                       print('Amount debited successfully..')
                       print(f'Available balance is {self.Bal}')
                       break
                   else:
                        print('Insufficient balance...')
                        break

               else:
                   print('Withdraw amount is upto 20000')
                   break

           else:
               print('Incorrect passcode')
               print(f'Remaining attempts {2-count}')
               count+=1

        else:
            print('Try after some time')


       

    @staticmethod
    def checkPin():

        passcode=int(input('Enter the 4-digit pin:'))

        return passcode

    @classmethod
    def ChangeBankname(cls):
        cls.Bname='Punjab National Bank'
                     
user1=Bank('Hari',9876543211,3467834567,'A420B420',5000,9878)
user2=Bank('Maitry',6876712819,6252398712,'E198321',9000,2342)
user3=Bank('Ravi',898610037,76010138891,'B92711',3000,1111)

print('Checking balance of user3:')
user3.BalCheck()
print('-------------------------')
print('Deposite the money in user1:')
user1.Deposite()
print('-------------------------')
print('Withdraw the money from user2:')             
user2.WithDraw()
print(Bank.Bname)
Bank.ChangeBankname()
print(user1.Bname)
print(Bank.Bname)

