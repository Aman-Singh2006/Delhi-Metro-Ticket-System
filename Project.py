import datetime
import random
red_line={"Rithala": 10, "Rohini West": 20, "Rohini East": 20, "Pitampura": 30,"Kohat Enclave": 30, "Nsp": 30, "Keshav Puram": 40, "Kanahiya Nagar": 40,"Inderlok": 40, "Shastri Nagar": 40, "Pratap Nagar": 50, "Pul Bangash": 50,
           "Tis Hazari": 50, "Kashmere Gate": 50}
green_line={"Inderlok": 10, "Ashok Park Main": 15, "Punjabi Bagh": 20, "Punjabi Bagh West": 25,"Shivaji Park": 30, "Madipur": 35, "Paschim Vihar East": 40, "Paschim Vihar West": 45,"Peeragarhi": 50, "Udyog Nagar": 55, "Surajmal Stadium": 60, "Nangloi": 65,
            "Nangloi Railway Station": 70, "Rajdhani Park": 75, "Mundka": 80,"Mundka Industrial Area": 85, "Ghevra": 90}
yellow_line={"Samaypur Badli": 10,"Rohini Sector 18": 15,"Haiderpur Badli Mor": 20,"Jahangirpuri": 25,"Adarsh Nagar": 30,"Azadpur": 35, "GTB Nagar": 40,"Vishwa Vidyalaya": 40,"Kashmere Gate": 50,
               "Chandni Chowk": 50,"New Delhi": 60,"Rajiv Chowk": 60,"Central Secretariat": 65,"INA": 70,"Hauz Khas": 75,"Qutub Minar": 80,"Millennium City Centre": 90}
pink_line = {"Majlis Park": 10,"Azadpur": 15, "Shalimar Bagh": 20,"Netaji Subhash Place": 25,"Punjabi Bagh West": 30,"Rajouri Garden": 35,"Mayapuri": 40,"Delhi Cantt": 45,"Durgabai Deshmukh South Campus": 50,
             "INA": 60, "Lajpat Nagar": 65,"Mayur Vihar Ph-1": 70,"Anand Vihar": 80,"Welcome": 85,"Shiv Vihar": 95}

metro_map={**red_line,**green_line}
metro_map.update(yellow_line)
metro_map.update(pink_line)
Balance=100
while True:
    print("press 1 For Ticket Book")
    print("Press 2 For Metro Card Recharge")
    print("Press 3 For Check Balance Of Metro Card")
    print("Press 4 For Exit")
    ch=int(input("Enter Your Choice:"))
    match ch:
        case 1:
            print("-"*30,"Welcome To Delhi Metro","-"*30)
            print("\n"," "*30,"Select Metro Line"," "*30)
            print("\n1.Red Line | 2.Green Line |3.Yellow Line |4.Pink Line")
            line=int(input("Select Line:"))
            if(line==1):
                print("->".join(red_line.keys()))
            elif(line==2):
                 print("->".join(green_line.keys()))
            elif(line==3):
                 print("->".join(yellow_line.keys()))
            elif(line==4):
                 print("->".join(pink_line.keys()))
            else:
                print("Invalid Choice")
            From=input("Enter Your Starting station:").title()
            To=input("Enter Your Destination:").title()
            if(From in metro_map and To in metro_map):
                num_passengers=int(input("Enter Number Of Passengers:"))
                base_fare=abs(metro_map[To]- metro_map[From])
                if(base_fare==0):base_fare=10
                Fare=base_fare*num_passengers
                print("\nSelect Payment Mode:")
                print("1. Cash | 2. UPI | 3. Metro Card")
                pay_mode = int(input("Choice (1/2/3): "))
                mode_name=""
                if(pay_mode==3):
                    mode_name = "Metro Card"
                    if(Balance>=Fare):
                        Balance-=Fare
                    else:
                        print("Insufficient Balance! Card has only Rs.",{Balance})
                        continue
                elif(pay_mode==2):
                    mode_name= "UPI"
                else:
                    mode_name="Cash"
                print("\n"+"="*55)
                print(" "*15+"DELHI METRO RAIL CORPORATION")
                print(" "*18+"(Government of Delhi)")
                if(From in red_line and To in green_line or From in green_line and To in red_line):
                    print("-"*55)
                    print(" "*6,">>Alert! Interchange At Inderlok Station<<")
                elif(From in red_line and To in yellow_line) or (From in yellow_line and To in red_line):
                    print("-"*55)
                    print(" "*6, ">> ALERT: INTERCHANGE AT KASHMERE GATE <<")
                elif (From in red_line and To in pink_line) or (From in pink_line and To in red_line):
                    print("-"*55)
                    print(" "*6,">> ALERT: INTERCHANGE AT NSP or WELCOME <<")
                elif (From in yellow_line and To in pink_line) or (From in pink_line and To in yellow_line):
                    print("-"*55)
                    print(" "*6, ">> ALERT: INTERCHANGE AT AZADPUR or INA <<")
                elif (From in green_line and To in pink_line) or (From in pink_line and To in green_line):
                    print("-" * 55)
                    print(" " * 6, ">> ALERT: INTERCHANGE AT PUNJABI BAGH WEST <<")

                print("-" * 55)
                print(" " * 18, "-" * 12)
                print(" " * 18, "|", "#" * 8, "|")
                print(" " * 18, "|", "#" * 8, "|")
                print(" " * 18, "|", "#" * 8, "|")
                print(" " * 18, "|", "#" * 8, "|")
                print(" " * 18, "|", "#" * 8, "|")
                print(" " * 18, "-" * 12)
                print(" " * 10, "Date/Time |", datetime.datetime.now())
                print(" " * 10, "Ticket Id:|", random.randint(1000, 9999))
                print(" " * 10, "From      |", From)
                print(" " * 10, "Destination|", To)
                print(" " * 10, "Fare      |Rs.", Fare)
                print(" " * 10, "STATUS    | BOOKED")
                print(" " * 10, "Payment   |", mode_name)
                print("-" * 55)
                print(" " * 12 + "WISH YOU A HAPPY JOURNEY!")
                print("=" * 55)
            else:
                print("!! Error: Station Name Not Found. Check Spelling !!")
                
        case 2:
            print("-"*20,"Card Recharge","-"*20)
            card_no=input("Enter 6 Digit Card Number:")
            if(len(card_no)==6 and card_no.isdigit()):
                Recharge_amt=int(input("Enter Recharge Amount:"))
                Balance+=Recharge_amt
                print("*"*30)
                print("Success:Card",card_no,"Recharged!")
                print("Amount Added: Rs.",Recharge_amt)
                print("New Balance:Rs.",Balance)
                print("*"*30)
            else:
                print("! ERROR: Invalid Card Number. Must be exactly 6 digits !!")
        case 3:
            print("-"*20,"Card Recharge","-"*20)
            card_no=input("Enter 6 Digit Card Number:")
            if(len(card_no)==6 and card_no.isdigit()):
                print("*"*30)
                print("Card Holder:Aman")
                print("Status:Active")
                print("Balance:Rs.",Balance)
                print("*"*30)
                if Balance<50:
                 print("!! ALERT: LOW BALANCE. PLEASE RECHARGE !!")
            else:
                print("!! ERROR: Invalid Card Number. Must be exactly 6 digits !!")
        case 4:
            print("*"*40)
            print("Thank You For Using Delhi Metro Service!")
            print(" "*10,"Having A Great Day!"," "*10)
            print("*"*40)
            break
        case _:
            print("Invalid Choice! Please Enter A Number Between 1 to 4")
                
                
                
    
