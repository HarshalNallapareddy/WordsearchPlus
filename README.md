# WordsearchPlus
A python script to solve wordsearch puzzles, fitted with Pytesseract OCR and Tkinter GUI. What initialy began as a simple, console-based, class project became a personal side project with periodic developments. 
<hr>

<h2>Input</h2>
WordsearchPlus takes 2 PNG images as input, the puzzle grid and the list of words, and uses OpenCV and Pytesseract for image pre-processing and OCR. 

<p align="center">
  <img src="https://github.com/HarshalNallapareddy/WordsearchPlus/blob/main/images/wordsearch.PNG" alt="Wordsearch Grid" width=35% height=auto>
  <img src="https://github.com/HarshalNallapareddy/WordsearchPlus/blob/main/images/words.PNG" alt="Wordsearch Grid" width=auto height=25%>
</p>

The letter grid and word list are displayed on a Tkinter GUI for the user to validate the grid/list and make edits in case the OCR misread any characters. The user also has the ability to add or delete rows and columns of the letter grid as well as add or remove words from the word list. Upon completing all necessary edits (if any), the user submits the grid and list for the algorithm to search for all the words in the grid. The grid is displayed again but with the words highlighted in the grid. 

<p align="center">
  <img src="https://github.com/HarshalNallapareddy/WordsearchPlus/blob/main/images/InputGUI.PNG" alt="Input GUI" width=60% height=auto>
</p>

<b>Points of Improvement:</b>
<ul>
  <li>Add a layer of ML to extract the letter grid and word list from a single image
</ul>
<h2>Search Algorithm</h2>
The search aglorithm traverses through the grid for each word in the list. When the first letter of the word is encountered, the algorithm checks the surrounding letters and seeks the rest of the word. 

https://github.com/HarshalNallapareddy/WordsearchPlus/blob/0c088a8ec7dd303feafeae1313e12d689a60f804/algo.py#L8-L27

<b>Points of Improvement:</b>
<ul>
  <li>Clearly, the algorithm is highly inefficient from a time complexity standpoint. Possible improvements could be removing redundant grid traversal.
</ul>
<h2>Output</h2>


<ul>
  <li><b>Point of Improvement:</b>
</ul>
