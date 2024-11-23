### What we need to send to other teams:

**Applied AI**  
 - On each turn we send a request to Applied AI for the number of plants that were sprayed and we send that to the REST endpoint immediately and log it in a JSON file


### Other competition notes:  
 - We need to connect a USB to Agrobot so we can record the plants we sprayed as we go. USB must be ready to present to judges when we leave

### Task 3:  
We need to explore an 8mx8m area and map out the coordinates of objects we detect. The objects will be more than one meter apart. When we detect them we need to send their coordinates to a REST API and record it in a USB JSON log file. We will provide a service that Applied AI can message so they can tell us when they see a weed.  
At the end of exploring or after 30 mins we need to send a finished token to the REST Api.
