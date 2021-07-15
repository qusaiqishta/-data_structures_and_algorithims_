# Hashtables

Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. ... In Python, the Dictionary data types represent the implementation of hash tables.

## Challenge

implement hash table class that contains add , get , has and contains methods


## Approach & Efficiency

for all methods :

- Time complixity: O(N)

- space complixity : O(1)


## API


- hash : Used to generate a memory location (aka array index) from the key

- add :

```
- You have data and it's key
- Use Hash function (algorithm) to generate memory address from the key of data
- Save data on that memory address


```

- get :

```
- You have a key
- Use the Hash function to convert the key into memory address
- Get the data from the memory address


```

- contains :

check if a key is exist in the hashtable or not