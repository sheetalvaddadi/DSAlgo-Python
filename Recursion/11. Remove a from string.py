class Removea:
    def removal(self, input_str, pointer, result):
        if(pointer<len(input_str)):
            if input_str[pointer] != 'a':
                result+=input_str[pointer]
            return self.removal(input_str, pointer+1, result)
        return result

if __name__ =="__main__":
    r1 = Removea()
    print(r1.removal('aqwsswasswsaaaseesaa', 0, ""))