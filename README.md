# Text Analysis Tool
This project provides a text analysis tool that performs linguistic analysis on a collection of web pages. It includes sentiment analysis, readability metrics, and other derived variables. The tool reads web page URLs from an Input.xlsx file, fetches the content of each URL, and saves the title and descriptions of each page in separate text files. It then performs text analysis on these text files and saves the results in the **output.csv** file.

## Prerequisites
Before running the code, please make sure the following libraries are installed:

* pandas: For handling data in tabular format.
* requests: For making HTTP requests to fetch web page content.
* beautifulsoup4: For parsing HTML content.
* nltk: The Natural Language Toolkit library for natural language processing.
* pyphen: For counting syllables in words.
You can install these libraries using

```
pip install pandas
pip install requests
pip install beautifulsoup4
pip install nltk
pip install pyphen
```
## **Data Files**
Make sure the following data files are present in the same directory as the code:
  `analysis.py` : the code file..
<u>**Input.xlsx:**</u> This file contains the URL ID and URLs.

<u>**Output Data Structure.xlsx:**</u> This file specifies the output file format.

<u>**MasterDictionary/positive-words.txt:**</u> A text file containing a list of positive words, one word per line.

<u>**MasterDictionary/negative-words.txt:**</u> A text file containing a list of negative words, one word per line.

<u>**StopWords:**</u> A directory containing text files with stop words. Each filename should start with "StopWords" and end with .txt.

## Code Execution
* Place the code file  `analysis.py` in a directory along with the required data files.

* Create an ***Input.xlsx*** file with two columns:

* **URL_ID:** An integer identifier for each URL.
  
* **URL:** The web page URLs to analyze.
  
* Create an **Output Data Structure.xlsx** file with the following columns:
  
    * **URL_ID:** The same integer identifier for each URL as in the ***Input.xlsx*** file.

* Additional columns for storing the computed text analysis variables.

* Please execute the code using a Python interpreter or IDE.

* After execution, the computed text analysis results will be saved in the ***output.xlsx*** file.

## Usage
* Ensure that the code file and data files are set up as described above.
* Run the code by executing the Python script or using an IDE.
* The code will fetch the web page content, perform text analysis, and save the results in the **output.csv** file.
* You can customize the code and parameters as per your requirements.
* Refer to the code comments for detailed explanations of each step.
  
## License
This project is licensed under the MIT License. See the LICENSE file for more information.
