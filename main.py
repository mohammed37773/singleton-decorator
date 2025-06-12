def singleton(cls):
    old_new = object.__new__
    def new_new(cls, *args, **kwargs):
        if not hasattr(cls, "_singleton_instance"): cls._singleton_instance = None
        if type(cls._singleton_instance) == cls:
            return cls._singleton_instance
        cls._singleton_instance = old_new(cls)
        return cls._singleton_instance
    cls.__new__ = new_new
    return cls



