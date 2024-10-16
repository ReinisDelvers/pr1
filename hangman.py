'''
1. Meklētā vārda izvēle
    Ar random biliotēku palīdzību dabūs random vārdu no vārdu saraksta vai spēlētājs varēs ievadīt savu vārdu
2. Lietotāja informācijas ievadīšana
    Lietotājs ievadīs informāciju konsolē ar input palīdzību un tā tiks pārbaudīta vai mainīta kur vajadzīgs.
3. Iegūtās informācijas salīdzināšana ar vārdu
    Pēc katra minējuma pārbaudīs vai spēlētājs ir uzminējis pilno vārdu salīdzinot vienu ar otru.
4. Informācijas attēlojums
    Informācija tiks attēlota konsolē, karātavas progresa attēls izsauks no iepriekš izveidotas saraksta 
    un pārējo informāciju mainīs un izprintēs ar spēles gaitu.
5. Spēles beigas un atkārtošana
    Spēles beigās tiks ierakstīta uzvara consolē. Spēli varēs atkārtot atbildod uz konsoles jautājumu.
'''

# Importē random bibliotēku, lai varētu izvēlēties random vārdus
import random

# Saraksts ar visām iespējamajām spēles pozīcijām, lai tās varētu attēlot spēles gaitā
hangmanpictures = [
"""
   +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
""","""
   +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
""","""
   +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
""","""
   +---+
    |   |
    O   |
   /|   |
        |
        |
=========
""","""
   +---+
    |   |
    O   |
   /    |
        |
        |
=========
""","""
   +---+
    |   |
    O   |
        |
        |
        |
=========
""","""
   +---+
    |   |
        |
        |
        |
        |
=========
"""]
# Saraksts ar vārdiem angļu valodā no kuriem tiks randomā paņemts kāds, ja izvēlēsies angļu valodā spēlēt
wordseng = ["able", "about", "account", "acid", "across", "act", "addition", "adjustment", "advertisement", "after", "again", "against", "agreement", "air", "all", "almost", "among", "amount", "amusement", "and", "angle", "angry", "animal", "answer", "ant", "any", "apparatus", "apple", "approval", "arch", "argument", "arm", "army", "art", "as", "at", "attack", "attempt", "attention", "attraction", "authority", "automatic", "awake", "baby", "back", "bad", "bag", "balance", "ball", "band", "base", "basin", "basket", "bath", "be", "beautiful", "because", "bed", "bee", "before", "behaviour", "belief", "bell", "bent", "berry", "between", "bird", "birth", "bit", "bite", "bitter", "black", "blade", "blood", "blow", "blue", "board", "boat", "body", "boiling", "bone", "book", "boot", "bottle", "box", "boy", "brain", "brake", "branch", "brass", "bread", "breath", "brick", "bridge", "bright", "broken", "brother", "brown", "brush", "bucket", "building", "bulb", "burn", "burst", "business", "but", "butter", "button", "by", "cake", "camera", "canvas", "card", "care", "carriage", "cart", "cat", "cause", "certain", "chain", "chalk", "chance", "change", "cheap", "cheese", "chemical", "chest", "chief", "chin", "church", "circle", "clean", "clear", "clock", "cloth", "cloud", "coal", "coat", "cold", "collar", "colour", "comb", "come", "comfort", "committee", "common", "company", "comparison", "competition", "complete", "complex", "condition", "connection", "conscious", "control", "cook", "copper", "copy", "cord", "cork", "cotton", "cough", "country", "cover", "cow", "crack", "credit", "crime", "cruel", "crush", "cry", "cup", "cup", "current", "curtain", "curve", "cushion", "damage", "danger", "dark", "daughter", "day", "dead", "dear", "death", "debt", "decision", "deep", "degree", "delicate", "dependent", "design", "desire", "destruction", "detail", "development", "different", "digestion", "direction", "dirty", "discovery", "discussion", "disease", "disgust", "distance", "distribution", "division", "do", "dog", "door", "doubt", "down", "drain", "drawer", "dress", "drink", "driving", "drop", "dry", "dust", "ear", "early", "earth", "east", "edge", "education", "effect", "egg", "elastic", "electric", "end", "engine", "enough", "equal", "error", "even", "event", "ever", "every", "example", "exchange", "existence", "expansion", "experience", "expert", "eye", "face", "fact", "fall", "false", "family", "far", "farm", "fat", "father", "fear", "feather", "feeble", "feeling", "female", "fertile", "fiction", "field", "fight", "finger", "fire", "first", "fish", "fixed", "flag", "flame", "flat", "flight", "floor", "flower", "fly", "fold", "food", "foolish", "foot", "for", "force", "fork", "form", "forward", "fowl", "frame", "free", "frequent", "friend", "from", "front", "fruit", "full", "future", "garden", "general", "get", "girl", "give", "glass", "glove", "go", "goat", "gold", "good", "government", "grain", "grass", "great", "green", "grey", "grip", "group", "growth", "guide", "gun", "hair", "hammer", "hand", "hanging", "happy", "harbour", "hard", "harmony", "hat", "hate", "have", "he", "head", "healthy", "hear", "hearing", "heart", "heat", "help", "high", "history", "hole", "hollow", "hook", "hope", "horn", "horse", "hospital", "hour", "house", "how", "humour", "I", "ice", "idea", "if", "ill", "important", "impulse", "in", "increase", "industry", "ink", "insect", "instrument", "insurance", "interest", "invention", "iron", "island", "jelly", "jewel", "join", "journey", "judge", "jump", "keep", "kettle", "key", "kick", "kind", "kiss", "knee", "knife", "knot", "knowledge", "land", "language", "last", "late", "laugh", "law", "lead", "leaf", "learning", "leather", "left", "leg", "let", "letter", "level", "library", "lift", "light", "like", "limit", "line", "linen", "lip", "liquid", "list", "little", "living", "lock", "long", "look", "loose", "loss", "loud", "love", "low", "machine", "make", "male", "man", "manager", "map", "mark", "market", "married", "mass", "match", "material", "may", "meal", "measure", "meat", "medical", "meeting", "memory", "metal", "middle", "military", "milk", "mind", "mine", "minute", "mist", "mixed", "money", "monkey", "month", "moon", "morning", "mother", "motion", "mountain", "mouth", "move", "much", "muscle", "music", "nail", "name", "narrow", "nation", "natural", "near", "necessary", "neck", "need", "needle", "nerve", "net", "new", "news", "night", "no", "noise", "normal", "north", "nose", "not", "note", "now", "number", "nut", "observation", "of", "off", "offer", "office", "oil", "old", "on", "only", "open", "operation", "opinion", "opposite", "or", "orange", "order", "organization", "ornament", "other", "out", "oven", "over", "owner", "page", "pain", "paint", "paper", "parallel", "parcel", "part", "past", "paste", "payment", "peace", "pen", "pencil", "person", "physical", "picture", "pig", "pin", "pipe", "place", "plane", "plant", "plate", "play", "please", "pleasure", "plough", "pocket", "point", "poison", "polish", "political", "poor", "porter", "position", "possible", "pot", "potato", "powder", "power", "present", "price", "print", "prison", "private", "probable", "process", "produce", "profit", "property", "prose", "protest", "public", "pull", "pump", "punishment", "purpose", "push", "put", "quality", "question", "quick", "quiet", "quite", "rail", "rain", "range", "rat", "rate", "ray", "reaction", "reading", "ready", "reason", "receipt", "record", "red", "regret", "regular", "relation", "religion", "representative", "request", "respect", "responsible", "rest", "reward", "rhythm", "rice", "right", "ring", "river", "road", "rod", "roll", "roof", "room", "root", "rough", "round", "rub", "rule", "run", "sad", "safe", "sail", "salt", "same", "sand", "say", "scale", "school", "science", "scissors", "screw", "sea", "seat", "second", "secret", "secretary", "see", "seed", "seem", "selection", "self", "send", "sense", "separate", "serious", "servant", "sex", "shade", "shake", "shame", "sharp", "sheep", "shelf", "ship", "shirt", "shock", "shoe", "short", "shut", "side", "sign", "silk", "silver", "simple", "sister", "size", "skin", "skirt", "sky", "sleep", "slip", "slope", "slow", "small", "smash", "smell", "smile", "smoke", "smooth", "snake", "sneeze", "snow", "so", "soap", "society", "sock", "soft", "solid", "some", "son", "song", "sort", "sound", "soup", "south", "space", "spade", "special", "sponge", "spoon", "spring", "square", "stage", "stamp", "star", "start", "statement", "station", "steam", "steel", "stem", "step", "stick", "sticky", "stiff", "still", "stitch", "stocking", "stomach", "stone", "stop", "store", "story", "straight", "strange", "street", "stretch", "strong", "structure", "substance", "such", "sudden", "sugar", "suggestion", "summer", "sun", "support", "surprise", "sweet", "swim", "system", "table", "tail", "take", "talk", "tall", "taste", "tax", "teaching", "tendency", "test", "than", "that", "the", "then", "theory", "there", "thick", "thin", "thing", "this", "thought", "thread", "throat", "through", "through", "thumb", "thunder", "ticket", "tight", "till", "time", "tin", "tired", "to", "toe", "together", "tomorrow", "tongue", "tooth", "top", "touch", "town", "trade", "train", "transport", "tray", "tree", "trick", "trouble", "trousers", "true", "turn", "twist", "umbrella", "under", "unit", "up", "use", "value", "verse", "very", "vessel", "view", "violent", "voice", "waiting", "walk", "wall", "war", "warm", "wash", "waste", "watch", "water", "wave", "wax", "way", "weather", "week", "weight", "well", "west", "wet", "wheel", "when", "where", "while", "whip", "whistle", "white", "who", "why", "wide", "will", "wind", "window", "wine", "wing", "winter", "wire", "wise", "with", "woman", "wood", "wool", "word", "work", "worm", "wound", "writing", "wrong", "year", "yellow", "yes", "yesterday", "you", "young", "Bernhard", "Breytenbach", "Android"]
# Saraksts ar vārdiem latviešu valodā no kuriem tiks randomā paņemts kāds, ja izvēlēsies latviešu valodā spēlēt
wordslv = ["māja", "skola", "auto", "grāmata", "suns", "kaķis", "galds", "krēsls", "logs", "durvis", "ūdens", "maize", "piens", "kafija", "tēja", "ēdiens", "auglis", "dārzenis", "zieds", "koks", "putns","zivs", "dzīvnieks", "debesis", "saule", "mēness", "zvaigzne", "kalns", "upe", "ezers", "jūra", "zeme", "vārds", "teikums", "doma", "frāze", "saruna", "jautājums", "atbilde", "ideja", "vieta","pilsēta", "valsts", "mūzika", "filma", "glezna", "stāsts", "dzeja", "kultūra", "sports", "izglītība","darbs", "laiks", "gadalaiks", "sezona", "ziema", "pavasaris", "vasara", "rudens", "mugura", "sirds","rokas", "kājas", "acis", "mati", "lūpas", "zobi", "smiekli", "sāpes", "prieks", "bēdas", "mīlestība","draugs", "ģimene", "tētis", "mamma", "brālis", "māsa", "bērns", "vecmāmiņa", "vecvectēvs", "māte","tēvs", "uzdevums", "stāsts", "pasaka", "daba", "vide", "pasaules", "ceļojums", "lidojums", "autobuss","trauks", "eļļa", "sviests", "cukurs", "sāls", "pipari", "garšviela", "tvaiks", "cepšana", "vārīšana","ēdienkarte", "restorāns", "kafejnīca", "bārs", "veikals", "tirgus", "sabiedriskā", "transporta", "ceļš","pārvietošanās", "kalendārs", "laikraksts", "žurnāls", "grāmatu", "bibliotēka", "skatuve", "koncerts","izstāde", "vīns", "alus", "šampanietis", "kokteils", "pēcpusdiena", "vakars", "rīts", "pārsteigums","sniegs", "lietus", "vējš", "siltums", "aukstums", "dūmi", "uguns", "sniega", "sniegs", "zāle","ceļmalas", "ceļgali", "kauli", "muskuļi", "sudrabs", "zelts", "bronza", "metāls", "koks", "augs","smarža", "skaņa", "krāsa", "forma", "līnija", "punkti", "apļa", "kvadrāts", "trijstūris", "izteiksme","spriedums", "izvēle", "lēmums", "pieredze", "sajūta", "emocija", "atsauksme", "viedoklis", "diskusija","saruna", "mīts", "pasaka", "vārdi", "tēma", "uzdevums", "izstāde", "izsniegšana", "satiksme", "gaisma","ēna", "spēle", "kārtis", "darbība", "spēlētājs", "kāzu", "balle", "pasākums", "skats", "jautājums","paziņojums", "ziņa", "reklāma", "informācija", "pārskats", "pētījums", "apspriešana", "komentārs","ideoloģija", "tehnoloģija", "metode", "prakse", "rezultāts", "dati", "pētījums", "teorija", "apmācība","izglītība", "skola", "kolēģis", "studijas", "universitāte", "kursa", "bakalaurs", "maģistrs", "doktors","apliecinājums", "sertifikāts", "nosacījums", "līgums", "darījums", "darba", "vietas", "ražošanas","pakalpojumi", "tirdzniecība", "ekonomika", "finanses", "izmaksa", "peļņa", "ieguldījums", "investīcijas","pārdošana", "iegāde", "uzņēmums", "kompānija", "projekts", "mārketings", "reklāma", "zīmols", "zīmola","attiecības", "partnerība", "klients", "patērētājs", "prece", "pakalpojums", "piegādātājs", "uzņēmējs","darbinieks", "birojs", "darbība", "profesija", "amats", "aizsardzība", "drošība", "tiesības", "likums","likums", "juridiskā", "pārkāpums", "pārkāpums", "nosacījums", "tiesāšanās", "atlīdzība", "apdrošināšana","risks", "lēmums", "strīds", "tiesa", "tiesnesis", "advokāts", "jurists", "atbildība", "sodīts", "sodi","soda", "dekrēts", "izpilde", "pārbaude", "izmeklēšana", "pārkāpums", "izpilddirektors", "pārvaldība","pārvalde", "darbība", "politika", "sociālais", "ekonomiskā", "konkurence", "tirgus", "produkti","ražotāji", "pakalpojumi", "piegādātāji", "investori", "klienti", "patērētāji", "uzņēmēji", "darbinieki","pašnodarbinātie", "nodokļi", "nodokļu", "sistēma", "fiskālā", "politika", "regulējums", "noteikums","normas", "pārliecināšanās", "pārskati", "atbilstība", "apstrāde", "produkcija", "piegāde", "sadarbība","izpēte", "pētniecība", "pētnieks", "izpētes", "projekts", "finansējums", "programmas", "fondi","investīcijas", "ražošana", "darbnīca", "uzņēmums", "uzņēmējdarbība", "tehnoloģijas", "iekārtas","kvalitāte", "standarts", "uzticība", "pašvaldība", "komiteja", "padome", "apgāde", "pārvalde","pārvaldība", "viss", "organizācija", "apvienība", "savienība", "centrs", "nodaļa", "struktūra","pārraudzība", "uzraudzība", "izpilde", "pārbaude", "izsniegšana", "sertifikācija", "reģistrācija","apliecinājums", "paziņojums", "pārskats", "analīze", "pētījums", "izdevums", "ziņojums", "lēmums","saturs", "atbalsts", "attiecības", "komunikācija", "informācija", "ziņas", "ziņu", "nepieciešamība","izpilde", "piekļuve", "pakalpojums", "mājas", "tehnoloģija", "uzņēmējdarbība", "finanses","izdevumi", "investīcijas", "darbības", "pārvaldība", "komanda", "tehnoloģiju", "atbalsts", "pārdošana","piegāde", "reklāma", "zināšanas", "izglītība", "darbs", "mācības"]

# x ir mainīgais lai while loop strādātu līdz tā tiek apstādināta mainīgo nomainot par citu skaitli kā 1 
x=1
# y ir mainīgais kura vērtība kas nosaka vai spēlētājs spēlēs spēli
y=0

# While loops kurā atkārtosies spēles kods līdz spēlētājs izvēlēsies nespēlēt
while x==1:
    # Mainīgajam y piešķir vērtību ko spēlētājs ievada (kurā lielos burtus pārvērš uz mazajiem burtiem, lai būtu vienalga raksta ar lielajiem vai mazajiem burtiem) 
    y = input("Do you want to play hangman y/n: ").lower()

    # Pārbauda vai palaist spēli skatoties uz ievades vērtību
    if y=="y":
        # t ir mainīgais lai while loop strādātu līdz tā tiek apstādināta mainīgo nomainot par citu skaitli kā 1  
        t=1
        # l ir mainīgais lai while loop strādātu līdz tā tiek apstādināta mainīgo nomainot par citu skaitli kā 1 
        l=1
        # Mainīgajam m piešķir vērtību ko spēlētājs ievada (kurā lielos burtus pārvērš uz mazajiem burtiem, lai būtu vienalga raksta ar lielajiem vai mazajiem burtiem), kas tiks izmantots lai spēlētājs izvēlētos kādā veidā iegūs minējamo vārdu
        m = input("""For random english word input eng
For random latvian word input lv 
For your own word input mine: """).lower()
        # Mainīgais lifesleft nosaka cik daudz dzīvības spēlētājam būs
        lifesleft = 6
        # Izveido sarakstu kuram pievienos visus minētos burtus
        guessedletterlist = []
        # Izveido mainīgo kura vērtība būs vienāda ar to cik tālu spēlētājs ir atminējis
        wordprogress = ""
        # While loops kurā prasīs spēlētājam kādā veidā iegūs minējamo vārdu
        
        while l==1:
            # Ja spēlētājs grib minēt angļu vārdu ievadīs "eng" consolē
            if m=="eng":
                # Mainīgajam selectedword nomainīs vērtību uz vienu no angļu vārdiem no saraksta wordseng
                selectedword = wordseng[random.randint(0,len(wordseng))]
                # Nomaina l vērtību uz 0 izies arā no šobrīdējā while loopa
                l=0
            # Ja spēlētājs grib minēt latviešu vārdu ievadīs "lv" consolē
            elif m=="lv":
                # Mainīgajam selectedword nomainīs vērtību uz vienu no latviešu vārdiem no saraksta wordslv
                selectedword = wordslv[random.randint(0,len(wordslv))]
                # Nomaina l vērtību uz 0 izies arā no šobrīdējā while loopa
                l=0
            # Ja spēlētājs grib pats ievadīt mināmo vārdu ievadīs "mine" consolē
            elif m=="mine":
                # Mainīgajam selectedword nomainīs vērtību uz spēlētāja ievadīto vērtību
                selectedword = input("Write a word you want to guess: ")
                # Nomaina l vērtību uz 0 izies arā no šobrīdējā while loopa
                l=0
            # Ja m vērtība neapmierina nevienu no iepriekšējām pārbaudēm, tad spēlētājam parsīs ievadīt atkārtoti
            else:
                # Prasīs spēlētajam vēlreiz ievadīt kādā veidā gribēs iegūs minējamo vārdu un pievienos to mainīgajam m (un vērtībai lielos burtus pārvērš uz mazajiem burtiem, lai būtu vienalga raksta ar lielajiem vai mazajiem burtiem) 
                m = input("""For random english word input eng
For random latvian word input lv 
For your own word input mine: """).lower()
                
        # Mainīgajam selectedword nomainīs visus lielos burtus uz mazajiem, lai nebūtu tie nebūtu jāmin atsevišķi
        selectedword = selectedword.lower()
        # Consolē izprintē pareizo karātavu attēlu atkarībā no atlikušajām dzīvībām
        print(hangmanpictures[lifesleft])
        # Consolē izprintē atlikušajās dzīvības
        print(f"Lifes left {lifesleft}")
        # Strings kurā saglabāts minējamā vārda garums
        wordlen = "_"*len(selectedword)
        # Consolē izprintē apakšsvītras lai redzētu cik garš ir redzamais vārds
        print(f"Word progress {wordlen}")
        # While loops kurā norisināsies spēle līdz zaudēs vai vinēs

        while t==1:
            # Pārbauda vai spēlētājs ir vinējis spēli
            if selectedword == wordprogress:
                # Izprintē visu vajadzīgo informāciju
                print(hangmanpictures[lifesleft])
                print(f"Lifes left {lifesleft}")
                print("Word guessed")
                print(f"The word was {selectedword}")
                print(f"Guessed letters {guessedletterlist}")
                # Nomaina t vērtību uz 0 izies arā no šobrīdējā while loopa
                t=0
            
            # Pārbauda vai spēlētājs ir dzīvs
            elif lifesleft > 0:
                # c ir mainīgais kuru maina lai pateiktu vai spēlētājs ir uzminējis burtu
                c=0
                # n ir mainīgais lai while loop strādātu līdz tā tiek apstādināta mainīgo nomainot par citu skaitli kā 1 
                n=1
                # Mainīgajam letterguessed piešķir vērtību ko spēlētājs ievada (kurā lielos burtus pārvērš uz mazajiem burtiem, lai būtu vienalga raksta ar lielajiem vai mazajiem burtiem), kas tiks izmantots lai spēlētu spēli
                letterguessed = input("Guess a letter: ").lower()

                # While loops kurā pārbauda vai letterguessed vērtība atbilst prasībām
                while n==1:
                    # Pārbauda vai spēlētājs burtu jau ir minējis
                    if letterguessed in guessedletterlist:
                        # Liek minēt vēlreiz
                        letterguessed = input("You already guessed this letter: ").lower()
                    # Pārbauda vai spēlētājs ievadīja tikai vienu burtu
                    elif 1 != len(letterguessed):
                        # Liek minēt vēlreiz
                        letterguessed = input("Guess one letter at a time: ").lower()
                    else:
                        # Nomaina n vērtību uz 0 izies arā no šobrīdējā while loopa
                        n=0
                
                # Pievieno minēto burtu minēto burtu sarakstam
                guessedletterlist += letterguessed
                # Nomaina wordprgress uz tukšu sttringu, lai veidotu jaunu, tas attēlos uzminētos burtus apakšsvītru vietā
                wordprogress = ""

                # For loops kurā tiek pievienot jauna vērtība wordprogress
                # Iet cauri izvēlētajam vārdam pa burtiem un to uzliek kā i vērtību  
                for i in selectedword:
                    # Pārbauda vai i ir vienāds ar kādu no vērtībām guessedletterlist
                    if i in guessedletterlist:
                        # Pievieno pareizi uzminēto burtu
                        wordprogress += i
                    # Ja tas nav
                    else:
                        # Pievieno apakšsvītru
                        wordprogress += "_"
                
                # Pārbauda vai spēlētājs uzminēja burtu pareizi
                # Iet cauri wordprogress pa burtiem un to uzliek kā i vērtību  
                for i in wordprogress:
                    # Pārbauda vai i ir vienāds ar kadu no minētajiem burtiem
                    if i == letterguessed:
                        # Nomaina c vērtību uz 1, kas nozīmē ka ir uzminēts pareizi 
                        c=1

                # Pārbauda vai spēlētājs neuzminēja burtu pareizi
                if c==0:
                    # Atņem vienu dzīvību
                    lifesleft-=1

                # Izprintē visu vajadzīgo informāciju
                print(hangmanpictures[lifesleft])
                print(f"Lifes left {lifesleft}")
                print(f"Word progress {wordprogress}")
                print(f"Guessed letters {guessedletterlist}")

            # Pārbauda vai spēlētājs ir zaudējis spēli
            elif lifesleft == 0:
                # Izprintē visu vajadzīgo informāciju
                print(hangmanpictures[lifesleft])
                print(f"Lifes left {lifesleft}")
                print("Game over")
                print(f"Word progress {wordprogress}")
                print(f"The word was {selectedword}")
                print(f"Guessed letters {guessedletterlist}")
                # Nomaina t vērtību uz 0 izies arā no šobrīdējā while loopa
                t=0
    
    # Pārbauda vai spēlētājs negrib spēlēt spēli
    elif y=="n":
        # Nomaina x vērtību uz 0 izies arā no šobrīdējā while loopa
        x=0