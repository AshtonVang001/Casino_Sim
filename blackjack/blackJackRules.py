class Rules:

    def __init__(
        self,
        money,
        # deck = ["2(spades)", "2(diamonds)", "2(hearts)", "2(clubs)",
        #         "3(spades)", "3(diamonds)", "3(hearts)", "3(clubs)",
        #         "4(spades)", "4(diamonds)", "4(hearts)", "4(clubs)",
        #         "5(spades)", "5(diamonds)", "5(hearts)", "5(clubs)",
        #         "6(spades)", "6(diamonds)", "6(hearts)", "6(clubs)",
        #         "7(spades)", "7(diamonds)", "7(hearts)", "7(clubs)",
        #         "8(spades)", "8(diamonds)", "8(hearts)", "8(clubs)",
        #         "9(spades)", "9(diamonds)", "9(hearts)", "9(clubs)",
        #         "10(spades)", "10(diamonds)", "10(hearts)", "10(clubs)",
        #         "J(spades)", "J(diamonds)", "J(hearts)", "J(clubs)",
        #         "Q(spades)", "Q(diamonds)", "Q(hearts)", "Q(clubs)",
        #         "K(spades)", "K(diamonds)", "K(hearts)", "K(clubs)",
        #         "A(spades)", "A(diamonds)", "A(hearts)", "A(clubs)"]
        deck = {"2(spades)": 2, "2(diamonds)": 2, "2(hearts)": 2, "2(clubs)": 2,
                "3(spades)": 3, "3(diamonds)": 3, "3(hearts)": 3, "3(clubs)": 3,
                "4(spades)": 4, "4(diamonds)": 4, "4(hearts)": 4, "4(clubs)": 4,
                "5(spades)": 5, "5(diamonds)": 5, "5(hearts)": 5, "5(clubs)": 5,
                "6(spades)": 6, "6(diamonds)": 6, "6(hearts)": 6, "6(clubs)": 6,
                "7(spades)": 7, "7(diamonds)": 7, "7(hearts)": 7, "7(clubs)": 7,
                "8(spades)": 8, "8(diamonds)": 8, "8(hearts)": 8, "8(clubs)": 8,
                "9(spades)": 9, "9(diamonds)": 9, "9(hearts)": 9, "9(clubs)": 9,
                "10(spades)": 10, "10(diamonds)": 10, "10(hearts)": 10, "10(clubs)": 10,
                "J(spades)": 10, "J(diamonds)": 10, "J(hearts)": 10, "J(clubs)": 10,
                "Q(spades)": 10, "Q(diamonds)": 10, "Q(hearts)": 10, "Q(clubs)": 10,
                "K(spades)": 10, "K(diamonds)": 10, "K(hearts)": 10, "K(clubs)": 10,
                "A(spades)": 11, "A(diamonds)": 11, "A(hearts)": 11, "A(clubs)": 11}

    ):
        self.deck = deck
        self.money = money
