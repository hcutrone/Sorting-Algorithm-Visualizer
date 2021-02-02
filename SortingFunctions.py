class SortingFunctions:
    def Bubble(): # bubble sort randrec list
        global rectangles
        global randRecHeights
        print ("Bubble")
        lenList = len(randRecHeights)     #lenList = # of rectangles
        index = 1
        x = 0
        while x < lenList:
            swapped = False
            for num in randRecHeights:

                if index == lenList:
                    chartCanvas.itemconfig(rectangles[index - 1], fill = "green")
                    index = 1
                    continue

                chartCanvas.itemconfig(rectangles[index], fill = "yellow")
                chartCanvas.itemconfig(rectangles[index - 1], fill = "yellow")
                window.update()
                time.sleep(0.5)

                if num > randRecHeights[index]:
                    x0, y0, x1, y1 = chartCanvas.coords(rectangles[index - 1])                                                  ## Get coords of first rectangle
                    x2, y2, x3, y3 = chartCanvas.coords(rectangles[index])                                                       #try deleting rectangle and making new one                         ## Get coords of second rectangle
                    chartCanvas.delete(rectangles[index])                                                                       ## Set coords of first rectangle to that of the second
                    chartCanvas.delete(rectangles[index - 1])
                    rectangles[index] = chartCanvas.create_rectangle(x0, y0, x1, y1)                                                ## Set coords of second rectangle to that of the first
                    rectangles[index - 1] = chartCanvas.create_rectangle(x2, y2, x3, y3)
                    rectangles[index], rectangles[index - 1] = rectangles[index - 1], rectangles[index]                         
                    randRecHeights[index], randRecHeights[index - 1] = randRecHeights[index - 1], randRecHeights[index]
                    window.update()
                    swapped = True
                
                chartCanvas.itemconfig(rectangles[index], fill = "red")
                chartCanvas.itemconfig(rectangles[index - 1], fill = "red")
                window.update()
                time.sleep(0.5)

                index += 1
            if swapped == False:
                x += 1
                break
            x += 1
        print("Done")



    def Quick():
        print ("Quick")

    def Selection():
        print ("Selection")

    def Insertion():
        print ("Insertion")

    def Merge():
        print ("Merge")
