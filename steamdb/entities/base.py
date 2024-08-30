import dataclasses


class BaseModel(object):

    def __snake_to_camel(self, input: str) -> str:
        # Can swap out with more sophisticated implementation if needed
        camel_cased = "".join(x.capitalize() for x in input.lower().split("_"))
        if camel_cased:
            return camel_cased[0].lower() + camel_cased[1:]
        else:
            return camel_cased

    # def __camel_to_snake(self, input: str) -> str:
    #     __camel_to_snake_pattern = re.compile(r"(?<!^)(?=[A-Z])")
    #     return __camel_to_snake_pattern.sub("_", input).lower()

    def to_json(self, include_null=False) -> dict:
        """Converts this to json. Assumes variables are snake cased, converts to camel case.

        Args:
            include_null (bool, optional): Whether null values are included. Defaults to False.

        Returns:
            dict: Json dictionary
        """
        return dataclasses.asdict(
            self,
            dict_factory=lambda fields: {
                self.__snake_to_camel(key): value
                for (key, value) in fields
                if value is not None or include_null
            },
        )

    # @classmethod
    # def from_json(self, cls: Type[T], json: dict) -> T:
    #     """Constructs `this` from given json. Assumes camel case convention is used and converts to camel case.

    #     Args:
    #         json (dict): Json dictionary

    #     Raises:
    #         ValueError: When `this` isn't a dataclass

    #     Returns:
    #         T: New instance
    #     """
    #     if not dataclasses.is_dataclass(cls):
    #         raise ValueError(f"{cls.__name__} must be a dataclass")
    #     field_names = {field.name for field in dataclasses.fields(cls)}
    #     kwargs = {
    #         self.__camel_to_snake(key): value
    #         for key, value in json.items()
    #         if self.__camel_to_snake(key) in field_names
    #     }
    #     return cls(**kwargs)
