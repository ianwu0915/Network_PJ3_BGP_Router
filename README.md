# BGP Router Simplified Overview

This document outlines the design and challenges faced during the development of a basic BGP router. This router is capable of accepting announcements from peer routers, updating its routing table accordingly, broadcasting new routes to peers, managing and compressing the routing table, and forwarding packets to their correct destinations.

## High-Level Approach

### IP Address Handling

To manage IP addresses, including tasks like bit shifting and masking, we developed an `Ip` class. This class handles operations related to IP address manipulation, ensuring efficient and accurate processing.

### Routing Table Format

Initially, we considered using a dictionary to store routing information. However, we realized that a dictionary wouldn't reduce runtime significantly since the router needs to search the routing table for the longest prefix match, which requires iterating through all elements regardless of the data structure used.

### Routing Table Entries

We decided to encapsulate routing information within a `Route` class. This class stores essential data such as network prefix, local preference, AS path, origin, and source of the route. The routing table itself is a list of `Route` objects, allowing easy access to route attributes.

### Aggregation

The `check_aggregation` method within the `Router` class handles route aggregation. It iterates over the routing table, looking for routes that can be combined. When two adjacent routes are found, they are merged into a single route, which is then updated in the routing table. This process repeats until no further aggregation is possible.

### Disaggregation

Conversely, the `disaggregation` method deals with breaking down aggregated routes. It maintains an additional table of non-aggregated routes. When disaggregation is necessary, the method reconstructs the original routing table from this secondary table and then re-applies aggregation where possible to ensure the table remains optimized.

## Project Challenges

### IP Address Longest Prefix Matching

A significant challenge was implementing the longest prefix match for IP addresses, stored as four-element lists. The process involves iterating over the mask and applying the netmask to determine the longest match for a given address.

### Default Route Handling (0.0.0.0/0)

A specific issue encountered involved handling the default route (0.0.0.0/0). Initially, our implementation failed to correctly process this route, mistakingly assigning it a match length of 0, which led to overlooking critical messages. This issue was rectified by adjusting our handling of the default route, ensuring it was correctly considered in our routing decisions.

## Summary

The development of the BGP router presented several challenges, particularly in efficiently managing IP addresses and optimizing the routing table through aggregation and disaggregation. Addressing these challenges required careful consideration of data structures and algorithms, ultimately leading to the successful implementation of a functional BGP router.