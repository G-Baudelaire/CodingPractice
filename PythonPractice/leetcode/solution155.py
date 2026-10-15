class MinStack(object):

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._stack += [val]
        if not self._min_stack or val  <= self._min_stack[-1]:
            self._min_stack += [val]

    def pop(self):
        """
        :rtype: None
        """
        val = self._stack.pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_stack[-1]
