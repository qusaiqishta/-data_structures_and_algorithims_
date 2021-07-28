# Hashmap LEFT JOIN
Hashmap LEFT JOIN returns all rows from the left hash table, even if there are no matches in the right hash table. This means that if the ON clause matches 0 (zero) records in the right hash table; the join will still return a row in the result, but with NULL in each column from the right hash table.

This means that a left join returns all the values from the left hash table, plus matched values from the right hash table or NULL in case of no matching join predicate.

## Challenge
Left_join is a function takes two hash tables , returns all key and values from the left one and only the matches values from right one

## Approach & Efficiency
- Big O of time : O(n^2)
## White board
![](/images/left_join_hashTable.png)
- Big O of space : O(n)
## solution

```

hash1.map=None None None None qusai:24
None None asma:28
hash2.map=None None qusai:27  None None omar:33

for item in hash1.map:
        if item: -> item1=[('qusai','23')]
             
            current = item.head 
            while current:
                output+=[[current.value[0],current.value[1]]]
                current=current.next

=> output=[['qusai','23'],['asma','28']]

for item in output:

        if hash2.contains(item[0])==True: chcck if the keys in output exit in hash2.map
            
            item.append(hash2.get(item[0])) => if exit , append the value that it;s key matches with the key in the output to the item
        else:
            item.append(None)
    return f"{output},"    
    ```