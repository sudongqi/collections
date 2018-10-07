def evaluate(expression):
    st, d, tokens = [], {}, ['']

    def getval(x):
        # get binding value or self
        return d.get(x, x)

    def _evaluate(tokens):
        if tokens[0] in ('add', 'mult'):
            tmp = list(map(int, map(getval, tokens[1:])))
            return str(tmp[0] + tmp[1] if tokens[0] == 'add' else tmp[0] * tmp[1])
        else:  # let
            for i in range(1, len(tokens) - 1, 2):
                if tokens[i + 1]:
                    # variable bindings update to global d
                    d[tokens[i]] = getval(tokens[i + 1])
            # let expression don't do anything but return the value of last token
            return getval(tokens[-1])

    for c in expression:
        if c == '(':
            # let expression need to update the variable bindings first, so the inner expression can use them
            if tokens[0] == 'let':
                _evaluate(tokens)
            # st store expression and the current variable bindings
            st.append((tokens, dict(d)))
            tokens = ['']
        elif c == ' ':
            # allocate space for new token for current expression
            tokens.append('')
        elif c == ')':
            # evaluate expression at the end bracket
            val = _evaluate(tokens)
            # retrieve the outer expression
            tokens, d = st.pop()
            # add val to the outer expression
            tokens[-1] += val
        else:
            tokens[-1] += c
    # print(st, tokens)
    return int(tokens[0])


print(evaluate('(let x 2 (mult x 5))'))  # 10
print(evaluate('(mult 3 (add 2 3))'))  # 15
print(evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))'))  # 14
print(evaluate('(let x 1 y 2 x (add x y) (add x y))'))  # 5
