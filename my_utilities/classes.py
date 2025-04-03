class SingletonBase:
    """
    This class can be used as a base class for any concrete singleton.
    Ex.
        class Config(SingletonBase):
            def __init__(self):
                super().__init__()
                self.some_folder_name = ""
        . . .
        config = Config.get_instance()
    """
    _instance = None
    _is_initialize_allowed = False

    def __init__(self):
        """
        __init__() is only allowed to be run when _is_initialize_allowed.
        """
        if not SingletonBase._is_initialize_allowed:
            message = "Only one instance is allowed. Use 'get_instance()'."
            raise RuntimeError(message)
        SingletonBase._is_initialize_allowed = False #No more instantiations allowed.

    @classmethod
    def get_instance(cls):
        """
        Return singleton instance. Instantiate first if needed.
        Args:
            cls Class that is calling get_instance.
        Returns:
            instance of class that is calling get_instance.
        """
        if cls._instance is None:
            SingletonBase._is_initialize_allowed = True #The only allowed case of instantiation.
            SingletonBase._instance = cls()
        return cls._instance