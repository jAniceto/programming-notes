# Abstract classes

Abstract class is an extension of a basic class. Like a basic class, an abstract class has methods and state. Unlike a basic class, it inherits the `ABC` class and has at least one `abstractmethod`. That means we cannot create an instance directly from its constructor. We will create an abstract class and two concrete classes.

## Creating the classes

First let's create an abstract definition of an employee. Any employee can work and relax. The way that one type of employee can work and relax is different from another type of employee.

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return self.name

    @abstractmethod
    def do_work(self):
        """Do something for work."""
        raise NotImplementedError

    @abstractmethod
    def do_relax(self):
        """Do something to relax."""
        raise NotImplementedError
```

Then we can create a concrete definition of an engineer. The Engineer class is concrete because it implements every `abstractmethod` that was not implemented above. Notice that we leverage the parent's constructor when creating this object. We also define `do_refactor` for an engineer, which is something that a manager prefers not to do.

```python
class Engineer(Employee):
    def __init__(self, name, title, skill):
        super().__init__(name, title)
        self.skill = skill

    def do_work(self):
        return f"{self} is coding in {self.skill}"

    def do_relax(self):
        return f"{self} is watching YouTube"

    def do_refactor(self):
        """Do the hard work of refactoring code, unlike managers."""
        return f"{self} is refactoring code"
```

Now we create a oncrete definition of a manager. The Manager class is concrete for the same reasons as the Engineer class is concrete. Notice that a manager has direct reports and has the responsibility of hiring people on the team, unlike an engineer.

```python
class Manager(Employee):
    def __init__(self, name, title, direct_reports):
        super().__init__(name, title)
        self.direct_reports = direct_reports

    def do_work(self):
        return f"{self} is meeting up with {len(self.direct_reports)} reports"

    def do_relax(self):
        return f"{self} is taking a trip to the Bahamas"

    def do_hire(self):
        """Do the hard work of hiring employees, unlike engineers."""
        return f"{self} is hiring employees"
```

## Using the classes

Declare two engineers:

```python
engineer_john = Engineer("John Doe", "Software Engineer", "Android")
engineer_jane = Engineer("Jane Doe", "Software Engineer", "iOS")
```

These engineers are employees but not managers:
```python
assert all(isinstance(engineer, Employee) for engineer in engineers)
assert all(not isinstance(engineer, Manager) for engineer in engineers)
```

Engineers can work, relax and refactor:
```python
assert engineer_john.do_work() == "John Doe is coding in Android"
assert engineer_john.do_relax() == "John Doe is watching YouTube"
assert engineer_john.do_refactor() == "John Doe is refactoring code"
```

Declare manager with engineers as direct reports:
```python
manager_max = Manager("Max Doe", "Engineering Manager", engineers)
```

Managers are employees but not engineers:
```python
assert isinstance(manager_max, Employee)
assert not isinstance(manager_max, Engineer)
```

Managers can work, relax and hire:
```python
assert manager_max.do_work() == "Max Doe is meeting up with 2 reports"
assert manager_max.do_relax() == "Max Doe is taking a trip to the Bahamas"
assert manager_max.do_hire() == "Max Doe is hiring employees"
```
