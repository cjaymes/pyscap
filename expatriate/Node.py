# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import logging
import math
import re

from .xpath import *

logger = logging.getLogger(__name__)
class Node(object):
    def __init__(self, document, document_order, parent):
        self._document = document
        self._document_order = document_order
        self.parent = parent

    def _tokenize(self, expr):
        tokens = []

        t = ''
        for i in range(len(expr)):
            if len(t) > 0:
                if t[0] in '\'"':
                    # string literal
                    t += expr[i]
                    if expr[i] == t[0] and t[-1] != '\\':
                        tokens.append(t)
                        t = ''
                elif t == '-':
                    tokens.append(t)
                    t = expr[i]
                elif t == '.' and expr[i] != '.':
                    tokens.extend(['self', '::', 'node', '(', ')'])
                    t = expr[i]
                elif re.fullmatch(r'[0-9][0-9.]*', t) and (expr[i].isdigit() or expr[i] == '.'):
                    t += expr[i]
                elif t[0] == '$' and expr[i].isalpha():
                    t += expr[i]
                elif t.isspace():
                    # skip space
                    t = expr[i]
                elif t in ':/.!<>':
                    if t + expr[i] in ['::', '//', '..', '!=', '<=', '>=']:
                        t += expr[i]
                        if t == '//':
                            tokens.extend(['/', 'descendant-or-self', '::', 'node', '(', ')', '/'])
                        elif t == '..':
                            tokens.extend(['parent', '::', 'node', '(', ')'])
                        else:
                            tokens.append(t)
                        t = ''
                    else:
                        tokens.append(t)
                        t = expr[i]
                elif t in '()[]@,\'"*|+=':
                    if t == '@':
                        tokens.extend(['attribute', '::'])
                    else:
                        tokens.append(t)
                    t = expr[i]
                elif expr[i].isalnum() or expr[i] == '-':
                    t += expr[i]
                else:
                    tokens.append(t)
                    t = expr[i]
            else:
                if expr[i].isspace():
                    continue
                t += expr[i]

        # append final token if there is one
        if t == '.':
            tokens.extend(['self', '::', 'node', '(', ')'])
            t = expr[i]
        elif t != '':
            tokens.append(t)

        return tokens

    def xpath(self, expr, version=1.0, variables={}, add_functions={}):
        if version != 1.0:
            raise NotImplementedError('Only XPath 1.0 has been implemented')

        tokens = self._tokenize(expr)
        logger.debug('Tokens: ' + str(tokens))

        functions = Function.FUNCTIONS.copy()
        functions.update(add_functions)

        stack = []
        for i in range(len(tokens)):
            token = tokens[i]

            if token == '(':
                e = Expression()
                logger.debug('Starting sub expression ' + str(e))
                stack.append(e)
            elif token == ')':
                if len(stack) <= 1:
                    continue

                logger.debug('End of ' + str(stack[-1]))
                if i > 0 and tokens[i-1] == '(':
                    # don't add empty Expression
                    stack.pop()
                    logger.debug('Ignoring empty expression')
                elif len(stack) > 1:
                    e = stack.pop()
                    logger.debug('Adding ' + str(e) + ' to ' + str(stack[-1]))
                    stack[-1].children.append(e)
                # else just let it on the stack
            elif token == '[':
                nt = stack.pop()
                stack[-1].children.append(nt)
                p = Predicate()
                stack.append(p)
                logger.debug('Starting predicate ' + str(p))
                e = Expression()
                stack.append(e)
                logger.debug('Starting sub expression ' + str(e))
            elif token == ']':
                logger.debug('End of ' + str(stack[-1]))
                if i > 0 and tokens[i-1] == '[':
                    # don't add empty predicate
                    stack.pop()
                    stack.pop()
                    logger.debug('Ignoring empty expression & predicate')
                else:
                    e = stack.pop()
                    logger.debug('Adding ' + str(e) + ' to ' + str(stack[-1]))
                    stack[-1].children.append(e)
            elif token  == '::':
                # already processed axis
                pass
            elif token  == ':':
                # already processed QNameNodeTest
                pass
            elif token == '*':
                if i > 0 and tokens[i-1] not in [
                    '::', '(', '[', ',', 'and', 'or', 'mod', 'div',
                    '*', '/', '//', '|', '+', '-', '=', '!=', '<', '<=',
                    '>', '>=']:
                    o = Operator(token)
                    o.children.append(stack.pop())
                    stack.append(o)
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                else:
                    if len(stack) == 0 or not isinstance(stack[-1], Axis):
                        # use implicit axis
                        a = Axis('child')
                        stack.append(a)
                        logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                    nt = AnyNodeTest()
                    stack.append(nt)
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif token == ',':
                try:
                    while(not isinstance(stack[-1], Function)):
                        i = stack.pop()
                        logger.debug('Adding ' + str(i) + ' to children of ' + str(stack[-1]))
                        stack[-1].children.append(i)
                except IndexError:
                    raise SyntaxException('Unable to add argument to function')

                logger.debug('Starting new expression ' + str(e) + ' for function argument')
                e = Expression()
                stack.append(e)
                logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif token[0] in '\'"':
                l = Literal(token[1:-1])
                stack.append(l)
                logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif re.fullmatch(r'[0-9.]+', token):
                if '.' in token:
                    l = Literal(float(token))
                else:
                    l = Literal(int(token))

                if len(stack) > 0 and isinstance(stack[-1], Operator):
                    op = stack.pop()
                    op.children.append(l)
                    logger.debug('Added ' + str(l) + ' to children of ' + str(op))
                    stack.append(op)
                else:
                    stack.append(l)
                logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif token in Operator.OPERATORS:
                if token == '-' and ( \
                    len(stack) == 0 \
                    or isinstance(stack[-1], Operator) \
                    or (i > 0 and tokens[i-1] in ('(', ',', '[')) \
                ):
                    o = Operator('negate')
                else:
                    o = Operator(token)
                    o.children.append(stack.pop())
                stack.append(o)
                logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif token == '/':
                if i == 0:
                    s = RootStep(self._document)
                else:
                    while(len(stack) > 1 and not isinstance(stack[-1])):
                        i = stack.pop()
                        logger.debug('Adding ' + str(i) + ' to children of ' + str(stack[-1]))
                        stack[-1].children.append(i)
                    s = Step()
                    i = stack.pop()
                    logger.debug('Adding ' + str(i) + ' to children of ' + str(s))
                    s.children.append(i)
                stack.append(s)
                logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif token == 'Infinity':
                stack.append(Literal(math.inf))
                logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif token == 'NaN':
                stack.append(Literal(math.nan))
                logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
            elif re.fullmatch(r'[a-zA-Z0-9_-]+', token):
                if len(stack) > 0 and isinstance(stack[-1], Axis):
                    if token in TypeNodeTest.NODE_TYPES:
                        stack[-1].children.append(TypeNodeTest(token))
                        logger.debug('Added ' + str(stack[-1].children[-1]) + ' to children of ' + str(stack[-1]))
                    elif len(tokens) > i+1 and tokens[i+1] == ':':
                        stack.append(QNameNodeTest(token))
                        logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                    else:
                        stack[-1].children.append(NCNameNodeTest(token))
                        logger.debug('Added ' + str(stack[-1].children[-1]) + ' to children of ' + str(stack[-1]))
                elif len(tokens) > i+1 and tokens[i+1] == '::' and token in Axis.AXES:
                    a = Axis(token)
                    stack.append(a)
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                elif len(tokens) > i+1 and tokens[i+1] == '(' and token in Function.FUNCTIONS:
                    f = Function(token, functions[token])
                    stack.append(f)
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                elif len(tokens) > i+1 and tokens[i+1] == '(' and token in TypeNodeTest.NODE_TYPES:
                    if len(stack) == 0 or not isinstance(stack[-1], Axis):
                        stack.append(Axis('child'))
                        logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                    nt = TypeNodeTest(token)
                    stack.append(nt)
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                elif token == 'true':
                    stack.append(Literal(True))
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                elif token == 'false':
                    stack.append(Literal(False))
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                elif token in Operator.OPERATORS and i > 0 and tokens[-1] not in [
                    '::', '(', '[', ',', 'and', 'or', 'mod', 'div',
                    '*', '/', '//', '|', '+', '-', '=', '!=', '<', '<=',
                    '>', '>=']:
                    o = Operator(token)
                    o.children.append(stack.pop())
                    stack.append(o)
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                elif len(tokens) > i+1 and tokens[i+1] == ':':
                    # first part of a qname test
                    if len(stack) == 0 or not isinstance(stack[-1], Axis):
                        stack.append(Axis('child'))
                        logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                    nt = QNameNodeTest(token)
                    stack.append(nt)
                    logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                elif i > 0 and tokens[i-1] == ':':
                    if len(stack) == 0 or not isinstance(stack[-1], QNameNodeTest):
                        raise SyntaxException('Expecting QNameNodeTest on stack; got second half of QName')
                    nt = stack.pop()
                    nt.name += ':' + token
                    if len(stack) == 0 or not isinstance(stack[-1], Axis):
                        raise SyntaxException('Expecting Axis on stack; finished QNameNodeTest')
                    stack[-1].children.append(nt)
                    logger.debug('Added ' + str(nt) + ' to ' + str(stack[-1]))
                else:
                    if len(stack) == 0 or not isinstance(stack[-1], Axis):
                        stack.append(Axis('child'))
                        logger.debug('Pushed ' + str(stack[-1]) + ' on stack')
                    nt = NCNameNodeTest(token)
                    stack[-1].children.append(nt)
                    logger.debug('Added ' + str(nt) + ' to children of ' + str(stack[-1]))
            else:
                raise SyntaxException('Unknown token: ' + str(token))

        while(len(stack) > 1):
            i = stack.pop()
            logger.debug('Adding ' + str(i) + ' to children of ' + str(stack[-1]))
            stack[-1].children.append(i)
        i = stack.pop()
        logger.debug('Final pop off stack got ' + str(i))

        # TODO need to make sure node set items are unique
        return i.evaluate(self, 1, 1, variables)

    def __repr__(self):
        return self.__class__.__name__ + ' ' + hex(id(self))

    def get_type(self):
        raise NotImplementedError('get_type has not been implemented in class ' + self.__class__.__name__)

    def escape(self, text):
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        return text

    def unescape(self, text):
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&apos;')
        return text
