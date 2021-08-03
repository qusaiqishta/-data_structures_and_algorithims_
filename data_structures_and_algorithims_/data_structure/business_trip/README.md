# Challenge Summary
Write a function Determine whether the trip is possible with direct flights, and how much it would cost.
## Whiteboard Process
![](/images/business_trip.png)
## Approach & Efficiency
Big O of time --> O(n^2) Big O of space --> O(n)
## Solution
```
def business_trip(graph,cities):
    isdirect = True
    cost = 0
    for i in range(len(cities)-1):
        for city in graph.get_neighbors(cities[i]):
            if cities[i+1]==city[0]:
                cost+=city[1]
                break
            else:
                can=False
        
    if isdirect==False:
            cost=0
    
    return isdirect, f'${cost}'

```