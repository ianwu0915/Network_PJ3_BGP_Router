# BGP Router
This is a representation of a simple BGP router. 
This router can accept the other router's announcement and update its routing table accordingly, generate and podcast 
new route to your peer router, managing and compress the routing table, forwarding packet to the correct destination.
## High Level Approach
### Ip address
In order to handle the ip for the masking and combination, we create a Ip class to do the operation of bit shifting and masking.
### Decide the format of the routing table
For the routing table, we first thought we can use dictionary to store the route. However, we then realize that the dictionary will not cut down on the runtime.
The router will have to run through the routing table to find the longest match of the
network prefix, so the use of the dictionary will not save the run time if we need to run through all the 
element.

### The entry of the routing table
We choose to build the entry of the routing table a class named Route.

### Aggregation


## Challenge of the project
### Ip address longest prefix
### Test 5-1
### Aggregation
### Disaggregate