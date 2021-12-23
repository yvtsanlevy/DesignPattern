The observer pattern is a  design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

The Observer pattern addresses the following problems:

1. A one-to-many dependency between objects should be defined without making the objects tightly coupled.
2. It should be ensured that when one object changes state, an open-ended number of dependent objects are updated automatically.
3. It should be possible that one object can notify an open-ended number of other objects.