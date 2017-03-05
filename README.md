# Physical Web Prelims
This repo contains solutions for questions given by Physical Web Mentors.
## Question 1: 
```
Queue

A queue is a particular kind of abstract data type or collection in which the entities in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed.

A basic queue has the following operations:
put: add a new element to the end of the queue.
pop: remove the element from the front of the queue and return it.
peek: returns the element at the head of the queue, without removing it.

We want you to implement a queue with the following operations:
1 x: Enqueue element x into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.

Example:

The first element in the input it is the number of commands that will be processed.
The example below we will have 10 commands: 1 42 → put 42 in the list, 2 → pop the head, etc.

Input
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2

Output
14
14
```
## Question 2
```
Running Median

Given that integers are read from a data stream. Find median of elements read so for in efficient way. The order of the data set must be the order in which the elements are inserted:
When the input size is odd, we take the middle element.
When the set contains an even number of elements, the median is the average of the two middle elements of the sorted sample

Examples:
Odd set [10, 23.33, 6.67] → median is 23.33
9.78 is added. Even set [10, 23.33, 6.67, 9.78] → median is (23.33 + 6.67) / 2 = 15
10 is added. Odd set [10, 23.33, 6.67, 9.78, 10.00] → median is 6.67
3.91 is added. Even set [10, 23.33, 6.67, 9.78, 10.00, 3.91] → median is (6.67 + 9.78) / 2 = 8.23

The first element in the input it is the number of elements that will be added to the set.
The example below we will have 10 elements:
First, 1 will be added and median will be 1.
Then, 2 will be added to the set and the median will be 1.5, etc.

Input
10
1
2
3
4
5
6
7
8
9
10
Output
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
5.5

```
