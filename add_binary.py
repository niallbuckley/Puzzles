carry = 0
        result = ''
        
        a = list(a)
        b = list(b)
        
        max_list = len(a),len(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int (b.pop())

            result += str(carry%2)
            carry //= 2
        return result[::-1]
