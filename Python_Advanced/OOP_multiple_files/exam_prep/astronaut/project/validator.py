class Validator:

    @staticmethod
    def is_string_empty(name, class_type):
        if name.strip() == "":
            raise ValueError(f"{class_type} name cannot be empty string or whitespace!")