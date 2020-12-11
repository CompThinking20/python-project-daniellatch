import random
#Purpose of project = To ask the user for a subject (ex. The apple) and a predicate (ex. is red) and create a unnecessarily long sentence (uses Python 3)
# List of possible used terms in the sentence
pre_sub_adj_list = ["individual","singluar","sole","lone","solitary"]
pre_sub_noun_list = ["topic","subject","study","focus","fixation"]
pre_sub_posv_list = ["of the discussion","of this sentence's matter","of the conversation","of the discourse","of the analysis"]
pre_pred_adj_list = ["undoubtly","clearly","absolutely","indisputably","of course"]
pre_pred_adv_list = ["in lack","without","in complete absence","not in need","with no chance"]
pre_pred_posv_list = ["of further required questioning","of a shadow of a doubt","of suspicion","of dispute","of skepticism"]

# Asks for and stores the subject of the sentence
print("What is your subject?")
subject = input("The ")

# Asks for and stores the predicate of the sentence
print("What is your predicate?")
predicate = input("is ")

#This contructs the phrase before the subject
pre_sub = random.choice(pre_sub_adj_list) + " " + random.choice(pre_sub_noun_list) + " " + random.choice(pre_sub_posv_list)

#This contructs the phrase before the predicate
pre_pred = random.choice(pre_pred_adj_list) + " " + random.choice(pre_pred_adv_list) + " " + random.choice(pre_pred_posv_list)

#Contructs the sentence and prints the contructed sentence
print("It is so, that the " + pre_sub + ", the " + subject + "," + " is " + pre_pred + ", " + predicate + ".")
