# Needed libraries for the program
import csv
import time

# Add file name and declare main variables
fileName = 'e-shop clothing 2008.csv'
prices = []
clicks = []

# Read file and save prices and other data to be displayed in lists
with open(fileName, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for i in reader:
        try:
            price = float(i[11])
            click = int(i[3])
            order_id = i[5]
            page = i[13]
            prices.append((price, click, order_id, page))
        except (ValueError, IndexError):
            continue

# Build maxheap
class MaxHeap:
    def __init__(self):
        self.heap = []

    #Function for insertion into the max heap
    def insert(self, val):
        self.heap.append(val)
        self.bubbleUp(len(self.heap) - 1)

    #Function for extracting the root of the max heap
    def extractMax(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
            
        maxVal = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return maxVal

    #Swaps element with parent to ensure heap properties are met for the max heap
    def bubbleUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i][0] > self.heap[parent][0]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    #Moves element at given index to the correct position to maintain heap properties
    def heapifyDown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapifyDown(largest)

#Start the timer for the max heap build
startMax = time.time();

# Build max heap using functions
maxHeap = MaxHeap()
for price, click, order_id, page in prices:
    maxHeap.insert((price, click, order_id, page))

#End the timer for the max heap build
endMax = time.time();
maxTime = startMax-endMax;

#Ensures that the heap has values and stores the content of the root in the variables designated
if maxHeap.heap:
    maxPrice, maxClicks, order_id, page = maxHeap.extractMax()
else:
    maxPrice, maxClicks, order_id, page = None, None, None, None

#Build minheap
class MinHeap:
    def __init__(self):
        self.heap=[]
        
    #Function for insertion into the min heap
    def insert(self,val):
        self.heap.append(val)
        self.bubbleUp(len(self.heap)-1)

    #Function for deleting the root in the min heap
    def extractMin(self):
        if len(self.heap) ==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        val=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapifyDown(0)
        return val

    #Swaps element with parent to ensure heap properties are met for the min heap
    def bubbleUp(self,index):
        parent=(index-1)//2
        while index>0 and self.heap[index][0]<self.heap[parent][0]:
            self.heap[index],self.heap[parent]=self.heap[parent], self.heap[index]
            index=parent
            parent=(index-1)//2

    #Moves element at given index to the correct position to maintain heap properties
    def heapifyDown(self,index):
        smallest=index
        left= 2*index +1
        right=2 * index +2
        if left<len(self.heap) and self.heap[left][0] <self.heap[smallest][0]:
            smallest=left
        if right<len(self.heap) and self.heap[right][0]<self.heap[smallest][0]:
            smallest=right
        if smallest!= index:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self.heapifyDown(smallest)
            
#Start the timer for finding the time for the min heap
startMin = time.time();

#Construct the min heap
minHeap=MinHeap()
for price, click, order_id, page in prices:
    minHeap.insert((price, click, order_id, page))

#End the timer for finding the time for the min heap
endMin = time.time();
minTime = startMin - endMin;

#Ensures that the heap has values and stores the content of the root in the variables designated
if minHeap.heap:
    minPrice, minClicks, order_id, page = minHeap.extractMin()
else:
    minPrice, minClicks, order_id, page = None, None, None, None
