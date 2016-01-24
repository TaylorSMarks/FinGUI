from unittest import main, TestCase
from entry    import Entry

class TestEvent(TestCase):
    def testDelegate(self):
        class Delegate(object):
            def onChange(self, newValue):
                self.called = True

        e = Entry()
        e.delegate = Delegate()
        e.delegate.called = False
        e.set('Hello World!')
        self.assertTrue(e.delegate.called)

    def testBindToFunction(self):
        def thatWhichMustBeCalled(newValue):
            thatWhichMustBeCalled.called = True

        thatWhichMustBeCalled.called = False
        e = Entry()
        e.bindOnChange(thatWhichMustBeCalled)
        e.set('Hello World!')
        self.assertTrue(thatWhichMustBeCalled.called)

    def testBindToMethod(self):
        class MethodHolder(object):
            def methodThatMustBeCalled(self, newValue):
                self.called = True

        e = Entry()
        methodHolder = MethodHolder()
        methodHolder.called = False
        e.bindOnChange(methodHolder.methodThatMustBeCalled)
        e.set('Hello World!')
        self.assertTrue(methodHolder.called)

    def testSubclass(self):
        class TestEntry(Entry):
            def onChange(self, oldValue, newValue):
                self.called = True

        te = TestEntry()
        te.called = False
        te.set('Hello World!')
        self.assertTrue(te.called)

if __name__ == '__main__':
    main()