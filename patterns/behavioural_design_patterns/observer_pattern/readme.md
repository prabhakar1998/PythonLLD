
Object subject maintains a list of dependent observers to notify them for it's state change.


When to Use the Observer Pattern:

1. When multiple objects need to be notified of an object's state change without tightly coupling them.
2. Decouples the subject and observers.
3. For realtime data updates.


Key Components:
observer(Interface) and observable(Interface)

1. Subject (Observable): The object whose state changes. (It maintains a list of observers.)

2. Observer: The objects that are interested in the changes in the subject. When the subject changes its state, subject notifies all registered observers.

