def talk_like_a_pirate():
    pirate_sayings = {
        "hello": "ahoy",
        "give-attention": "avast", 
        "yes": "aye",
        "help-a-friend-in-need": "bail out",
        "stop": "belay",
        "nonsense": "bilge",
        "loot": "booty",
        "friendly-conversation": "chew the fat", 
        "bottom-of-the-sea": "Davy Jones’s locker",
        "goodbye": "fair winds",
        "good-luck": "fair winds",
        "food": "grub",
        "to-rob": "pillage",
        "gossip": "scuttlebutt",
        "exclamation": "aargh",
        "friend": "matey",
        "friends": "harties",
        "disbelief": "blimey",
        "leave-no-survivors": "dead men tell no tales",
        "alcoholic-drink": "grog",
        "person-who-is-not-a-sailor": "landlubber",
        "pirate-flag": "jolly roger",
        "troublemaker": "scallywag",
        "surprise": "shiver me timbers",
        "have-a-drink": "splice the mainbrace",
        "whale-sighting": "thar she blows",
        "cheerful-expression": "yo ho ho",
        "is": "be"
    }
    
    hello_words = ["hello", "hi", "yo", "wassup", "hola", "bonjour", "guten-tag", "salve", "greetings", "salutations", "hey"]
    attention_words = ["give-attention", "attention", "listen", "pay-attention", "hear-ye", "look-at-me"]
    yes_words = ["yes", "i-agree", "of-course", "yeah", "uh-huh", "I-like-that", "definitely", "great"]
    help_words = ["help-a-friend-in-need", "help", "assist", "aid", "help-out"]
    stop_words = ["stop", "halt", "cease", "stop-it", "don't-do-that", "shut-up"]
    nonsense_words = ["nonsense", "foolish-talk", "lunacy", "senselessness", "ridiculous"]
    conversation_words = ["friendly-conversation", "conversation", "chat", "talk", "text", "email"]
    bottom_words = ["bottom-of-the-sea", "ocean-floor", "lake-bed", "river-bed"]
    goodbye_words = ["goodbye", "farewell", "so-long", "vale", "see-you-later", "bye-bye", "bye"]
    luck_words = ["good-luck", "you-got-this", "break-a-leg", "slay"]
    food_words = ["food", "kimchi", "rice", "meat", "beaf", "pork", "breakfast", "lunch", "dinner", "dessert", "pizza", "pasta", "bread", "fruit", "vegetables", "apples", "bananas", "carrots", "donuts", "eggs", "fries", "grapes", "hamburgers", "ice cream", "jelly", "kiwi", "lemons", "mangoes", "noodles", "oranges", "pizza", "quinoa", "rice", "spinach", "tomatoes", "ugli fruit", "vegetables", "watermelon", "xigua", "yogurt", "zucchini", "bacon", "cheese", "dates", "enchiladas", "falafel", "guacamole", "honey", "jam", "kale", "lasagna", "macaroni", "nectarines", "olives", "pancakes", "quesadilla", "ramen", "sushi", "tacos", "udon", "vanilla", "waffles", "xanthan-gum", "yams", "ziti"]
    rob_words = ["to-rob", "to-steal", "rob", "robbed", "robbing", "robbery", "steal", "stealing", "stole"]
    gossip_words = ["gossip", "rumors", "tea"]
    exclamation_words = ["exclamation", "omg", "oh-my-gosh", "oh-my-God", "dang-it", "darn-it"]
    friend_words = ["friend", "mate", "bff", "bud", "buddy", "best-friend"]
    friends_words = ["friends", "mates", "bffs", "buds", "buddies", "best-friends"]
    disbelief_words = ["disbelief", "i-don't-believe-it", "i-didn't-see-that-comming", "what-the-heck", "i-didn't-expect-that"]
    nosurvivors_words = ["leave-no-survivors", "kill-them-all", "execute-them", "kill-them", "murder"]
    alcohol_words = ["alcoholic-drink", "wine", "beer", "ale", "liqour", "vodka", "booze", "spirits"]
    career_words = ["person-who-is-not-a-sailor", "doctor", "engineer", "teacher", "chef", "scientist", "lawyer", "accountant", "artist", "writer", "architect", "nurse", "software-developer", "photographer", "psychologist", "veterinarian", "firefighter", "police-officer", "pilot", "carpenter", "electrician", "mechanic", "social-worker", "pharmacist"]
    flag_words = ["pirate-flag", "skull-and-cross-bones", "flag", "banner"]
    troublemaker_words = ["troublemaker", "rogue", "rapscallion", "rabble-rouser", "rioter"]
    surprise_words = ["surprise", "wow", "holy-cow", "that's-awesome", "that's-amazing"]
    drink_words = ["have-a-drink", "drink-this", "have-some-water"]
    whale_words = ["whale-sighting", "look-a-whale", "i-see-a-whale", "whale", "orca", "humpback", "whales", "orcas", "humpbacks"]
    cheerful_words = ["cheerful-expression", "yay", "song", "chorus"]
    is_words = ["is", "am", "was", "were", "are"]
    
    lists = [hello_words, attention_words, yes_words, help_words, stop_words, nonsense_words, conversation_words, bottom_words, goodbye_words, luck_words, food_words, rob_words, friend_words, friends_words, gossip_words, exclamation_words, disbelief_words, surprise_words, cheerful_words, nosurvivors_words, alcohol_words, career_words, flag_words, troublemaker_words, drink_words, whale_words, is_words]

    text = str(input("Input a sentence you'd like to piratify! "))
    text = text.lower()
    text_list = []
    text_list = text.split()

    i = 0
    while i < len(text_list):
        for l in lists:
            if text_list[i] in l:
                text_list[i] = l[0]
                break
        i+=1
                
    j = 0
    while j < len(text_list):
        if text_list[j] in pirate_sayings.keys():
            text_list[j] = pirate_sayings.get(text_list[j])
        j+=1
    
    new_text = " "
    new_text = " ".join(text_list)
    new_text = new_text.capitalize()
    print(new_text)
    
    play_again = str(input("Would you like to play again? Aye or nay ")).lower()
    if play_again == "aye":
        talk_like_a_pirate()
        

talk_like_a_pirate()
