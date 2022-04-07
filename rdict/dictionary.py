import abc


class DictBase(metaclass=abc.ABCMeta):
    """Abstract base class for all dictionaries."""

    @abc.abstractmethod
    def show(self):
        """Show the keyword in dictionary."""
        pass

    @abc.abstractmethod
    def query(self, word):
        """Get the word information from the dictionary."""
        pass
