# Using difflib in Python for fuzzy string matching
**_Posted on 10 Aug, 2021_**

```
>>> from difflib import get_close_matches                                  
>>> fruits = ["apple", "orange", "banana", "peach"]                        
>>> get_close_matches('app', fruits)                                       
['apple']                                                                  
>>> get_close_matches('aple', fruits)                                      
['apple']                                                                  
>>> get_close_matches('ach', fruits)                                       
['peach']                                                                  
>>> get_close_matches('ba', fruits)                                        
[]                                                                         
>>> get_close_matches('ban', fruits)                                       
['banana']  
```

- A nice use case for this in CLI when a user enter a wrong sub-command, we can suggest or automatically run the correct command
- [`get_close_matches` docs](https://docs.python.org/3.8/library/difflib.html#difflib.get_close_matches)
