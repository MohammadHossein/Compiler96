class SymbolTable:
    def __init__(self):
        self.table = self.mktable(None)

    def mktable(self, previous):
        table = Table()
        table.parent = previous
        return table

    def enter(self, table, name, type, offset):
        table.items.append(TableItem(name, type, offset, table))

    def addwidth(self, table, width):
        table.header = width

    def enterproc(self, table, name, newTable):
        table.items.append(TableProc(name, newTable, table))


class Table:
    def __init__(self):
        self.parent = None
        self.header = None
        self.items = []


class TableItem:
    def __init__(self, name, type, offset, table=None):
        self.name = name
        self.type = type
        self.offset = offset
        self.table = table


class TableProc:
    def __init__(self, name, table, parentTable):
        self.name = name
        self.table = table
        self.parentTable = parentTable
