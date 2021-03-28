Pytesseract Code Readme

To use the code, you will need to have some packages installed.

1. Pytesseract: here is a handy Youtube guide to install Pytesseract since we couldn't explain it better ourselves: https://www.youtube.com/watch?v=DG5D8A3zi4o
Do keep in mind that you will need to replace the line "tess.pytesseract.tesseract_cmd = r'{PUT YOUR tesseract.exe DIRECTORY HERE}'",
however if you follow the video you should be fine.

2. cv2: the image processing package. Can be installed using the command "pip install opencv-python" at the command prompt.

3. matplotlib: generally used for data visualization, however in this case it is used to display the output image.
Can be installed using the command "pip install matplotlib" at the command line.

4. pandas: provides DataFrame support. Can be installed using the command "pip install pandas" at the command line.

_________________________________________________________________________________________________________________________

You will need to prepare an image file named 'test.png' and place it in the same directory as the notebook code.
Use your desired paint tool (ie. Microsoft Paint) and draw your desired handwritten digits; this will be the input
into the file. Try to keep the digits of similar size, in a single straight line, and don't write too small for best results.

To run the code just click the cell and press Shift+Enter to run it (unless you have changed the hotkey for whatever reason).
Make sure to run the first cell with the imports, then the second cell which will read in your test.png file and print 
an output consisting on the interpreted digits, a slice of a DataFrame consisting of the confidence level for the output
and the interpreted text, as well as a matplotlib image with boxes around what Pytesseract considered were individual digits
as well as their interpretation (Sometimes, Pytesseract may group multiple handwritten digits into one box and give a single 
digit output; it isn't perfect yet!)