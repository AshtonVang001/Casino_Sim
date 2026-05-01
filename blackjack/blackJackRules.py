class Rules:

    def __init__(
        self,
        money,
        deck = ["2(spades)", "2(diamonds)", "2(hearts)", "2(clubs)",
                "3(spades)", "3(diamonds)", "3(hearts)", "3(clubs)",
                "4(spades)", "4(diamonds)", "4(hearts)", "4(clubs)",
                "5(spades)", "5(diamonds)", "5(hearts)", "5(clubs)",
                "6(spades)", "6(diamonds)", "6(hearts)", "6(clubs)",
                "7(spades)", "7(diamonds)", "7(hearts)", "7(clubs)",
                "8(spades)", "8(diamonds)", "8(hearts)", "8(clubs)",
                "9(spades)", "9(diamonds)", "9(hearts)", "9(clubs)",
                "10(spades)", "10(diamonds)", "10(hearts)", "10(clubs)",
                "J(spades)", "J(diamonds)", "J(hearts)", "J(clubs)",
                "Q(spades)", "Q(diamonds)", "Q(hearts)", "Q(clubs)",
                "K(spades)", "K(diamonds)", "K(hearts)", "K(clubs)",
                "A(spades)", "A(diamonds)", "A(hearts)", "A(clubs)"]

    ):
        self.deck = deck
        self.money = money
