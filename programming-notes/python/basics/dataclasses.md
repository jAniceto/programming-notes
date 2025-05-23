# Dataclasses

Since version 3.7, Python offers data classes. There are several advantages over regular classes or other alternatives like returning multiple values or dictionaries:
- a data class requires a minimal amount of code
- you can compare data classes because `__eq__` is implemented for you
- you can easily print a data class for debugging because `__repr__` is implemented as well
- data classes require type hints, reduced the chances of bugs

Example:

```python
from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str
    
card = Card("Q", "hearts")

print(card == card)
# True

print(card.rank)
# 'Q'

print(card)
Card(rank='Q', suit='hearts')
```
