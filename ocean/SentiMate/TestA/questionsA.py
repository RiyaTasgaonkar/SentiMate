
questions = [
    'How often do you pitch in your ideas during a brain storming session at your workplace?',
    'Suppose you are with one of your friends and your friend mistreats another person in front of you will you tell them that this is wrong?',
    'Suppose you have a deadline for an assignment today at midnight, what will be your plans for evening?',
    'How efficiently do you plan your day-to-day life?',
    'It is your first day of college you have your first lecture early in the morning. What is your plan?',
    'Your cousins have made a plan for an outing. They ask you will join them or not. What will be your response?',
    'How likely are you to use a use a train service without getting a ticket?',
    'You need to help your friend but it will require you to stay up all night. What will you do?',
    'You have an extremely important presentation schedued next day morning which will decide the course of your career. How likely are you to suffer some anxiety?',
    'How often do you look at the mirror to assess yourself?/ How concious are you about your looks?',
    
]

options = [
    ((1,'Very Rarely'), (2,'Often'),(3,'Frequently')),
    ((1,'I will confront him/her'), (2,'I will not say anything to my friend'),(3,'Let him know some time later indirectly that his behaviour was incorrect.')),
    ((1,'Start your assignment then'), (2,'You are almost done but working on some final touches'),(3,'Relax and enjoy a movie as you have already completed it')),
    ((1,'I dont know what I am doing today evening'), (2,'I do plan same events but it it quite possible that i might deviate from my plans'),(3,'I plan everything and manage to complete all activities before deadline.')),
    ((1,'I will prefer to be alone'), (2,'Nah I will  talk to only those who talk to me.'),(3,'Will go and talk to everyone')),
    ((1,'I prefer staying at home'), (2,'Will decide depending on the place and who all are coming'),(3,'Will immediately respond with yes')),
    ((1,'You feel it if okay if you are late or have a valid reason.'), (2,'You have at times but you know that is it the best portrayal of your behaviour'),(3,'Never as you do not believe that is is morally right')),
    ((1,' No I would try to avoid him/her saying I have some other work'), (2,' I will not stay awake the entire night but for some time.'),(3,' Will stay up an entire night for the friend')),
    ((1,'You wont let such thoughts affect you and are completely relaxed.'), (2,'A bit tensed but you know you will manage to give your best'),(3,'You are not at all worried about the big event')),
    ((1,' Not too much but also not much less'), (2,'Rarely '),(3,'Very often')),
]

def get_questions_and_options():
    global questions, options
    return questions, options

