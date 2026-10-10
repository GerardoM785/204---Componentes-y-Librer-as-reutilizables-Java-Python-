import tkinter as tk
import re

class ValidatedEntry(tk.Entry):
    
    def __init__(
        self, 
        master=None, 
        pattern=None, 
        valid_color="#ddffdd", 
        invalid_color="#ffdddd", 
        empty_color="white", 
        **kwargs
    ):
        super().__init__(master, **kwargs)
        self._pattern = re.compile(pattern) if pattern else None
        self._valid_color = valid_color
        self._invalid_color = invalid_color
        self._empty_color = empty_color
        
        self._var = tk.StringVar()
        self.configure(textvariable=self._var)
        self._var.trace_add("write", self._on_change)
        self._valid = False

    @property
    def valid(self):
        return self._valid

    def _on_change(self, *args):
        text = self._var.get()
        if self._pattern is None:
            ok = True
        else:
            ok = bool(self._pattern.fullmatch(text))
            
        self._valid = ok
        
        if not text:
            bg = self._empty_color
        elif ok:
            bg = self._valid_color
        else:
            bg = self._invalid_color
            
        self.configure(bg=bg)