import tkinter as tk
import random
import time

# Creates Window
window = tk.Tk()
window.title("Sorting Algorithms")
window.minsize(1000, 600)
window.maxsize(1000, 600)
window.columnconfigure(0, weight = 1)
window.rowconfigure(0, weight = 0)
window.rowconfigure(1, weight = 2)

# List that is filled with the heights of the rectangles
recHeights = []
# List that is filled with the heights of the random rectangles
randRecHeights = []
# List that is filled with the identifiers for each rectangle
rectangles = []

# Options for sorting methods and chart sizes
sortOptions = ["Bubble", "Quick", "Selection", "Insertion", "Merge"]
chartOptions = ["Tiny", "Small", "Medium", "Large", "Gigantic"]
speedOptions = ["Slow", "Normal", "Fast", "Insane", "Instant"]
wait = .75




def DrawRandomRectangles():
	global randRecHeights
	global rectangles
	rectangles = []
	randRecHeights = []
	num = float(len(recHeights))
	chartCanvas.delete("all")
	recWidth = float((chartCanvas.winfo_width() - 2) / num) # makes length of each rectangle 1/num of total canvas width
	#recHeight = float((chartCanvas.winfo_height() - 2) / num) # makes height of each rectangle 1/num of total canvas height
	start = 0.00 # declares beginning of rectangles (X)
	size = num # used in loop to generate all rectangles
	step = 1.00 # multiples with height/width to ensure each rectangle is flush against each other
	index = 0
	while size > 0:
		randHeight = (recHeights[random.randint(0, len(recHeights) - 1)])
		randRecHeights.append(randHeight)
		recHeights.remove(randHeight)
		a = chartCanvas.create_rectangle(start, randRecHeights[index], (recWidth * step), chartCanvas.winfo_height(), fill = "red")
		rectangles.append(a)
		step += 1 # scales height/width depending on location
		start += recWidth # makes sure each rectangles starts flush against the previous
		index += 1
		size -= 1



##################### SORTING FUNCTIONS #####################

def Bubble(): # bubble sort randrec list
	global rectangles
	global randRecHeights
	print ("Bubble")
	time.sleep(wait)
	BubbleSort(randRecHeights)
	for rectangle in rectangles:
		chartCanvas.itemconfig(rectangle, fill = "green")
		time.sleep(wait)
		window.update()
	print("Done")

def BubbleSort(lst):
	swapped = True
	runs = 0
	while swapped and runs < len(lst):
		swapped = False
		x = 1
		while x < len(lst):
			chartCanvas.itemconfig(rectangles[x], fill = "yellow")     							    # mark the two rectangles being compared as yellow	
			chartCanvas.itemconfig(rectangles[x - 1], fill = "yellow")
			window.update()
			time.sleep(wait)

			if lst[x] > lst[x - 1]:
				swapped = True
				SwapRectangles(x, x - 1, lst)
				lst[x], lst[x - 1] = lst[x - 1], lst[x]
		
			chartCanvas.itemconfig(rectangles[x], fill = "red")     							   		# mark the two rectangles being compared as red	
			chartCanvas.itemconfig(rectangles[x - 1], fill = "red")
			window.update()
			time.sleep(wait)
			x += 1

def SwapRectangles(index1, index2, lst):
	x1, y1, x2, y2 = chartCanvas.coords(rectangles[index1])
	chartCanvas.coords(rectangles[index1], x1, lst[index2], x2, y2)
	x, y, x1, y1 = chartCanvas.coords(rectangles[index2])
	chartCanvas.coords(rectangles[index2], x, lst[index1], x1, y1)
	window.update()


def Quick():
	print ("Quick")
	time.sleep(.75)
	global rectangles
	global randRecHeights
	randRecHeights = QuickSort(randRecHeights)
	print(randRecHeights)
	print("Done")

def QuickSort(lst):
	if len(lst) > 1:
		pivot = 0
		lesser = []
		equal = []
		greater = []

		chartCanvas.itemconfig(rectangles[pivot], fill = "yellow")
		window.update()
		time.sleep(wait)

		x = 0
		while x < len(lst):
			chartCanvas.itemconfig(rectangles[x], fill = "yellow")
			window.update()
			time.sleep(wait)

			if lst[x] < lst[pivot]:
				lesser.append(lst[x])
			elif lst[x] > lst[pivot]:
				greater.append(lst[x])
			else:
				equal.append(lst[x])

			if x != pivot:
				chartCanvas.itemconfig(rectangles[x], fill = "red")
				window.update()
				time.sleep(wait)
			x += 1

		chartCanvas.itemconfig(rectangles[pivot], fill = "red")
		window.update()
		time.sleep(wait)
	else:
		return lst

	return QuickSort(lesser) + equal + QuickSort(greater)



def Selection():
	print ("Selection")
	global rectangles
	global randRecHeights
	SelectionSort(randRecHeights)
	print("Done")

def SelectionSort(lst):
	length = len(lst)
	x = 0
	while x < length: 
		chartCanvas.itemconfig(rectangles[x], fill = "yellow")
		window.update()
		i = x + 1
		minimum = x

		while i < length:
			chartCanvas.itemconfig(rectangles[i], fill = "yellow")
			window.update()
			time.sleep(wait)	

			if lst[minimum] < lst[i]:										# remember, recHeights = distance from top of canvas to top of rectangle, so a larger "recHeight" is a shorter rectangle
				chartCanvas.itemconfig(rectangles[minimum], fill = "red")
				minimum = i
				chartCanvas.itemconfig(rectangles[minimum], fill = "yellow")
				window.update()
				time.sleep(wait)

			if minimum != i:
				chartCanvas.itemconfig(rectangles[i], fill = "red")
				window.update()
				time.sleep(wait)
			i += 1

		if minimum != x:													# swap
			chartCanvas.itemconfig(rectangles[x], fill = "yellow")
			window.update()
			time.sleep(wait)
			SwapRectangles(x, minimum, lst)
			chartCanvas.itemconfig(rectangles[minimum], fill = "red")

		chartCanvas.itemconfig(rectangles[x], fill = "green")
		window.update()
		time.sleep(wait)
		
		lst[x], lst[minimum] = lst[minimum], lst[x] 
		x += 1

def Insertion():
	print ("Insertion")
	global rectangles
	global randRecHeights
	InsertionSort(randRecHeights)
	for rectangle in rectangles:
		chartCanvas.itemconfig(rectangle, fill = "green")
		time.sleep(.1)
		window.update()
	print("Done")

def InsertionSort(lst):
	x = 1
	while x < len(lst):
		key = x
		i = x - 1

		chartCanvas.itemconfig(rectangles[key], fill = "yellow")
		chartCanvas.itemconfig(rectangles[i], fill = "yellow")
		window.update()
		time.sleep(wait)

		while lst[key] > lst[i] and key > 0:
			SwapRectangles(key, i, lst)
			lst[key], lst[i] = lst[i], lst[key]

			chartCanvas.itemconfig(rectangles[key], fill = "red")
			chartCanvas.itemconfig(rectangles[i], fill = "red")
			window.update()

			key -= 1
			i -= 1

			chartCanvas.itemconfig(rectangles[key], fill = "yellow")
			if i >= 0:
				chartCanvas.itemconfig(rectangles[i], fill = "yellow")
			window.update()
			time.sleep(wait)

		chartCanvas.itemconfig(rectangles[key], fill = "red")
		chartCanvas.itemconfig(rectangles[i], fill = "red")
		window.update()
		x += 1
		

def Merge():
	print ("Merge")
	global rectangles
	global randRecHeights
	MergeSort(randRecHeights)
	print("Done")

def MergeSort(lst):
	if len(lst) > 1:
		mid = len(lst) // 2
		leftList = lst[:mid]
		rightList = lst[mid:]

		MergeSort(leftList)
		MergeSort(rightList)

		left = 0	# counter for left list
		right = 0	# counter for right list
		result = 0	# counter for retured (sorted) list

		# iterate through the two lists, and put the greater value of the two compared indexes in the result.
		# Only increment list index when it was the greater value (placed into new list)
		while left < len(leftList) and right < len(rightList): 
			chartCanvas.itemconfig(rectangles[left], fill = "yellow")
			chartCanvas.itemconfig(rectangles[right + mid], fill = "yellow")
			window.update()
			time.sleep(wait)
			if leftList[left] < rightList[right]:
				# need to swap rectangle at 'result' and rectangle and leftList[left]
				lst[result] = leftList[left]
				chartCanvas.itemconfig(rectangles[left], fill = "red")
				chartCanvas.itemconfig(rectangles[right + mid], fill = "red")
				left += 1
			else:
				lst[result] = rightList[right]
				chartCanvas.itemconfig(rectangles[left], fill = "red")
				chartCanvas.itemconfig(rectangles[right + mid], fill = "red")
				right += 1
			result += 1

			window.update()
			time.sleep(wait)
		# if any values are left in either list (one is longer than the other), put them in the resulting list 
		while left < len(leftList):
			lst[result] = leftList[left]
			left += 1
			result += 1

		while right < len(rightList):
			lst[result] = rightList[right]
			right += 1
			result += 1

def SetSpeed(speed):
	if speed == "Slow":
		wait = 1
	elif speed == "Normal":
		wait = .75
	elif speed == "Fast":
		wait = .50
	elif speed == "Insane":
		wait = .25
	elif speed == "Instant":
		wait = 0

# Begins the sorting algorithm
def StartSort():
	SetSpeed(speedVar.get())
	GetRectangles(chartVar.get())     ###### MAY NOT NEED WHEN SORTING IS DONE ######
	DrawRandomRectangles()
	window.update()
	for option in sortOptions:
		if sortVar.get() == option:
			if option == "Bubble": # Bubble Sort
				Bubble()
			elif option == "Quick": # Quick Sort
				Quick()
			elif option == "Selection": # Selection Sort
				Selection()
			elif option == "Insertion": # Insertion Sort
				Insertion()
			else:                   # Merge Sort
				Merge()




##################### CHART ROW #####################

# Frame that will house the sorting chart
chartFrame = tk.Frame(master = window, bg = "gray20", height = 50, width = 50, relief = "groove", bd = 5)
# Makes a row and column in frame so that the canvas can adjust with the size of the window
chartFrame.rowconfigure(0, weight = 1)
chartFrame.columnconfigure(0, weight = 1)
# Places frame in the WINDOWS row 1 and column 0
chartFrame.grid(row = 1, column = 0, sticky = "nsew")
# Create canvas to house bars
chartCanvas = tk.Canvas(master = chartFrame, bg = "gray20", highlightthickness = 0)
# Places canvas in CHARTFRAME row 0 and column 0
chartCanvas.grid(row = 0, column = 0, sticky = "NSEW")




# Draws the rectangles in order based on the chart size
# num = number of rectangles
def DrawRectangles(num):
	global recHeights
	recHeights = []
	num = float(num)
	chartCanvas.delete("all")
	recWidth = float((chartCanvas.winfo_width() - 2) / num) # makes length of each rectangle 1/num of total canvas width
	recHeight = float((chartCanvas.winfo_height() - 2) / num) # makes height of each rectangle 1/num of total canvas height
	start = 0.00 # declares beginning of rectangles (X)
	size = num # used in loop to generate all rectangles
	step = 1.00 # multiples with height/width to ensure each rectangle is flush against each other
	while size > 0:
		chartCanvas.create_rectangle(start, chartCanvas.winfo_height() - recHeight * step, (recWidth * step) + 2, chartCanvas.winfo_height(), fill = "red")
		recHeights.append(chartCanvas.winfo_height() - (recHeight * step)) # Accumulates the height of each rectangle for sorting
		step += 1 # scales height/width depending on location
		start += recWidth # makes sure each rectangles starts flush against the previous
		size -= 1
	recHeights.reverse() # makes sure heights are in order of rectangles (increasing)



# Uses the selected chart size to determine # of rectangles, then calls DrawRectangles to draw them all
def GetRectangles(size):
	recWidth = 0
	recHeight = 0
	# Create rectangles based on size chose by user:
	for option in chartOptions:
		if size == option:
			if option == "Tiny": # 10 rectangles
				DrawRectangles(10)
			elif option == "Small": # 20 rectangles
				DrawRectangles(20)
			elif option == "Medium": # 30 rectangles
				DrawRectangles(30)
			elif option == "Large": # 50 rectangles
				DrawRectangles(50)
			else:                   # 100 rectangles
				DrawRectangles(100)






##################### CONTROL ROW #####################

# Create frame that will house the controls
controlFrame = tk.Frame(master = window, height = 50, width = 50, relief = "groove", bd = 5, bg = "gray29")

# Create 3 columns; one for each control. Ensures each widget is equidistant and moves in unison
controlFrame.columnconfigure(0, weight = 1, minsize = 100)
controlFrame.columnconfigure(1, weight = 1, minsize = 100)
controlFrame.columnconfigure(2, weight = 1, minsize = 100)
controlFrame.columnconfigure(3, weight = 1, minsize = 100)
controlFrame.rowconfigure(0, weight = 0, minsize = 50)

# Creates drop down menu for sorting algorithms
sortVar = tk.StringVar() #established string variable
sortVar.set(sortOptions[0]) #sets first selected variable
controlSortOption = tk.OptionMenu(controlFrame, sortVar, *sortOptions)
controlSortOption.config(bg = "gray29")

# Creates drop down for size of chart (number of columns)
chartVar = tk.StringVar() #established string variable
chartVar.set(chartOptions[0]) #sets first selected variable
controlChartOption = tk.OptionMenu(controlFrame, chartVar, *chartOptions, command = GetRectangles)
controlChartOption.config(bg = "gray29")

# Creates drop down for speed of sort
speedVar = tk.StringVar() # established string variable
speedVar.set(speedOptions[0]) # sets first selected variable
controlSpeedOption = tk.OptionMenu(controlFrame, speedVar, *speedOptions)
controlSpeedOption.config(bg = "gray29")

# Button that starts sort when clicked
controlButton = tk.Button(master = controlFrame, text = "SORT", command = StartSort, width = 10, highlightbackground = "gray29")

# Place each item in CONTROLFRAMES rows and columns
controlSortOption.grid(row = 0, column = 0)
controlChartOption.grid(row = 0, column = 1)
controlSpeedOption.grid(row = 0, column = 2)
controlButton.grid(row = 0, column = 3)

# Places frame in WINDOWS row0 column0
controlFrame.grid(row = 0, column = 0, sticky = "nsew")






window.update()
window.lift()
window.attributes('-topmost', True)
window.attributes('-topmost', False)
GetRectangles(chartVar.get())
window.mainloop()