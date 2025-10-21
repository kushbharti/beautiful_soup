<h1>🌐 Web Scraper Pro - GUI Based Web Data Extractor</h1>

<p><strong>Web Scraper Pro</strong> is a desktop-based GUI application built with <strong>Python (Tkinter)</strong> that allows users to scrape and extract HTML content from any website with ease.  
Designed with a sleek, modern interface, it helps users visualize and extract text data (like headings, paragraphs, or links) from any webpage in just a few clicks.</p>

<hr>

<h2>📌 Features</h2>
<ul>
  <li>✅ Beautiful, modern Tkinter UI with dark mode styling</li>
  <li>✅ Extract specific HTML tags (e.g., p, h1, div, a, etc.)</li>
  <li>✅ Real-time status and count of extracted elements</li>
  <li>✅ Error handling for invalid URLs, timeouts, or empty pages</li>
  <li>✅ Scrollable text area for extracted results</li>
  <li>✅ Clear input/output buttons for quick resets</li>
  <li>✅ Responsive window resizing and user-friendly interface</li>
</ul>

<h2>🛠 Tech Stack</h2>
<ul>
  <li><strong>Language:</strong> Python 3.8+</li>
  <li><strong>GUI Library:</strong> Tkinter, ttk</li>
  <li><strong>Web Scraping:</strong> BeautifulSoup, Requests</li>
  <li><strong>Styling:</strong> Custom ttk themes and layout design</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
web_scraper_pro/
├── web_scraping_gui.py          # Main Tkinter GUI application
├── home.html                    # Sample HTML file for testing
├── practice_scraper.py          # Script for scraping local HTML
├── site_scraper_books.py        # Script for scraping online website (books.toscrape.com)
├── requirements.txt             # Dependencies list
└── README.md                    # Project documentation
</pre>

<h2>🚀 Installation</h2>
<p><strong>Prerequisites:</strong> Python 3.8+ and pip installed</p>

<pre>
# Clone the repository
git clone https://github.com/your-username/web-scraper-pro.git
cd web-scraper-pro

# Create virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the GUI application
python web_scraping_gui.py
</pre>

<h2>🖥 Usage Guide</h2>
<ol>
  <li>Enter the website URL (e.g., https://example.com)</li>
  <li>Enter the HTML tag you want to extract (e.g., <code>p</code>, <code>h1</code>, <code>a</code>)</li>
  <li>Click <strong>“🚀 Start Scraping”</strong></li>
  <li>View and copy extracted text from the results area</li>
  <li>Use <strong>“🧹 Clear & Back”</strong> to return to the input form</li>
</ol>

<h2>🔍 Example Pages</h2>

<h3>1️⃣ Local HTML Scraping (home.html)</h3>
<p>Extract course names and prices from a local HTML page.</p>

<h3>2️⃣ Online Scraping (books.toscrape.com)</h3>
<p>Fetch book titles, image URLs, and prices from the demo e-commerce website for scraping practice.</p>

<h2>📜 Example Output</h2>
<pre>
[1] Python for Beginners
[2] Python Web Development
[3] Python Machine Learning
</pre>

<h2>🧠 How It Works</h2>
<ul>
  <li><strong>Requests</strong> fetches the webpage HTML.</li>
  <li><strong>BeautifulSoup</strong> parses and finds all the specified HTML tags.</li>
  <li>The extracted content is displayed inside a scrollable text area in the GUI.</li>
</ul>

<h2>🧪 Testing</h2>
<ul>
  <li>Run: <code>python web_scraping_gui.py</code></li>
  <li>Try different websites and HTML tags</li>
  <li>Test error handling by entering invalid URLs</li>
</ul>

<h2>🚧 Future Improvements</h2>
<ul>
  <li>[ ] Add export to CSV/JSON option</li>
  <li>[ ] Support multiple tags at once</li>
  <li>[ ] Add progress bar for large scraping tasks</li>
  <li>[ ] Include proxy and headers support for advanced users</li>
  <li>[ ] Package into an executable (.exe) using PyInstaller</li>
</ul>

<h2>📜 License</h2>
<p>This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.</p>

<h2>👨‍💻 Author</h2>
<p>Developed by <strong>Kush Bharti</strong> for web scraping practice and GUI design learning.</p>
