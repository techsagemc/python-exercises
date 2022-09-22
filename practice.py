from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Michael. We hope you had a great day of work. It's time to submit your employee wellness statement.")
engine.runAndWait()

print("Enter your wellness statement: ")
engine.say("Enter your wellness statement.")
engine.runAndWait()
phrase = input(">")
blob = TextBlob(phrase)
while blob.sentiment.polarity < 0.5:
    print("Try saying that a little nicer please..")
    engine.say("Try saying that a little nicer please")
    engine.runAndWait()
    print("Enter your wellness statement: ")
    engine.say("Enter your wellness statement.")
    engine.runAndWait()
    phrase = input(">") 
    blob = TextBlob(phrase)

print("We appreciate that. You are a valuable asset to this team!!")
engine.say("We appreciate that. You are a valuable asset to this team!!")
engine.runAndWait()


