# Exercise 1 Below are two lists convert it into a dictionary keys=keys = ['Ten', 'Twenty', 'Thirty'], values = [10, 20, 
dictionary = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
print(dictionary)

#Exercise 2 
sampleDict = {"class": {
               	 "student" : {
                   		 "name":"Mike",
                   		 "marks":{
                       			 "physics":70,
                      			  "history":80  }
                            	}
                       	 }
             }

#Exercise 3
marks = sampleDict['class']['student']['marks']
marks["mathematics"]= 99
print(sampleDict)

#Exercise 4, Reverse this list
numbers = [100, 200, 300, 400, 500]
numbers.reverse()
print(numbers)

#Exercise 5
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

# Exercise  6. Check if these two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set3 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))

# Exercise 7 Correct this sentence = "One year has {} months, {} weeks and {} days.".format(52, 365, 12)
sentence1 = "One year has {} months, {} weeks and {} days.".format(12, 52, 365)
sentence2 = "One year has {2} months, {0} weeks and {1} days.".format(52, 365, 12)
print(sentence2)
print(sentence1)

#Exercise 8  What is the cube root of 8?
x= 8
print(x**(1/3))

# Exercise 9 
sentence ="Hello from the Other side I must've called a thousand times To tell you I'm sorry for EVERYTHING that I've done But when I call, You never seem to be Home"
capitalize_sentence = sentence.capitalize()
print(capitalize_sentence)

# Exercise 10
arr = ['joyfloyd2@hotmail.com', 'jb23forever@yahoo.com', 'adesade4@gmail.com', 'bimpeadeola@gmail.com', 'harunaik@yahoo.com', 'chikaoluchi@gmail.com', 'sweetheart4eva@hotmail.com', 'fionashrek@gmail.com', 'peace_goodness@hotmail.com']
arr_gmail = arr[2:4]+arr[5:6]+arr[7:8]
print(arr_gmail)