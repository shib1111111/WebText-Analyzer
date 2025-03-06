# WebText Analyzer: Comprehensive Web Content Analysis Tool

The **WebText Analyzer** is a sophisticated Python-based tool designed to extract and analyze textual content from web pages. This project facilitates advanced linguistic analysis, including sentiment analysis, readability metrics, and other key text-derived variables. The tool systematically processes URLs provided in an Excel file, retrieves web content, stores titles and descriptions in text files, and outputs detailed analysis results into a structured Excel file.

---

## Project Overview

The WebText Analyzer automates the following workflow:

1. **Input Processing**: Reads URLs and their identifiers from an Excel file (`Input.xlsx`).
2. **Content Extraction**: Fetches web page content using HTTP requests and parses it to extract titles and descriptions.
3. **Text Storage**: Saves extracted text into individual text files for further processing.
4. **Text Analysis**: Performs linguistic analysis, including sentiment scoring and readability assessments.
5. **Output Generation**: Compiles results into a structured Excel file (`output.xlsx`) based on a predefined format.

This tool is ideal for researchers, marketers, or data analysts seeking to derive actionable insights from web-based textual data.

---

## Prerequisites

To ensure seamless execution, install the following Python libraries:

- **pandas**: Manages tabular data (e.g., Excel files).
- **requests**: Retrieves web page content via HTTP requests.
- **beautifulsoup4**: Parses HTML for content extraction.
- **nltk**: Provides natural language processing capabilities.
- **pyphen**: Calculates syllable counts for readability metrics.

Install these dependencies using pip:

```bash
pip install pandas requests beautifulsoup4 nltk pyphen
```

**Note**: Ensure you have Python 3.x installed, and verify library installations before running the tool.

---

## Required Data Files

Place the following files in the same directory as the script (`analysis.py`):

1. **`analysis.py`**  
   - The core Python script driving the analysis.

2. **`Input.xlsx`**  
   - Contains two columns:
     - **URL_ID**: Unique integer identifier for each URL.
     - **URL**: The web page URL to analyze.
   - Example:
     ```
     | URL_ID | URL                      |
     |--------|--------------------------|
     | 1      | https://example.com/page1|
     | 2      | https://example.com/page2|
     ```

3. **`Output Data Structure.xlsx`**  
   - Defines the output format with:
     - **URL_ID**: Matches the `Input.xlsx` identifiers.
     - Additional columns for analysis results (e.g., sentiment score, readability index).
   - This file serves as a template for the final `output.xlsx`.

4. **`MasterDictionary/positive-words.txt`**  
   - A text file listing positive words (one per line) for sentiment analysis.
   - Example:
     ```
     happy
     great
     excellent
     ```

5. **`MasterDictionary/negative-words.txt`**  
   - A text file listing negative words (one per line) for sentiment analysis.
   - Example:
     ```
     sad
     bad
     terrible
     ```

6. **`StopWords/`**  
   - A directory containing text files of stop words (e.g., "StopWords_Generic.txt").
   - Each file should start with "StopWords" and end with ".txt".
   - Stop words are excluded during text analysis to focus on meaningful content.

**Setup Tip**: Verify that all files are correctly formatted and present before execution to avoid runtime errors.

---

## Execution Steps

1. **Prepare the Environment**:
   - Place `analysis.py` and all required data files in a single directory.
   - Ensure the libraries are installed.

2. **Configure Input**:
   - Populate `Input.xlsx` with URL_IDs and URLs.
   - Define the desired output structure in `Output Data Structure.xlsx`.

3. **Run the Script**:
   - Execute the script via a Python interpreter or IDE:
     ```bash
     python analysis.py
     ```
   - The tool will:
     - Fetch content from each URL.
     - Extract and save titles/descriptions to text files.
     - Analyze the text and compute metrics.
     - Save results to `output.xlsx`.

4. **Review Output**:
   - Check `output.xlsx` for the analysis results, aligned with the structure defined in `Output Data Structure.xlsx`.

---

## Customization and Usage

- **Modifications**: The script includes detailed comments explaining each step. Adjust parameters or analysis logic as needed by editing `analysis.py`.
- **Scalability**: Add more URLs to `Input.xlsx` to analyze larger datasets.
- **Extensibility**: Enhance the tool by integrating additional metrics or analysis types (e.g., keyword frequency, entity recognition).

---

## License

This project is distributed under the [MIT License](LICENSE), offering flexibility for personal and commercial use with proper attribution.

---

## Contact and Support

For questions, feedback, or assistance, feel free to reach out to the project creator. Contributions and suggestions are welcome to enhance the tool’s capabilities.

---

*Designed and developed with passion by Shib Kumar Saraf*  
*Empower your web content analysis with WebText Analyzer!*
