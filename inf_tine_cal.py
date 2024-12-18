import tkinter as tk
from tkinter import ttk, messagebox
import re
from PIL import Image, ImageTk  # For adding the logo

class InferenceTimeApp:
    """
    A Tkinter-based GUI application for extracting and averaging inference times 
    from user-input text.
    pyinstaller --onefile --windowed --icon=logo.ico inf_tine_cal.py
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Inference Time Processor")
        self.root.geometry("520x650")  # Set window size
        self.root.resizable(False, False)

        # Add a logo to the top
        self.add_logo("D:\project\poc\cal_inf_time\qc.png")  # Replace with your logo file path

        # Title Label
        title_label = ttk.Label(self.root, text="Inference Time Average Calculator",
                                font=("Helvetica", 18, "bold"))
        title_label.pack(pady=10)

        # Separator
        ttk.Separator(self.root, orient="horizontal").pack(fill="x", pady=5)

        # Input Section
        input_label = ttk.Label(self.root, text="Input Text:", font=("Helvetica", 12, "bold"))
        input_label.pack(anchor="w", padx=20, pady=5)

        # Text Input Field
        self.text_input = tk.Text(self.root, height=12, width=60, wrap="word", font=("Arial", 10))
        self.text_input.pack(padx=20, pady=5)

        # Buttons Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        # Process Button
        process_button = ttk.Button(button_frame, text="Calculate Average", command=self.process_text)
        process_button.grid(row=0, column=0, padx=10)

        # Clear Button
        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_input)
        clear_button.grid(row=0, column=1, padx=10)

        # Result Section
        result_label = ttk.Label(self.root, text="Result:", font=("Helvetica", 12, "bold"))
        result_label.pack(anchor="w", padx=20, pady=5)

        self.result_var = tk.StringVar()
        self.result_display = ttk.Label(self.root, textvariable=self.result_var,
                                        font=("Helvetica", 12), foreground="green")
        self.result_display.pack(anchor="w", padx=20, pady=5)

        # Separator
        ttk.Separator(self.root, orient="horizontal").pack(fill="x", pady=10)

        # Footer
        footer_label = ttk.Label(self.root, text="Developed by APT_DSP_ML Team", font=("Helvetica", 10, "italic"))
        footer_label.pack(pady=10)

    def add_logo(self, logo_path):
        """
        Adds a logo image to the top of the application window.
        """
        try:
            image = Image.open(logo_path)
            image = image.resize((120, 120), Image.Resampling.LANCZOS)  # Resize for display
            logo = ImageTk.PhotoImage(image)
            logo_label = ttk.Label(self.root, image=logo)
            logo_label.image = logo  # Keep a reference to avoid garbage collection
            logo_label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Logo Error", f"Failed to load logo: {e}")

    def process_text(self):
        """
        Processes the input text to extract and calculate the average of inference times.
        """
        text = self.text_input.get("1.0", tk.END).strip()  # Retrieve text from input
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text.")
            return

        try:
            inference_times = self.extract_inference_times(text)
            if inference_times:
                average = sum(inference_times) / len(inference_times)
                self.result_var.set(f"Average Inference Time: {average:.2f}")
            else:
                self.result_var.set("No inference times found.")
        except Exception as e:
            messagebox.showerror("Processing Error", f"An error occurred: {e}")

    def clear_input(self):
        """
        Clears the text input field and resets the result.
        """
        self.text_input.delete("1.0", tk.END)
        self.result_var.set("")

    def extract_inference_times(self, text):
        """
        Extracts all inference time values from the provided text.

        Args:
            text (str): The input text.

        Returns:
            list: A list of integers representing the extracted inference times.
        """
        pattern = r"inference time:\s*(\d+)"
        return [int(match) for match in re.findall(pattern, text, re.IGNORECASE)]


if __name__ == "__main__":
    # Root Window
    root = tk.Tk()

    # Create the Application
    app = InferenceTimeApp(root)

    # Start the Application Loop
    root.mainloop()
