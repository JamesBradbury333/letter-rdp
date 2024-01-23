from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Union, List


def main():
    with open("./test.txt", "r") as f:
        source_code = f.read()
    print(source_code)
    for thing in tokenize(source_code):
        print(thing)




# Let x  = 45
# [LetToken, IdentifierToken, EqualsToken, NumberToken]
class TokenType(Enum):
    Number = auto()
    Identifier = auto()
    Equals = auto()
    OpenParen = auto()
    CloseParen = auto()
    BinaryOperator = auto()
    Let = auto()


@dataclass
class Token(ABC):
    @property
    @abstractmethod
    def value(self) -> Union[str, None]:
        pass

    @property
    @abstractmethod
    def value(self) -> TokenType:
        pass


KEYWORDS = {
    "let": TokenType.Let,
}


def token(character: str, type: TokenType) -> TokenType:
    return character, type



def tokenize(source_code: str)-> List[Token]:
    tokens = []
    src = list(source_code)

    while len(src) > 0:
        if src[0] == '(':
            tokens.append(token(src.pop(0), TokenType.OpenParen))
        elif src[0] == ')':
            tokens.append(token(src.pop(0), TokenType.CloseParen))
        elif src[0] == '+' or src[0] == '-':
            tokens.append(token(src.pop(0), TokenType.BinaryOperator))
        elif src[0] == '*' or src[0] == '/':
            tokens.append(token(src.pop(0), TokenType.BinaryOperator))
        elif src[0] == '=':
            tokens.append(token(src.pop(0), TokenType.Equals))
        # handle multi character token
            # string.isalpha(), string.isdigit()
        else:
            # Build number token
            if src[0].isdigit():
                num = ""
                while len(src) > 0 and src[0].isdigit():
                    num = f"{num}{src.pop(0)}"
                tokens.append(token(num, TokenType.Number))
            # Build identity token (key-word or user-defined-var)
            elif src[0].isalpha():
                ident = ""
                while len(src) > 0 and src[0].isalpha():
                    ident = f"{ident}{src.pop(0)}"
                # Check for reserved keywords
                try:
                    reserved = KEYWORDS[ident]
                    tokens.append(token(ident, reserved))
                # If not keyword token is identifier
                except KeyError as e:
                    tokens.append(token(ident, TokenType.Identifier))
            elif src[0].isspace():
                src.pop(0) # Skip a whitespace character
            else:
                raise TypeError(f"Unrecognixed character found in source: {src[0]}")
                # src.pop(0)
    return tokens




if __name__ == "__main__":
    main()