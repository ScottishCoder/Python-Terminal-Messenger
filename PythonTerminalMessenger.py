
try:

	import keyboard
	from playsound import playsound
	import os
	from twilio.rest import Client
	import pyttsx3
	import threading

except OSError:
	print('you done goofed')
	print('For this to work, I need to install some libaries')
	choice = input('Proceed to install libaries? y or n ')
	if choice == 'y':
		os.system('pip install keyboard')
		os.system('pip install playsound')
		os.system('pip install twilio')
		os.system('pip install pyttsx3')


class Communicator:
	def __init__(self, message, account_sid, auth_token, recipient, sender):
		self.message = message
		self.account_sid = account_sid
		self.auth_token = auth_token
		self.sender = sender
		self.recipient = recipient

	def display_data(self):
		print(self.recipient)
		print(self.message)

	def confirmation(self):
		engine = pyttsx3.init()
		engine.say("Your message reads")
		engine.say(self.message)
		engine.runAndWait()
		proceed = input('Do you want to send this message? y or n ')
		if proceed == "y":
			self.send_message()
		else:
			pass

	def send_message(self):
		client = Client(self.account_sid, self.auth_token)
		message = client.messages.create(body=self.message,from_=self.sender,to=self.recipient)
		if message:
			print('message sent successfully!')
			playsound('successsend.mp3')
		else:
			print('something happened!')
			playsound('error.mp3')

class ThreadListener:

	def __init__(self):

		self.running = True

	
	def keyListener(self):

		while self.running:
			if keyboard.is_pressed('1'):
				playsound('DTMFTones/dtmf-1.mp3')
			elif keyboard.is_pressed('2'):
				playsound('DTMFTones/dtmf-2.mp3')
			elif keyboard.is_pressed('3'):
				playsound('DTMFTones/dtmf-3.mp3')
			elif keyboard.is_pressed('4'):
				playsound('DTMFTones/dtmf-4.mp3')
			elif keyboard.is_pressed('5'):
				playsound('DTMFTones/dtmf-5.mp3')
			elif keyboard.is_pressed('6'):
				playsound('DTMFTones/dtmf-6.mp3')
			elif keyboard.is_pressed('7'):
				playsound('DTMFTones/dtmf-7.mp3')
			elif keyboard.is_pressed('8'):
				playsound('DTMFTones/dtmf-8.mp3')
			elif keyboard.is_pressed('9'):
				playsound('DTMFTones/dtmf-9.mp3')
			elif keyboard.is_pressed('0'):
				playsound('DTMFTones/dtmf-0.mp3')
			elif keyboard.is_pressed('+'):
				playsound('DTMFTones/dtmf-hash.mp3')
			elif keyboard.is_pressed('esc'):
				break
		
		return False


	def toneSound(self):
		while self.running:
			playsound('dialtone.mp3')
		return False

	def terminate(self):
		self.running = False



def main():


	dialer = ThreadListener()
	# Create threads to add tone dialer sound effect
	thread = threading.Thread(target=dialer.keyListener)
	toneDialThread = threading.Thread(target=dialer.toneSound)
	

	checked = 0

	comm_constants = []
	
	while True:
		

		if checked == 0:

			print('communicator opening up')
			print('Please provide these details')
			account_sid = input('Insert your account id: ')
			auth_token = input('insert your auth token: ')
			phone_state = input('Do you wish to turn the phone on? y or n: ')

			if phone_state == "y":
				thread.start()
				toneDialThread.start()
				sender = input('Please input senders number: ')
				recipient = input('Enter the number you wish to send to: ')
				dialer.terminate()
				
			comm_constants.append(account_sid)
			comm_constants.append(auth_token)
			comm_constants.append(recipient)
			comm_constants.append(sender)
			


			checked = 1
			
		else:
			
			message = input('Write your message: ')

			comm = Communicator(message, comm_constants[0], comm_constants[1], comm_constants[2], comm_constants[3])

			comm.display_data()

			## Read message to user
			comm.confirmation()

			confirm = input('Send another message to the same recipient? y or n')
			if confirm == "y":
				pass
			else:
				break
		 

if __name__ == "__main__":
	main()