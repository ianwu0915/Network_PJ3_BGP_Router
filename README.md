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
This enables the information we need like the network prefix, local preference, AS path, origin, the source of the route
will all attached with route class. The routing table will only be the list of the route class.
We can easily get the attribute inside the route class.

### Aggregation
We use the route class to check if two routes are neighbor and can be aggregation or not.
If two route classes is neighbor, we will aggregate them togather.

### Disaggregate
We use an un-aggregation table to keep track of all the update entry. When disaggregate we will withdraw from the
table and run the loop of the aggregation to see if there are route to be aggregate.



## Challenge of the project
### Ip address longest prefix
The ip address is store in a list of four elements. I need to iterative the mask and apply the net mask to find out the longest
length matching the given address.
### default 0.0.0.0/0
When test the router, we couldn't pass the 5-1 test in quite a while. At first, we thought it was the problem of logic 
that the BGP router to send a data or not is not correct. However, we change to send all the data no matter it is to peer
or customer, the problem still exist. Next, we try if it is the problem in the find best route, but the 5-2 test passed.
We then try to find out all the config file. We found out that there is one route with the netmask of 0.0.0.0/0. We
previous implementation set the matching length as 0, so it would consider there was no route. Thus, we missed two 
message.
### Aggregation
### Disaggregate