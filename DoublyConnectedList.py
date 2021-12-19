class DoublyConnectedList:
    def __init__(self, list_element_class):
        self.first = list_element_class(None, None)

    is_empty = property(lambda self: self.first.next is None)

    @staticmethod
    def insert_after(element_to_append, element_after):
        element_to_append.next = element_after.next
        element_to_append.previous = element_after
        if element_after.next is not None:
            element_after.next.previous = element_to_append
        element_after.next = element_to_append

    # починить!!!
    @staticmethod
    def insert_before(element_to_append, element_before):
        element_to_append.previous = element_before.previous
        element_to_append.next = element_before
        element_before.previous = element_to_append
        element_before.previous.next = element_to_append

    @staticmethod
    def delete(element):
        # если элемент последний
        if element.next is None:
            element.previous.next = None
        else:
            # если не последний
            element.previous.next = element.next
            element.next.previous = element.previous

    # возвращает объект
    def search(self, key):
        current_element = self.first
        while True:
            if current_element.key == key:
                return current_element
            elif current_element.next is None:
                return False
            current_element = current_element.next

    def __str__(self):
        str_to_return = ''
        current_element = self.first.next
        while current_element is not None:
            str_to_return += current_element.value + ' '
            current_element = current_element.next
        return str_to_return
