import tess
import gui
import algo

text = tess.read_image("images/wordsearch.png")
word_list = tess.read_image("images/words.png")
word_board, word_list = gui.input_edit(text, word_list)
word_coords = algo.solve(word_board, word_list)
print(word_coords)
gui.output(word_board, word_coords)
