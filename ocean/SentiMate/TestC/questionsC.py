questions = {
    'O' : "You and your friend go to a hotel. Your friend is a foodie. He loves trying out new dishes whenever he goes to somewhere new. On placing your order, the waiter mentions that they have the cook’s special dish in addition to the one’s mentioned in the menu. Describe how you will react when your friend asks you to try out the day’s special dish?",
    'C' : "Your best friend has been inviting you over to his house.You have always been excited to visit his place. One day you go to his room, and to your surprise, you find the room absolutely messy and disorganised. Describe your thoughts and actions?",
    'E' : "Your office colleagues invited you to a house party. You expected all your friends and co-workers to be invited. You reach the party and to your surprise you find out none of them made it to the party. Everyone seems to be a stranger to you. Describe yours thoughts and emotions.",
    'A' : "You are always open to your best friend. You share everything with her, tell her about each and every thing in your life. Your best friends birthday is around the corner and everyone planned a secret party for your friend. You have been told not to tell a word about it. Describe how you will act upon it.",
    'N' : "Your unit tests are in a week. You have been preparing for past 1 week for your exams. The syllabus is too heavy yet you try your best to complete majority of the portion. However, your exam does not go well. Describe your emotional state.",
}

def get_keys_for_questions():
    global questions
    return questions.keys()

def get_values_for_questions():
    global questions
    return questions.values()

def get_questions():
    global questions
    return questions