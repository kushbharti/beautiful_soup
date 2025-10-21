import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup

class WebScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")
        self.root.configure(bg='#1e1e1e')
        
        # Fixed window size
        self.width = 900
        self.height = 650
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.resizable(False, False)
        
        self.main_frame = tk.Frame(root, bg='#1e1e1e')
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.9, relheight=0.9)
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Dark.TButton',
                       background='#2d2d2d',
                       foreground='#ffffff',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Segoe UI', 10, 'bold'))
        style.map('Dark.TButton',
                 background=[('active', '#3d3d3d')])
        style.configure('Clear.TButton',
                       background='#d93025',
                       foreground='#ffffff',
                       borderwidth=1,
                       font=('Segoe UI', 11, 'bold'))
        style.map('Clear.TButton',
                 background=[('active', '#a52714')])

    def create_widgets(self):
        # Title
        self.title = tk.Label(self.main_frame, text="Web Scraper", 
                         font=('Segoe UI', 20, 'bold'),
                         bg='#1e1e1e', fg='#00ff88')
        self.title.pack(pady=20)
        
        # URL Frame
        self.url_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
        self.url_frame.pack(fill='x', padx=10, pady=10)
        url_label = tk.Label(self.url_frame, text="URL:", 
                             font=('Segoe UI', 11, 'bold'),
                             bg='#1e1e1e', fg='#ffffff')
        url_label.pack(anchor='w')
        self.url_entry = tk.Entry(self.url_frame, font=('Segoe UI', 12),
                                  bg='#2d2d2d', fg='#ffffff',
                                  insertbackground='#ffffff',
                                  relief='flat', bd=2)
        self.url_entry.pack(fill='x', ipady=8, pady=5)

        # Tag Frame
        self.tag_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
        self.tag_frame.pack(fill='x', padx=10, pady=10)
        tag_label = tk.Label(self.tag_frame, text="HTML Tag:", 
                             font=('Segoe UI', 11, 'bold'),
                             bg='#1e1e1e', fg='#ffffff')
        tag_label.pack(anchor='w')
        self.tag_entry = tk.Entry(self.tag_frame, font=('Segoe UI', 12),
                                 bg='#2d2d2d', fg='#ffffff',
                                 insertbackground='#ffffff',
                                 relief='flat', bd=2)
        self.tag_entry.pack(fill='x', ipady=8, pady=5)
        self.tag_entry.insert(0, "p")

        # Buttons Frame
        self.btn_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
        self.btn_frame.pack(pady=20)
        self.submit_btn = ttk.Button(self.btn_frame, text="Submit",
                                     style='Dark.TButton',
                                     command=self.submit_action)
        self.submit_btn.pack(side='left', padx=10, ipadx=20, ipady=5)

        self.clear_btn = ttk.Button(self.btn_frame, text="Clear",
                                    style='Clear.TButton',
                                    command=self.clear_action)
        self.clear_btn.pack(side='left', padx=10, ipadx=20, ipady=5)

        # Result Frame (initially hidden)
        self.result_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
        self.result_frame.pack_forget()
        self.result_label = tk.Label(self.result_frame, text="Scraped Content:",
                                     font=('Segoe UI', 12, 'bold'),
                                     bg='#1e1e1e', fg='#00ff88')
        self.result_label.pack(anchor='w', pady=5)

        self.result_text = scrolledtext.ScrolledText(self.result_frame,
                                                     font=('Segoe UI', 12),
                                                     bg='#252525',
                                                     fg='#ffffff',
                                                     insertbackground='#ffffff',
                                                     relief='flat',
                                                     wrap='word')
        self.result_text.pack(fill='both', expand=True)
        self.result_text.tag_configure('number', foreground='#00d6d6', font=('Segoe UI', 12, 'bold'))
        self.result_text.tag_configure('content', foreground='#fff', font=('Segoe UI', 12, 'bold'))

    def submit_action(self):
        url = self.url_entry.get().strip()
        tag = self.tag_entry.get().strip()

        # Validation: URL must be non-empty and should look like a web address
        if not url:
            messagebox.showerror("Input Error", "URL field cannot be empty.")
            return
        if not ((url.startswith("http://") or url.startswith("https://")) and "." in url):
            messagebox.showerror("Input Error", "Please enter a valid URL (starting with http:// or https://).")
            return

        # Validation: tag must be non-empty and contain only letters or numbers
        if not tag:
            messagebox.showerror("Input Error", "HTML Tag field cannot be empty.")
            return
        if not tag.isalnum():
            messagebox.showerror("Input Error", "HTML Tag can only contain letters and numbers (e.g., div, p, h1).")
            return

        # Hide inputs and submit button, show result area
        self.url_frame.pack_forget()
        self.tag_frame.pack_forget()
        self.submit_btn.pack_forget()
        self.clear_btn.pack(side='left', padx=10, ipadx=20, ipady=5)
        self.result_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Scraping...\n\n")
        self.root.update()

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.find_all(tag)

            self.result_text.delete(1.0, tk.END)
            if elements:
                for i, elem in enumerate(elements, 1):
                    self.result_text.insert(tk.END, f"[{i}] ", 'number')
                    self.result_text.insert(tk.END, elem.get_text(strip=True) + '\n\n', 'content')
            else:
                self.result_text.insert(tk.END, f"No <{tag}> tags found on this page.", 'content')
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}", 'content')

    def clear_action(self):
        self.url_frame.pack(fill='x', padx=10, pady=10)
        self.tag_frame.pack(fill='x', padx=10, pady=10)
        self.submit_btn.pack(side='left', padx=10, ipadx=20, ipady=5)

        self.result_frame.pack_forget()
        self.url_entry.delete(0, tk.END)
        self.tag_entry.delete(0, tk.END)
        self.tag_entry.insert(0, "p")
        self.result_text.delete(1.0, tk.END)

    def on_resize(self, event):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperGUI(root)
    root.mainloop()
