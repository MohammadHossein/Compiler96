

class SymbolTable:
    def __init__(self):
        self.table = self.mktable(None)

    def mktable(self, previous):
        table = Table()
        table.parent = previous
        return table

    def enter(self, table, name, type, offset=None):
        table.items.append(TableItem(name, type, offset, table))

    def addwidth(self, table, width):
        table.header = width

    def enterproc(self, table, name, type, newTable):
        table.items.append(TableProc(name, type, newTable, table))



class Table:
    def __init__(self):
        self.parent = None
        self.header = None
        self.items = []

    def lookup(self, ID):
        for item in self.items:
            if item.name == ID:
                return item.type
        if self.parent is not None:
            return self.parent.lookup(ID)
        raise KeyError('متفیر \"' + ID + '\" تعریف نشده است!')


class TableItem:
    def __init__(self, name, type, offset, table=None):
        self.name = name
        self.type = type
        self.offset = offset
        self.table = table


class TableProc:
    def __init__(self, name, type,  table, parentTable):
        self.name = name
        self.type = type
        self.table = table
        self.parentTable = parentTable
