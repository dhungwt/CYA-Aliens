print('You are walking along the beach when a UFO crashes near you ')

userinput1 = (input("What do you do? Please enter 'approach' or 'run away' "))

#approach them
if userinput1 == "approach":
  print ("You approach the aliens and they gesture towards their ship. Looks like you're going up! \n Now that you're on board the ship, it looks like the aliens want to chat! Oooh and one of them is kinda flirty! ")
  userinputA = (input("What should you do? Please enter 'Reciprocate' or 'Reject' "))
  if userinputA == "Reciprocate":
    print ("You tell the alien they have beautiful eyes, all 16 of them. The aliens gets on one knee and asks you to marry them. ")
  elif userinputA == "Reject":
    print ("The alien's feelings are hurt and they zap you in retaliation! GAME OVER ")
  userinputB = (input("What should you do? Please enter 'Marry them' or 'Escape'"))
  if userinputB == "Marry them":
      print ("You have a beautiful Spring wedding and honeymoon on the rings of Saturn. HAPPILY EVER AFTER! GAME WON! ")
  elif userinputB == "Escape":
    print ("You manage to go home in an escape pod but you hurt the feelings of the aliens. They invade Earth as revenge! ")
elif userinput1 == 'run away':
  print('The Aliens starts chasing you.')
  userinput2 = (input("What do you do? Please enter 'pick up a stick' or 'pick up a rock'"))
  if userinput2 == "pick up a stick":
    print("You jab one of them with a stick. They become aggravated and run at you. Which ends with the Aliens taking over Earth. GAME OVER")
  else:
    print('You have defeated the aliens and donate their bodies to science. This ends up being the cure to cancer. GAME WON')


  
#run away path

