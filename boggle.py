from boggle_board_randomizer import randomize_board
import tkinter as tk
from boggle_board_randomizer import randomize_board
from helper import *

"""Magic Numbers"""
CANVAS_SIZE = (700,375)
COLOR_1 ="lightblue"
COLOR_2 = "lime green"
BUTTON_HOVER_COLOR = 'lightgreen'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'green3'
BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tk.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}

YES_BUTTON = "YES\nJust saying ...\nit's the best choice !!"
NO_BUTTON = "NO\nI need to leave...\nexams start in one week :'( "
MIN = 3
SEC = 0
POINTS = 0
TYPO = 'Helvetica bold'


class Boogle:
    def __init__(self):
        """this function will initialize all the stuff we need for the tkinter"""
        self.__root = tk.Tk()
        self.__root.title("BoogleGame")
        self.__root.resizable(False, False)
        self.__root.geometry("500x375")
        self.__canvas = tk.Canvas(self.__root, width=CANVAS_SIZE[0], height=CANVAS_SIZE[1])
        self.__canvas.pack()
        self.__img = tk.PhotoImage(file="boogle-1.png")
        self.__photo = tk.PhotoImage(file="button_play.png")
        self.__canvas.create_image(0, 0, anchor=tk.NW, image=self.__img)
        self.__button = tk.Button(self.__root, image=self.__photo, height=35, width=35)
        self.__button.pack()
        self.__button["command"] = lambda: self._destroy()
        self.__button.place(x=170, y=100)
        self.__curr = ""
        self._path = []
        self._sec = SEC
        self._min = MIN
        self._points = POINTS

    def _destroy(self):
        """ this function destroy the canvas"""
        self.__canvas.destroy()
        self.__button.destroy()
        self._start_game()

    def _start_game(self):
        """starting the game !"""
        self.__root.geometry("700x375")
        self._outer_frame = tk.Frame(self.__root, bg=REGULAR_COLOR,
                                     highlightbackground=REGULAR_COLOR,
                                     highlightthickness=5)
        self._outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self._guessed_in_str = "GUESSED WORDS:"
        self._words_guessed_frame = tk.Label(self._outer_frame, text=self._guessed_in_str)
        self._words_guessed_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.__button_1 = tk.Button(height=2, width=5, text="ADD", bg=COLOR_1)
        self.__button_1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.__button_1.place(x=10, y=10)
        self._display_label = tk.Label(self._outer_frame, font=("Courier", 30),
                                       bg=REGULAR_COLOR, width=23, relief="ridge")
        self._display_label.pack(side=tk.TOP, fill=tk.BOTH)
        self._lower_frame = tk.Frame(self._outer_frame)
        self._lower_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self._inf_frame = tk.Frame(self._outer_frame)
        self._inf_frame.pack(fill=tk.BOTH, expand=True)
        # Configure the background
        self._all_words = load_words_lst("boggle_dict.txt")
        self._create_buttons_in_lower_frame()
        self._check_add()
        self._label_timer = tk.Label(self._inf_frame, font=(TYPO, 20), bg=COLOR_1)
        self._label_timer.pack(side=tk.LEFT)
        self._score = tk.Label(self._inf_frame, font=(TYPO, 15),
                               bg=BUTTON_HOVER_COLOR, text=("POINTS :" + "  " + str(self._points) + "  "))
        self._guessed = []
        self._score.pack(side=tk.RIGHT)
        self._update_clock()

    def _check_add(self):
        """
        this function will add the points that were earned during the game in the canvas
        """
        def _is_pressed(*args):

            if is_valid_path(self.board, self._path, self._all_words) and self.__curr not in self._guessed:
                self._points += len(self.__curr) ** 2
                self._score.config(text=("POINTS :" + "  " + str(self._points) + "  "))
                self._guessed.append(self.__curr)
                self._guessed_in_str += "\n" + self.__curr
                self._words_guessed_frame.config(text=self._guessed_in_str)
            self._path = []
            self.__curr = ""
            self._display_label["text"] = self.__curr

        self.__button_1.bind("<Button-1>", _is_pressed)

    def _update_clock(self):
        """
        this function was made to create a timer that is visible for the player in the tkinter
        :return:
        """
        if self._sec == self._min == 0:
            self._end_option()
        else:
            if self._sec == 0:
                if self._min == 0:
                    pass
                self._sec = 59
                self._min -= 1
            self._sec -= 1
            now = str(self._min) + "min" + " " + str(self._sec) + "sec"
            self._label_timer.configure(text=now)
            self.__root.after(1000, self._update_clock)

    def _end_option(self):
        """ this function is responsible for all the stuff that will be shown in the end of the game in the tkinter"""
        self._outer_frame.destroy()
        self.__button_1.destroy()
        self.__canvas_1 = tk.Canvas(self.__root, height=200, width=389)
        self.__canvas_1.pack()
        self.__img_option = tk.PhotoImage(file="option_final.png", height=200, width=389)
        self.__canvas_1.create_image(0, 0, anchor=tk.NW, image=self.__img_option)
        self._frame_option = tk.Frame()
        self._frame_option.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self._label_option = tk.Label(self._frame_option, text="PLAY AGAIN?", font=(TYPO, 35))
        self._label_option.pack()
        self._label_option = tk.Label(self._frame_option, text="Your score in this game was :\n " + "  " +
                                                               str(self._points) + "  ",font = ('italic', 12))
        self._label_option.place(relheight=0.4, relwidth=0.3, relx=0.35, rely=0.6)
        self._button_yes = tk.Button(self._frame_option, text=
        YES_BUTTON, font=('italic', 12),  bg=COLOR_2)
        self._button_yes.place(relheight=0.4, relwidth=0.3, relx=0.7, rely=0.6)
        self._button_no = tk.Button(self._frame_option, text=NO_BUTTON,
                                    font=('italic', 12), bg="red3")
        self._button_no.place(relheight=0.4, relwidth=0.3, relx=0, rely=0.6)

        def _is_pressed_yes(*args):
            """
            if the user wants to play again
            """
            self.__root.destroy()
            Boogle().run()

        def _is_pressed_no(*args):
            """ if the user wants to quit the game"""
            self.__root.destroy()

        self._button_yes.bind("<Button-1>", _is_pressed_yes)
        self._button_no.bind("<Button-1>", _is_pressed_no)

    def _create_buttons_in_lower_frame(self) -> None:
        """this function creates the buttons to be shown in the game"""
        for i in range(4):
            tk.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore
        for i in range(5):
            tk.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore
        self.board = randomize_board()
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self._make_button(self.board[i][j], i, j)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tk.Button:
        """creates the button using all the parameters we gave him"""
        button = tk.Button(self._lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tk.NSEW)

        def _on_enter(*args):
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(*args):
            button['background'] = REGULAR_COLOR

        def _if_pressed(*args):
            self._path.append((row, col))
            self.__curr += button_char
            self._display_label["text"] = self.__curr

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        button.bind("<Button-1>", _if_pressed)
        return button

    # call countdown first time

    def run(self):
        """running the game"""
        self.__root.mainloop()


if __name__ == "__main__":
    Boogle().run()

