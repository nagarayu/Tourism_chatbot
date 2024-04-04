import re
import long_responces as long
import time
import sqlite3
con = sqlite3.connect("lab.db")
cur= con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS bot
                    (Person text ,Response text)''')

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi','hii', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('Experience the allure of [City/Region]\'s coastline from the comfort of our luxurious tourism boat.', ['luxurious', 'comfortable', 'coastline', 'journey'], required_words=['comfort', 'coastline'])
    response('Prepare to be amazed as we navigate through breathtaking landscapes and hidden gems.', ['amazed', 'breathtaking', 'hidden', 'gems', 'scenic'], required_words=['scenic'])
    response('Join us for a voyage filled with discovery, relaxation, and endless photo opportunities.', ['voyage', 'discovery', 'relaxation', 'photo opportunities'], required_words=['voyage', 'discovery'])
    response('Our tourism boat offers the perfect blend of adventure and tranquility, promising an unforgettable escape.', ['perfect', 'blend', 'adventure', 'tranquility', 'unforgettable'], required_words=['adventure', 'tranquility'])
    response('Cruise with us and uncover the secrets of [City/Region]\'s coastal treasures.', ['cruise', 'uncover', 'secrets', 'coastal treasures'], required_words=['secrets', 'coastal'])
    response('Sail away with us and indulge in a leisurely exploration of [City/Region]\'s most enchanting sights.', ['sail away', 'indulge', 'leisurely', 'exploration', 'enchanting sights'], required_words=['leisurely', 'exploration'])
    response('Embark on a maritime adventure with our expert crew, ready to guide you through [City/Region]\'s maritime marvels.', ['embark', 'maritime adventure', 'expert crew', 'guide', 'maritime marvels'], required_words=['maritime', 'adventure'])
    response('Discover the magic of [City/Region] from a new perspective as you glide along its shimmering waters aboard our tourism boat.', ['discover', 'magic', 'new perspective', 'glide', 'shimmering waters'], required_words=['discover', 'magic'])

    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response



def chat():
    t=5
    while t:
        t = t-1
        ye=input('You: ')
        cur.execute("INSERT INTO bot VALUES ('user',?)", [ye])
        print('Bot: ' + get_response(ye))


def hotel_info():
    print("1.","I want a 2-star hotel")
    print("2.","I want a 3-star hotel") 
    print("3.","I want a 5-star hotel")
    int(input("Please enter your hotel choice"))
    print("Thanks !! \n ", "now , please specify your food choice")
    print("1.","Indian Food")
    print("2.","American Food")
    print("3.","Italian Food")
    print("4.","Native Food")
    food = int(input())
    time.sleep(1)
    if food>4 or food<1:
      print("please check again!!")


    elif food==1:
      print("Great Choice !!")
      print("i know various types of Indian food ")
      print("you will find the best local recommendations for food & attractions!\n  ")
    elif food==2:
      print("Great Choice !!")
      print("i know various types of American food ")
      print("you will find the best local recommendations for food & attractions!\n  ")
    elif food == 3:
      print("Great Choice !!")
      print("i know various types of Italian food ")
      print("you will find the best local recommendations for food & attractions!\n  ")
    else:
      print("Great Choice !!")
      print("i know various types of Native food ")
      print("you will find the best local recommendations for food & attractions!\n  ") 
def Eat_drink():
    time.sleep(1)
    print("chhose from below\n")
    time.sleep(2)
    print("1. Our_Recommendations")
    print("2. Romanian_Restaurants")
    print("3. Italian_Cuisine")
    print("4. Asian_Cuisine")
    print("5. Bars&Pubs")
    print("6. Coffee_Shops")
    print("7. Back_to_main_menu\n")

    Eat=input()
    match Eat:
      case "1":
        print("Our Recommendation is...")
        print("Building 42, Amphitheatre Pkwy,Mountain View ,CA 94043, los angel")
        

      case "2":
        print("You can become a Data Scientist")

      case "3":
        print("You can become a backend developer")
    
      case "4":
        print("You can become a Blockchain developer")
      case "5":
        print("You can become a Blockchain developer")
      case "6":
        print("You can become a Blockchain developer")
      case "7":
        print("You can become a Blockchain developer")
      case _:
        print("chhose right option.")
def freetimeadvice(): 
    time.sleep(1)
    g="chhose from below\n"
    print(g)
    cur.execute("INSERT INTO bot VALUES ('bot',?)",[g])
    time.sleep(2)
    h="1. Where_to_Eat&Drink"
    print(h)
    i="2. What_to_visit"
    print(i)
    j="3. Where_to_party"
    print(j)
    k="4. Shopping \n"
    print(k)
       
    free=input()

    match free:
      case "1":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[h])
        time.sleep(1) 
        l="Ask your tastebuds what's they like?\n"
        print(l)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[l])
        Eat_drink()

      case "2":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[i])
        m="You can become a Data Scientist"
        print(m)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[m])

      case "3":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[j])
        n="You can become a backend developer"
        print(n)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[n])
    
      case "4":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[k])
        o="You can become a Blockchain developer"
        print(o)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[o])
      case _:
        print("chhose right option.")
nu=" "
cur.execute("INSERT INTO bot VALUES (?,?)", [nu,nu])
chat()
nu=" "
cur.execute("INSERT INTO bot VALUES (?,?)", [nu,nu])
x="how can i be of assistance?  chhose from below"
cur.execute("INSERT INTO bot VALUES ('bot',?)", [x])
print(x)

time.sleep(2)
y="1. FREETIME_ADVICES"
print(y)
z="2. HOTEL_INFORMATION"
print(z)
a="3. INTRESTING_FACTS_ABOUT_THE_CITY"
print(a)
b="4. FIND_DIRECTION\n"
print(b)
lang=input()

match lang:
    case "1":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[y])
        c="\nPlease tell me what you like to find\n"
        print(c)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[c])
        freetimeadvice()

    case "2":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[z])
        d="please choose your preferred hotel type\n"
        print(d)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[d])
        hotel_info()
    case "3":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[a])
        e="You can become a backend developer"
        print(e)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[e])
    
    case "4":
        cur.execute("INSERT INTO bot VALUES ('user',?)",[b])
        f="You can become a Blockchain developer"
        print(f)
        cur.execute("INSERT INTO bot VALUES ('bot',?)",[f])
    case _:
        print("chhose right option.")

con.commit()