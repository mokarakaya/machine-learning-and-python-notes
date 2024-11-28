from collections import defaultdict

from abc import ABC, abstractmethod

"""
Implement two classes on sparse matrices where:
- the first class implements dot product.
- the second class implements element-wise product.

- Leverage abstract classes where possible.
"""

first_matrix = [
    [1, 0, 2],
    [0, 3, 0],
    [0, 0, 4]
]

second_matrix = [
    [5, 0, 0, 1],
    [0, 6, 0, 1],
    [0, 0, 7, 1]
]

second_matrix2 = [
    [5, 0, 0],
    [0, 6, 0],
    [0, 0, 7]
]

response = [
    [5, 0, 14],
    [0, 18, 0],
    [0, 0, 28]
]


# mXn , nXk = mXk

class Product(ABC):
    def __init__(self):
        self.first_row2col = None
        self.second_row2col = None
        self.first_col2row = None
        self.second_col2row = None
        self.result_matrix = None

    def _init_result_matrix(self, first_matrix, second_matrix):
        row_count = len(first_matrix)
        col_count = len(second_matrix[0])
        self.result_matrix = [[0 for _ in range(col_count)] for _ in range(row_count)]

    def index_data(self, first_matrix, second_matrix):
        self._check_matrix(first_matrix, second_matrix)
        self.first_row2col, self.first_col2row = self._make_sparse(first_matrix)
        self.second_row2col, self.second_col2row = self._make_sparse(second_matrix)
        self._init_result_matrix(first_matrix, second_matrix)

    def _make_sparse(self, matrix):
        row2col = defaultdict(lambda: defaultdict(int))
        col2row = defaultdict(lambda: defaultdict(int))
        for idx1, row in enumerate(matrix):
            for idx2, num in enumerate(row):
                if num == 0:
                    continue
                row2col[idx1][idx2] = num
                col2row[idx2][idx1] = num
        return row2col, col2row

    @abstractmethod
    def _check_matrix(self, matrix, matrix2):
        pass

    @abstractmethod
    def multiply(self):
        pass


class DotProduct(Product):
    def _check_matrix(self, first_matrix, second_matrix):
        if not len(first_matrix[0]) == len(second_matrix):
            raise ValueError("First matrix and second matrix must have same length")

    def _calculate(self, first_values, second_values):
        total = 0
        for key, value in first_values.items():
            total += second_values[key] * value
        return total

    def multiply(self):
        for first_key, first_values in self.first_row2col.items():
            for second_key, second_values in self.second_col2row.items():
                total = self._calculate(first_values, second_values)
                self.result_matrix[first_key][second_key] = total
        return self.result_matrix


class ElementWiseProduct(Product):
    def __init__(self):
        super().__init__()

    def _check_matrix(self, first_matrix, second_matrix):
        if not len(first_matrix[0]) == len(second_matrix[0]) or not len(first_matrix[1]) == len(second_matrix[1]):
            raise ValueError("First matrix and second matrix must have same length")

    def multiply(self):
        for first_key, first_values in self.first_row2col.items():
            for key, value in first_values.items():
                self.result_matrix[first_key][key] = value * self.second_row2col[first_key][key]
        return self.result_matrix


dot_product = DotProduct()
dot_product.index_data(first_matrix, second_matrix)
print(dot_product.multiply())

element_wise_product = ElementWiseProduct()
element_wise_product.index_data(first_matrix, second_matrix2)
print(element_wise_product.multiply())
