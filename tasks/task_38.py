class Future:
    ### Inits a new not-yet-specified future value
    def __init__(self):
        self.__continuations = []
        
    ### Registers a continuation to run when the flattened future value is ready
    ### Returns the continuation's future result
    def continueWith(self, continuation):
        # remember to run continuation, if result not provided yet
        if self.__continuations != None:
            r = Future()
            self.__continuations.append((continuation, r))
            return r
        
        # automatic flattening
        if isinstance(self.__result, Future):
            return self.__result.continueWith(continuation)

        # run continuation inline when already finished        
        r = Future()
        v = continuation(self.__result)
        r.trySetResult(v)
        return r
    
    ### Sets this future's value, if it has not yet been set.
    ### Causes all registered continuations to be run or handed off.
    def trySetResult(self, result):
        # already set?
        cs = self.__continuations
        if cs == None: return False;
        
        # state transition
        self.__continuations = None
        self.__result = result
        
        # perform or hand-off registered continuations
        for e in cs:
            continuation, future = e
            r = self.continueWith(continuation);
            future.trySetResult(r)
        
        return True
    
    ### Determines if this future has a flattened result yet
    def hasResult(self):
        return self.__continuations == None and (not isinstance(self.__result, Future) or self.__result.hasResult())
    
    ### Gets the flattened result of this future, raising an error if it's not ready yet
    def forceGetResult(self):
        assert self.hasResult() 
        return self.__result if not isinstance(self.__result, Future) else self.__result.forceGetResult()
        
    
f1 = Future()
f2 = Future()
f3 = f1.continueWith(lambda v1: f2.continueWith(lambda v2: v1 + v2))

def out(x): print x
f1.continueWith(lambda x: out("f1's result = " + x))
f2.continueWith(lambda x: out("f2's result = " + x))
f3.continueWith(lambda x: out("f3's result = " + x))

f1.trySetResult(f2)
f2.trySetResult('Hello')

# outputs: 
# f2's result = Hello
# f3's result = HelloHello
# f1's result = Hello