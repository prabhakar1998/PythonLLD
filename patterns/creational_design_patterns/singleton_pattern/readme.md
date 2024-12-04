# limits the class initialization or object creation to only one object
# Use cases where the object is compute and memory heavy and is expected to get shared by multiple threads concurrently, singleton pattern can be used
# Key use cases are: DB connection

Ways to implement:-
    Eager (Init object at the time of module import)
    Lazy (Init object when required, without thread safety)
    Syncronized (java, adds thread safety that the lock is established before accessing critical section)
    Double locking (most preffered, adds thread safety that the lock is established before accessing and inside critical section)
