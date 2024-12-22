Builder design pattern is useful when we need to create an object with step by step optional configurations. If there are two many optional params or configurations that can be set for the class, builder pattern can simplify the object creation.

Example:-
    client = PulsarClinet(pulsar_adrr).with_DLQ(DLQ_name).with_retry(True)...build()



When to use builder pattern
    1. When the object creation is a step by step complex process, which can have different steps based on the requirement.

    2. Avoid telescopic contructors, when the constructor has too many varibales it is good to use builder pattern

    3. When we can have different representations of the same object.
        Luxary house, Simple house, House with a swimming pool, etc
    
    4. For creating immutable objects.