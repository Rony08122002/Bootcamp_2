class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_page = 1

    def get_page(self, page_number):
        if page_number < 1 or page_number > self.total_pages():
            return "Invalid page number"
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def total_pages(self):
        return -(-len(self.items) // self.page_size)

    def next_page(self):
        if self.current_page < self.total_pages():
            self.current_page += 1
        return self.get_page(self.current_page)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self.get_page(self.current_page)

    def first_page(self):
        self.current_page = 1
        return self.get_page(self.current_page)

    def last_page(self):
        self.current_page = self.total_pages()
        return self.get_page(self.current_page)

alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabet_list, 4)

print(p.get_page(1))  # ['a', 'b', 'c', 'd']
print(p.next_page())  # ['e', 'f', 'g', 'h']
#ijkl mnop qrst uvwx
print(p.last_page())  # ['y', 'z']
