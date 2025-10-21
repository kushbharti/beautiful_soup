import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup

class WebScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper Pro")
        self.root.configure(bg='#0a0e27')
        
        # Window setup
        self.width = 850
        self.height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.resizable(True, True)
        self.root.minsize(700, 500)
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Primary button
        style.configure('Primary.TButton',
                       background='#6366f1',
                       foreground='#ffffff',
                       borderwidth=0,
                       focuscolor='none',
                       font=('Inter', 11, 'bold'),
                       padding=(20, 12))
        style.map('Primary.TButton',
                 background=[('active', '#4f46e5'), ('disabled', '#4b5563')])
        
        # Secondary button
        style.configure('Secondary.TButton',
                       background='#1f2937',
                       foreground='#ffffff',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Inter', 11),
                       padding=(20, 12))
        style.map('Secondary.TButton',
                 background=[('active', '#374151')])
        
        # Danger button
        style.configure('Danger.TButton',
                       background='#ef4444',
                       foreground='#ffffff',
                       borderwidth=0,
                       focuscolor='none',
                       font=('Inter', 11, 'bold'),
                       padding=(20, 12))
        style.map('Danger.TButton',
                 background=[('active', '#dc2626')])

    def create_widgets(self):
        # Main container with padding
        self.container = tk.Frame(self.root, bg='#0a0e27')
        self.container.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Header section
        self.create_header()
        
        # Input section
        self.input_container = tk.Frame(self.container, bg='#0a0e27')
        self.input_container.pack(fill='x', pady=(20, 0))
        self.create_input_section()
        
        # Results section (initially hidden)
        self.results_container = tk.Frame(self.container, bg='#0a0e27')
        self.create_results_section()
        
    def create_header(self):
        header_frame = tk.Frame(self.container, bg='#0a0e27')
        header_frame.pack(fill='x')
        
        # Icon/Logo placeholder
        icon_frame = tk.Frame(header_frame, bg='#6366f1', width=50, height=50)
        icon_frame.pack(side='left', padx=(0, 15))
        icon_frame.pack_propagate(False)
        icon_label = tk.Label(icon_frame, text="🌐", font=('Segoe UI', 24),
                             bg='#6366f1', fg='#ffffff')
        icon_label.place(relx=0.5, rely=0.5, anchor='center')
        
        # Title and subtitle
        text_frame = tk.Frame(header_frame, bg='#0a0e27')
        text_frame.pack(side='left', fill='x', expand=True)
        
        title = tk.Label(text_frame, text="Web Scraper Pro", 
                        font=('Inter', 24, 'bold'),
                        bg='#0a0e27', fg='#f9fafb')
        title.pack(anchor='w')
        
        subtitle = tk.Label(text_frame, 
                           text="Extract content from any webpage instantly",
                           font=('Inter', 11),
                           bg='#0a0e27', fg='#9ca3af')
        subtitle.pack(anchor='w', pady=(2, 0))
        
    def create_input_section(self):
        # Card-like container for inputs
        card = tk.Frame(self.input_container, bg='#1f2937', 
                       highlightbackground='#374151', highlightthickness=1)
        card.pack(fill='x', pady=10)
        
        card_inner = tk.Frame(card, bg='#1f2937')
        card_inner.pack(fill='x', padx=25, pady=25)
        
        # URL input
        url_label = tk.Label(card_inner, text="Website URL", 
                            font=('Inter', 12, 'bold'),
                            bg='#1f2937', fg='#f9fafb')
        url_label.pack(anchor='w', pady=(0, 8))
        
        url_frame = tk.Frame(card_inner, bg='#111827', 
                            highlightbackground='#374151', highlightthickness=1)
        url_frame.pack(fill='x', pady=(0, 15))
        
        self.url_entry = tk.Entry(url_frame, font=('Inter', 13),
                                  bg='#111827', fg='#f9fafb',
                                  insertbackground='#6366f1',
                                  relief='flat', bd=0)
        self.url_entry.pack(fill='x', padx=15, pady=12)
        self.url_entry.insert(0, "https://example.com")
        self.url_entry.bind('<FocusIn>', lambda e: self.on_entry_focus(self.url_entry, "https://example.com"))
        self.url_entry.bind('<FocusOut>', lambda e: self.on_entry_unfocus(self.url_entry, "https://example.com"))
        
        # Tag input
        tag_label = tk.Label(card_inner, text="HTML Tag to Extract", 
                            font=('Inter', 12, 'bold'),
                            bg='#1f2937', fg='#f9fafb')
        tag_label.pack(anchor='w', pady=(0, 8))
        
        tag_desc = tk.Label(card_inner, 
                           text="Common tags: p (paragraphs), h1 (headings), div (sections), a (links)",
                           font=('Inter', 10),
                           bg='#1f2937', fg='#9ca3af')
        tag_desc.pack(anchor='w', pady=(0, 8))
        
        tag_frame = tk.Frame(card_inner, bg='#111827',
                            highlightbackground='#374151', highlightthickness=1)
        tag_frame.pack(fill='x')
        
        self.tag_entry = tk.Entry(tag_frame, font=('Inter', 13),
                                 bg='#111827', fg='#f9fafb',
                                 insertbackground='#6366f1',
                                 relief='flat', bd=0)
        self.tag_entry.pack(fill='x', padx=15, pady=12)
        self.tag_entry.insert(0, "p")
        
        # Action buttons
        btn_frame = tk.Frame(self.input_container, bg='#0a0e27')
        btn_frame.pack(pady=20)
        
        self.scrape_btn = ttk.Button(btn_frame, text="🚀  Start Scraping",
                                     style='Primary.TButton',
                                     command=self.submit_action)
        self.scrape_btn.pack(side='left', padx=5)
        
        self.clear_inputs_btn = ttk.Button(btn_frame, text="🗑️  Clear",
                                          style='Secondary.TButton',
                                          command=self.clear_inputs)
        self.clear_inputs_btn.pack(side='left', padx=5)
        
    def create_results_section(self):
        # Status bar
        self.status_frame = tk.Frame(self.results_container, bg='#1f2937',
                                    highlightbackground='#374151', highlightthickness=1)
        self.status_frame.pack(fill='x', pady=(0, 15))
        
        status_inner = tk.Frame(self.status_frame, bg='#1f2937')
        status_inner.pack(fill='x', padx=20, pady=15)
        
        # Left side: status labels
        status_left = tk.Frame(status_inner, bg='#1f2937')
        status_left.pack(side='left', fill='x', expand=True)
        
        self.status_label = tk.Label(status_left, text="✓ Scraping complete",
                                     font=('Inter', 12, 'bold'),
                                     bg='#1f2937', fg='#10b981')
        self.status_label.pack(side='left')
        
        self.count_label = tk.Label(status_left, text="",
                                    font=('Inter', 11),
                                    bg='#1f2937', fg='#9ca3af')
        self.count_label.pack(side='left', padx=(10, 0))
        
        # Right side: Clear button (initially hidden)
        self.clear_output_btn = ttk.Button(status_inner, text="🧹 Clear & Back",
                                           style='Secondary.TButton',
                                           command=self.clear_results_action)
        self.clear_output_btn.pack(side='right')
        self.clear_output_btn.pack_forget()  # hide initially
        
        # Results area
        results_label = tk.Label(self.results_container, text="Extracted Content",
                                font=('Inter', 14, 'bold'),
                                bg='#0a0e27', fg='#f9fafb')
        results_label.pack(anchor='w', pady=(0, 10))
        
        text_frame = tk.Frame(self.results_container, bg='#111827',
                             highlightbackground='#374151', highlightthickness=1)
        text_frame.pack(fill='both', expand=True)
        
        self.result_text = scrolledtext.ScrolledText(text_frame,
                                                     font=('Consolas', 11),
                                                     bg='#111827',
                                                     fg='#e5e7eb',
                                                     insertbackground='#6366f1',
                                                     relief='flat',
                                                     wrap='word',
                                                     padx=15,
                                                     pady=15,
                                                     spacing3=8)
        self.result_text.pack(fill='both', expand=True)
        
        # Tag configurations
        self.result_text.tag_configure('number', foreground='#818cf8', font=('Consolas', 11, 'bold'))
        self.result_text.tag_configure('content', foreground='#e5e7eb', font=('Consolas', 11))
        self.result_text.tag_configure('error', foreground='#f87171', font=('Consolas', 11))
        self.result_text.tag_configure('success', foreground='#34d399', font=('Consolas', 11))
        
    def on_entry_focus(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            
    def on_entry_unfocus(self, entry, placeholder):
        if entry.get().strip() == "":
            entry.insert(0, placeholder)
    
    def copy_results(self):
        content = self.result_text.get(1.0, tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(content)
        messagebox.showinfo("Success", "Results copied to clipboard!")
    
    def submit_action(self):
        url = self.url_entry.get().strip()
        tag = self.tag_entry.get().strip()
        
        if url == "https://example.com":
            url = ""
        
        if not url:
            messagebox.showerror("Missing URL", "Please enter a website URL to scrape.")
            return
        if not ((url.startswith("http://") or url.startswith("https://")) and "." in url):
            messagebox.showerror("Invalid URL", "Please enter a valid URL starting with http:// or https://")
            return
        if not tag:
            messagebox.showerror("Missing Tag", "Please enter an HTML tag to extract.")
            return
        
        self.scrape_btn.config(state='disabled')
        self.root.update()
        
        self.input_container.pack_forget()
        self.results_container.pack(fill='both', expand=True, pady=(20, 0))
        self.clear_output_btn.pack_forget()  # hide clear until done
        
        self.result_text.delete(1.0, tk.END)
        self.status_label.config(text="⏳ Scraping in progress...", fg='#fbbf24')
        self.count_label.config(text="")
        self.root.update()
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.find_all(tag)
            
            self.result_text.delete(1.0, tk.END)
            
            if elements:
                self.status_label.config(text="✓ Scraping complete", fg='#10b981')
                self.count_label.config(text=f"{len(elements)} item(s) found")
                self.clear_output_btn.pack(side='right')  # show clear after success
                
                for i, elem in enumerate(elements, 1):
                    self.result_text.insert(tk.END, f"[{i}] ", 'number')
                    content = elem.get_text(strip=True)
                    if content:
                        self.result_text.insert(tk.END, content + '\n\n', 'content')
                    else:
                        self.result_text.insert(tk.END, "(empty tag)\n\n", 'content')
            else:
                self.status_label.config(text="⚠ No results found", fg='#fbbf24')
                self.count_label.config(text="")
                
        except requests.exceptions.Timeout:
            self.handle_error("Connection timeout.")
        except requests.exceptions.ConnectionError:
            self.handle_error("Connection failed.")
        except requests.exceptions.HTTPError as e:
            self.handle_error(f"HTTP Error: {e}")
        except Exception as e:
            self.handle_error(f"Unexpected error: {str(e)}")
        
        self.scrape_btn.config(state='normal')
    
    def handle_error(self, message):
        self.status_label.config(text="✗ Error occurred", fg='#ef4444')
        self.count_label.config(text="")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, message, 'error')
    
    def clear_inputs(self):
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, "https://example.com")
        self.tag_entry.delete(0, tk.END)
        self.tag_entry.insert(0, "p")
    
    def clear_results_action(self):
        self.results_container.pack_forget()
        self.input_container.pack(fill='x', pady=(20, 0))
        self.result_text.delete(1.0, tk.END)
        self.scrape_btn.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperGUI(root)
    root.mainloop()
