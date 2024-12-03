# ShoppingPrices
*DSA Project 3*

The purpose of this Python Project is to use heaps to gain an understanding about consumer spending. The GUI uses data to retrieve the highest and lowest priced purchases from the shopping data csv in the repository. This is helpful for users to sort and retrieve information about extreme shopping datapoints.

To run the program you must install the **PySimpleGUI** Library.
You must run the file product_UI.py for the application to run.

Once you run the python product_UI.py application you can click two buttons. The Find Lowest Price button will display the details of the order with the lowest price(USD). The Find Highest Price Button will display the details along with the highest price(USD) of the purchase. The details we are displaying are the the Session ID for the purchase, the number of clicks that users made before making that purchase and the page number that the item purchased was on. These details give users more information about the highest and lowest purchases.

The time taken to compile the minheap and maxheap will also be displayed. However, this does not change since the minheap and maxheap are only built once. The purpose of this data is to show the user how long it takes for these structures to be created to compare the two structures for analyzing the two extremes.

### Credits
Sriya Kollipara: Implemented the max heap, built the timer and imported the data.

Amelia Wazio: Made the user interface for the program and debugged.

Shreyas Koduvayur: Implemented the min heap.
