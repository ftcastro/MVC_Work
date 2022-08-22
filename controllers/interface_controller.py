''' This Module contains meta model for controllers
'''
from views.frame import View
from abc import ABC, abstractmethod


class AbstractController(ABC):
    @abstractmethod
    def bind(view: View):
        raise NotImplementedError
