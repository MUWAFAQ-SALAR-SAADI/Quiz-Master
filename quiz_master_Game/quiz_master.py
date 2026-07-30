import random
import time


# This class acts as a template for every single question.
class Question:

  def __init__(self, prompt, choices, answer, difficulty, hint):
    self.prompt = prompt  # The actual question text
    self.choices = choices  # List of options
    self.answer = answer  # The correct letter
    self.difficulty = difficulty  # "Easy", "Medium", or "Hard"
    self.hint = hint


# This class stores all the information about a specific player.
class Player:

  def __init__(self, name):
    self.name = name  # Player's name
    self.score = 0  # Current score
    self.correct = 0  # Right answers
    self.total = 0  # Total questions tried
    self.times = []  # How much time taken
    self.achievements = []  # List of achievements earned

  # Method to unlock a badge/achievement
  def unlock(self, title):
    # Only add badge if not won already
    if title not in self.achievements:
      self.achievements.append(title)
      print(f"Achievement Unlocked: {title}")


# Store questions in lists. Each item is a 'Question' object.
science = [
    Question("Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "B", "Easy", "4th planet"),
    Question("H2O is?", ["Oxygen", "Salt", "Water", "Hydrogen"], "C", "Easy", "Liquid"),
    Question("Force pulling objects?", ["Energy", "Gravity", "Speed", "Mass"], "B", "Easy", "Apple"),
    Question("Gas plants absorb?", ["O2", "CO2", "H2", "N2"], "B", "Easy", "Photosynthesis"),
    Question("Heart function?", ["Think", "Breathe", "Pump blood", "Digest"], "C", "Easy", "Beats"),
    Question("Earth shape?", ["Flat", "Cube", "Sphere", "Triangle"], "C", "Easy", "Round"),
    Question("Hardest natural substance?", ["Gold", "Iron", "Diamond", "Silver"], "C", "Easy", "Ring stone"),
    Question("Center of atom?", ["Shell", "Nucleus", "Electron", "Skin"], "B", "Easy", "Core"),
    Question("Largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"], "B", "Easy", "Ocean"),
    Question("Freezing point of water?", ["0", "10", "-10", "100"], "A", "Easy", "Ice"),
    Question("Boiling point of water?", ["50", "100", "150", "200"], "B", "Medium", "\u00b0C"),
    Question("Vitamin from sun?", ["A", "B", "C", "D"], "D", "Medium", "Bones"),
    Question("DNA found in?", ["Cell wall", "Nucleus", "Membrane", "Cytoplasm"], "B", "Medium", "Center"),
    Question("Planet with rings?", ["Mars", "Saturn", "Venus", "Mercury"], "B", "Medium", "Gas Giant"),
    Question("Chemical symbol for Gold?", ["Go", "Ag", "Au", "Fe"], "C", "Medium", "Latin 'Aurum"),
    Question("Powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Wall"], "B", "Medium", "Energy"),
    Question("Speed of sound is faster in?", ["Air", "Water", "Steel", "Vacuum"], "C", "Medium", "Density"),
    Question("Study of fungus?", ["Biology", "Mycology", "Virology", "Botany"], "B", "Medium", "Mushrooms"),
    Question("Nearest star to Earth?", ["Alpha Centauri", "Sun", "Sirius", "Vega"], "B", "Medium", "Daylight"),
    Question("Human body bone count?", ["200", "206", "212", "198"], "B", "Medium", "Adult"),
    Question("Speed of light symbol?", ["v", "c", "s", "x"], "B", "Hard", "Einstein"),
    Question("Most abundant gas in air?", ["Oxygen", "Nitrogen", "Argon", "CO2"], "B", "Hard", "78%"),
    Question("Smallest unit of matter?", ["Molecule", "Atom", "Quark", "Cell"], "C", "Hard", "Sub-atomic"),
    Question("Theory of Relativity?", ["Newton", "Einstein", "Tesla", "Darwin"], "B", "Hard", "E=mc^2"),
    Question("Who discovered Penicillin?", ["Pasteur", "Fleming", "Curie", "Edison"], "B", "Hard", "Mold"),
    Question("Value of Pi (approx)?", ["3.12", "3.14", "3.16", "3.18"], "B", "Hard", "Circle"),
    Question("Lightest element?", ["Helium", "Hydrogen", "Lithium", "Boron"], "B", "Hard", "H"),
    Question("Rare blood type?", ["O+", "A+", "AB-", "B-"], "C", "Hard", "Universal Recipient"),
    Question("First element on periodic table?", ["Helium", "Hydrogen", "Oxygen", "Carbon"], "B", "Hard", "No. 1"),
    Question("Absolute Zero in Celsius?", ["-100", "-273.15", "-500", "0"], "B", "Hard", "Kelvin 0"),
]

history = [
    Question("First US president?", ["Lincoln", "Washington", "Adams", "Jefferson"], "B", "Easy", "$1 bill"),
    Question("Pyramids built by?", ["Romans", "Greeks", "Egyptians", "Persians"], "C", "Easy", "Pharaoh"),
    Question("Roman capital?", ["Athens", "Rome", "Paris", "Berlin"], "B", "Easy", "Italy"),
    Question("Cleopatra was?", ["Queen", "General", "Writer", "Slave"], "A", "Easy", "Egypt"),
    Question("Discovered America?", ["Columbus", "Magellan", "Cook", "Drake"], "A", "Easy", "1492"),
    Question("Ancient Greek games?", ["World Cup", "Olympics", "Superbowl", "Cricket"], "B", "Easy", "Zeus"),
    Question("Country of Samurai?", ["China", "Korea", "Japan", "Vietnam"], "C", "Easy", "Sword"),
    Question("Who built the Great Wall?", ["Japan", "Mongolia", "China", "India"], "C", "Easy", "Dragon"),
    Question("Napoleon was?", ["French", "British", "German", "Spanish"], "A", "Easy", "Short"),
    Question("Ship that hit an iceberg?", ["Titanic", "Olympic", "Britannic", "Queen Mary"], "A", "Easy", "Movie"),
    Question("Titanic sank?", ["1910", "1911", "1912", "1913"], "C", "Medium", "Iceberg"),
    Question("WWII ended?", ["1943", "1944", "1945", "1946"], "C", "Medium", "Mid 40s"),
    Question("Cold War?", ["USA-USSR", "UK-France", "China-Japan", "Germany-Italy"], "A", "Medium", "Superpowers"),
    Question("Berlin Wall fell?", ["1987", "1988", "1989", "1990"], "C", "Medium", "80s"),
    Question("First man on Moon?", ["Gagarin", "Armstrong", "Aldrin", "Collins"], "B", "Medium", "Apollo 11"),
    Question("Year of US Independence?", ["1770", "1776", "1780", "1800"], "B", "Medium", "July 4"),
    Question("Iron Lady?", ["Thatcher", "Merkel", "Queen Elizabeth", "Madonna"], "A", "Medium", "UK PM"),
    Question("Currency before Euro in Germany?", ["Franc", "Lira", "Mark", "Pound"], "C", "Medium", "DM"),
    Question("Founder of Mongol Empire?", ["Kublai", "Genghis Khan", "Attila", "Timur"], "B", "Medium", "Khan"),
    Question("Black Death was a?", ["War", "Plague", "Famine", "Flood"], "B", "Medium", "Rats"),
    Question("Iliad author?", ["Plato", "Homer", "Socrates", "Aristotle"], "B", "Hard", "Poet"),
    Question("Renaissance began in?", ["France", "Italy", "Germany", "Spain"], "B", "Hard", "Art"),
    Question("French Revolution start?", ["1789", "1799", "1805", "1776"], "A", "Hard", "Bastille"),
    Question("Last Tsar of Russia?", ["Ivan", "Peter", "Nicholas II", "Alexander"], "C", "Hard", "Romanov"),
    Question("Year WWI started?", ["1912", "1914", "1916", "1918"], "B", "Hard", "Archduke"),
    Question("Who painted Mona Lisa?", ["Michelangelo", "Raphael", "Da Vinci", "Donatello"], "C", "Hard", "Leo"),
    Question("Longest reigning UK monarch?", ["Victoria", "Elizabeth II", "George III", "Henry VIII"], "B", "Hard", "70 years"),
    Question("Alexander the Great from?", ["Rome", "Macedonia", "Sparta", "Troy"], "B", "Hard", "Greece"),
    Question("Fall of Constantinople?", ["1453", "1492", "1204", "1517"], "A", "Hard", "Ottomans"),
    Question("Civil Rights leader 'Dream'?", ["Malcolm X", "MLK Jr", "Rosa Parks", "Obama"], "B", "Hard", "Luther"),
]

english = [
    Question("Synonym of happy?", ["Sad", "Glad", "Angry", "Tired"], "B", "Easy", "Smile"),
    Question("Past of go?", ["Go", "Gone", "Went", "Going"], "C", "Easy", "Irregular"),
    Question("Plural of child?", ["Childs", "Children", "Childes", "Child"], "B", "Easy", "Grammar"),
    Question("Opposite of hot?", ["Warm", "Cold", "Cool", "Freeze"], "B", "Easy", "Weather"),
    Question("Better is?", ["Good", "Best", "Comparative", "Adverb"], "C", "Easy", "Grammar"),
    Question("He ___ playing.", ["is", "are", "am", "be"], "A", "Easy", "Verb"),
    Question("Vowel letter?", ["B", "C", "A", "D"], "C", "Easy", "AEIOU"),
    Question("Antonym of Big?", ["Huge", "Small", "Giant", "Large"], "B", "Easy", "Tiny"),
    Question("Cat sound?", ["Bark", "Moo", "Meow", "Roar"], "C", "Easy", "Pet"),
    Question("Plural of mouse?", ["Mouses", "Mice", "Mousies", "Mees"], "B", "Easy", "Rodent"),
    Question("Noun is?", ["Action", "Name", "Time", "Place"], "B", "Medium", "Person"),
    Question("Correct spelling?", ["Recieve", "Receive", "Receve", "Receeve"], "B", "Medium", "Rule"),
    Question("Break the ice?", ["Freeze", "Start talk", "Destroy", "Run"], "B", "Medium", "Idiom"),
    Question("Piece of cake?", ["Food", "Easy", "Hard", "Dessert"], "B", "Medium", "Idiom"),
    Question("Past participle of Write?", ["Wrote", "Written", "Writed", "Writes"], "B", "Medium", "V3"),
    Question("Which is an adjective?", ["Run", "Quickly", "Beautiful", "Dog"], "C", "Medium", "Descriptive"),
    Question("Homophone for 'See'?", ["Sea", "Saw", "Seen", "Say"], "A", "Medium", "Ocean"),
    Question("Bite the bullet?", ["Eat", "Endure pain", "Shoot", "Die"], "B", "Medium", "Brave"),
    Question("Collective noun for lions?", ["Pack", "Herd", "Pride", "School"], "C", "Medium", "King"),
    Question("Prefix 'Re' means?", ["Not", "Again", "Before", "After"], "B", "Medium", "Repeat"),
    Question("Adverb describes?", ["Noun", "Verb", "Adj", "Pronoun"], "B", "Hard", "How"),
    Question("Meaning of 'Benevolent'?", ["Cruel", "Kind", "Rich", "Poor"], "B", "Hard", "Good"),
    Question("Synonym for 'Lethargic'?", ["Energetic", "Lazy/Tired", "Happy", "Fast"], "B", "Hard", "Slow"),
    Question("What is a stanza?", ["Poem paragraph", "Sentence", "Word", "Title"], "A", "Hard", "Poetry"),
    Question("Correct: 'She have gone.'", ["should", "must", "can", "is"], "A", "Hard", "Modal"),
    Question("Palindrome example?", ["Hello", "Racecar", "World", "Python"], "B", "Hard", "Backwards"),
    Question("Meaning of 'Ephemeral'?", ["Eternal", "Short-lived", "Heavy", "Light"], "B", "Hard", "Time"),
    Question("The 'Protagonist' is?", ["Villain", "Hero", "Sidekick", "Narrator"], "B", "Hard", "Main"),
    Question("Oxymoron example?", ["Big Giant", "Deafening Silence", "Red Apple", "Fast Car"], "B", "Hard", "Opposite"),
    Question("To 'let the cat out of the bag'?", ["Free pet", "Reveal secret", "Go shopping", "Clean"], "B", "Hard", "Secret"),
]

german = [
    Question("Hallo?", ["Bye", "Hello", "Thanks", "Sorry"], "B", "Easy", "Greeting"),
    Question("Danke?", ["Please", "Thanks", "Yes", "No"], "B", "Easy", "Polite"),
    Question("Ja?", ["No", "Yes", "Why", "When"], "B", "Easy", "Agree"),
    Question("Water?", ["Milch", "Bier", "Wasser", "Saft"], "C", "Easy", "Clear"),
    Question("Good morning?", ["Guten Abend", "Guten Morgen", "Hallo", "Nacht"], "B", "Easy", "Morning"),
    Question("Ich bin?", ["You are", "I am", "He is", "We are"], "B", "Easy", "Self"),
    Question("Haus means?", ["Car", "Tree", "House", "Chair"], "C", "Easy", "Home"),
    Question("Nein?", ["Nine", "No", "New", "Near"], "B", "Easy", "Negative"),
    Question("Eins, zwei...?", ["Drei", "Vier", "F\u00fcnf", "Sechs"], "A", "Easy", "Three"),
    Question("Rot means?", ["Blue", "Red", "Rat", "Road"], "B", "Easy", "Color"),
    Question("Bitte?", ["Sorry", "Please", "Thanks", "Hello"], "B", "Medium", "Request"),
    Question("Danke sch\u00f6n?", ["Hello", "Thanks a lot", "Bye", "Please"], "B", "Medium", "Grateful"),
    Question("German alphabet?", ["24", "25", "26", "30"], "C", "Medium", "Same"),
    Question("Auf Wiedersehen?", ["Hello", "Good bye", "Good night", "Welcome"], "B", "Medium", "See again"),
    Question("Der Hund?", ["The Cat", "The Dog", "The Bird", "The Fish"], "B", "Medium", "Bark"),
    Question("Die Katze?", ["The Cat", "The Car", "The Cake", "The City"], "A", "Medium", "Meow"),
    Question("Guten Appetit?", ["Good night", "Enjoy meal", "Good luck", "Cheers"], "B", "Medium", "Food"),
    Question("Entschuldigung?", ["Excuse me", "Please", "Thanks", "Yes"], "A", "Medium", "Sorry"),
    Question("Wo ist...?", ["Who is", "Where is", "What is", "When is"], "B", "Medium", "Place"),
    Question("Ich liebe dich?", ["I hate you", "I love you", "I like it", "I see you"], "B", "Medium", "Love"),
    Question("Article for Girl (M\u00e4dchen)?", ["Der", "Die", "Das", "Den"], "C", "Hard", "Neutral"),
    Question("Capital of Germany?", ["Munich", "Berlin", "Hamburg", "Frankfurt"], "B", "Hard", "Wall"),
    Question("Prost means?", ["Hello", "Cheers", "Thanks", "Stop"], "B", "Hard", "Drink"),
    Question("Krankenhaus?", ["School", "Hospital", "Church", "House"], "B", "Hard", "Sick House"),
    Question("Schmetterling?", ["Fly", "Butterfly", "Butter", "Bird"], "B", "Hard", "Insect"),
    Question("How many states in Germany?", ["10", "12", "16", "20"], "C", "Hard", "Bundesl\u00e4nder"),
    Question("Verstehen Sie?", ["Do you understand?", "Are you standing?", "Who are you?", "Go away"], "A", "Hard", "Formal"),
    Question("Past tense of 'haben'?", ["Hatte", "Habe", "Hat", "Habt"], "A", "Hard", "Had"),
    Question("What is 'Das Auto'?", ["The Bus", "The Car", "The Train", "The Bike"], "B", "Hard", "VW"),
    Question("Oktoberfest is in?", ["Berlin", "Munich", "Cologne", "Vienna"], "B", "Hard", "Beer"),
]

# This dictionary divides the question lists into their categories
database = {
    "Science": science,
    "History": history,
    "Languages": {"English": english, "German": german},
}


# Class for handling the quiz engine
class Quiz:

  def __init__(self, db, players, qn):
    self.db = db  # The entire database of questions
    self.players = players  # The list of players playing
    self.qn = qn  # How many questions per round
    self.session_start_time = time.time()  # Record the time the game started

  def points(self, d):
    return {"Easy": 10, "Medium": 20, "Hard": 30}.get(d, 10)

  # --- Menu System ---
  def select_pool(self):
    print("Available Sections:", list(self.db.keys()))
    while True:
      sec = input("Choose Section: ").strip().capitalize()
      if sec in self.db:
        break
      print("Invalid section, try again.")

    if sec == "Languages":
      print("Languages:", list(self.db["Languages"].keys()))
      while True:
        lang = input("Choose Language: ").strip().capitalize()
        if lang in self.db["Languages"]:
          return self.db["Languages"][lang]
        print("Invalid language.")
    else:
      return self.db[sec]

  # --- Round Manager ---
  def play_round(self):
    pool = self.select_pool()
    actual_qn = min(self.qn, len(pool))

    print("--- Classic Mode ---")

    for p in self.players:
      print(f"Player's Turn: {p.name}")
      questions = random.sample(pool, actual_qn)
      for q in questions:
        self.ask_question(p, q)

  # --- Question Logic ---
  def ask_question(self, p, q):
    print(f"\n[{q.difficulty}] {q.prompt}")

    for i, c in enumerate(q.choices):
      print(f"  {chr(65+i)}. {c}")

    start = time.time()
    ans = input("Answer (A/B/C/D) or 'HINT': ").upper().strip()
    elapsed = time.time() - start

    p.total += 1
    p.times.append(elapsed)

    score_val = self.points(q.difficulty)

    if ans == "HINT":
      print("HINT:", q.hint)
      score_val //= 2
      ans = input("Final Answer: ").upper().strip()

    if ans == q.answer:
      p.score += score_val
      p.correct += 1
      print(f"Correct! (+{score_val} points)")

      if elapsed <= 3:
        p.unlock("Fast Thinker")
      if p.score >= 50:
        p.unlock("Rising Star")
    else:
      print(f"Wrong! The correct answer was: {q.answer}")

  # Show Results (Leaderboard after round)
  def show_results(self):
    print("\n--- Round Standings ---")
    sorted_p = sorted(self.players, key=lambda x: x.score, reverse=True)
    for p in sorted_p:
      print(f"  {p.name}: {p.score} points")

  # Final Report (End of Game)
  def final_report(self):
    session_time = time.time() - self.session_start_time
    print("\n--- Final Report ---")
    print(f"Total Game Time: {session_time/60:.1f} minutes")

    with open("statistics.txt", "w") as f:
      f.write(f"Session Time: {session_time:.1f}s\n")

      sorted_players = sorted(self.players, key=lambda x: x.score, reverse=True)
      for i, p in enumerate(sorted_players, 1):
        acc = (p.correct / p.total * 100) if p.total > 0 else 0
        avg = (sum(p.times) / len(p.times)) if p.times else 0
        total_think_time = sum(p.times)

        print(f"\n#{i} {p.name}")
        print(f"Final Score: {p.score}")
        print(f"Accuracy: {acc:.1f}%")
        print(f"Total Thinking Time: {total_think_time:.2f}s")
        print(f"Avg Speed: {avg:.2f} sec/question")
        if p.achievements:
          print(f"Badges: {', '.join(p.achievements)}")

        f.write(f"  {p.name} | Score: {p.score} | Acc: {acc:.1f}%\n")

    print("\nStatistics saved to 'statistics.txt'")


# Start the game in try statement to avoid crashing on error
try:
  print("QUIZ MASTER | FULL EDITION 2025 \n")
  n_input = input("Number of Players: ")

  if not n_input.isdigit():
    n_input = "1"
  n = int(n_input)

  players = []
  for i in range(n):
    name = input(f"Name for Player {i+1}: ")
    players.append(Player(name))

  qn_input = input("Questions per round: ")
  if qn_input.isdigit():
    qn = int(qn_input)
  else:
    qn = 5

  game = Quiz(database, players, qn)

  while True:
    game.play_round()
    game.show_results()
    print("\n" + "-" * 30)

    cont = input("Play another round? (y/n) ").lower()
    if cont != "y":
      break

  game.final_report()
  input("\nPress Enter to exit...")

except Exception as e:
  print(f"An error occurred: {e}")
