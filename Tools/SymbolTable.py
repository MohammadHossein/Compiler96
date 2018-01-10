class SymbolTable:
    def __init__(self):
        self.table = self.mktable(None)

    @staticmethod
    def mktable(previous):
        table = Table()
        table.parent = previous
        return table

    def addwidth(self, table, width):
        table.header = width


class Table:
    def __init__(self):
        self.parent = None
        self.header = None
        self.items = []

    def enter(self, name, type, offset=None, isParam=False):
        self.items.append(TableItem(name, type, offset, self, isParam))

    def enterproc(self, name, type, newTable):
        self.items.append(TableProc(name, type, newTable, self))

    def lookup(self, ID):
        print(type(self.parent), self.items)
        for item in self.items:
            if item.name == ID:
                return item.type, item.isParam
        if self.parent is not None:
            return self.parent.lookup(ID)
        raise KeyError('متفیر \"' + ID + '\" تعریف نشده است!')

    def lookupStruct(self, ID, struct):
        print(type(self.parent), self.items)
        for item in self.items:
            if item.type == 'struct' and item.name == struct:
                for i in item.table.items:
                    if i.name == ID:
                        return i.type, i.isParam
        raise KeyError('متفیر \"' + ID + '\" تعریف نشده است!')


class TableItem:
    def __init__(self, name, type, offset, table=None, isParam=False):
        self.name = name
        self.type = type
        self.offset = offset
        self.table = table
        self.isParam = isParam


class TableProc:
    def __init__(self, name, type, table, parentTable):
        self.name = name
        self.type = type
        self.table = table
        self.parentTable = parentTable
        self.isParam = False
