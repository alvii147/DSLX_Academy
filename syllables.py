import json
import syllables
import random
import azure.cognitiveservices.speech as speechsdk

with open('azurekeys.json') as f:
    keys = json.load(f)

speech_key, service_region = keys['KEY1'], keys['REGION']
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

words = {"kitten":2, "school":1, "cat":1, "rat":1, "morning":2, "September":3, "year":1, "hospital":3, "doctor":2, "Saturday":3, "Sunday":2, "Monday":2, "Tuesday":2, "Wednesday":3, "Thursday":2, "Friday":2, "January":4, "February":4, "March":1, "April":2, "May":1, "June":1, "July":1, "August":2, "October":3, "November":3, "December":3, "bedding":2, "wedding":2, "chicken":2, "holly":2, "tomato":3}

def num_syllables():
    status = 'n'
    while status == 'n':
        # Check speech
        word = random.choice(list(words.keys()))
        print("Say the following word: {}".format(word))
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        result = speech_recognizer.recognize_once_async().get()
        result = result.text.strip('.').strip('?').strip('!').strip(',').lower()
        # ^^ POTENTIAL PUNCTUATION BUG HERE ^^
        print(result)
        print('You said: {}'.format(result))
        if result == word.lower():
            print('Good job!')
        else:
            print('Not quite!')

        # Check syllables
        actual = words[word]
        guess = input('How many syllables are in {}? '.format(word))
        try:
            guess = int(guess)
        except:
            print("\nPlease enter a digit from 0 to 9")
            guess = input('How many syllables are in {}? '.format(word))
            guess = int(guess)
        if actual == guess:
            print('Correct!')
        else:
            print('Incorrect. The number of syllables is {}.'.format(actual))

        # Check if user is tired
        status = input('Are you tired? Enter (y/n): ')
        if status == 'y':
            break

if __name__ == "__main__":
    num_syllables()
