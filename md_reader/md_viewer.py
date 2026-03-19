import sys
import markdown
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                             QWidget, QFileDialog, QTextBrowser, QHBoxLayout, QLabel)
from PyQt6.QtCore import Qt

class PremiumMarkdownViewerV6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markdown Reader Pro v6.0")
        self.setMinimumSize(1100, 850)
        
        self.is_dark = False
        self.current_content = "" 
        
        self.init_ui()
        self.update_theme()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # --- Toolbar ---
        self.toolbar = QWidget()
        self.toolbar.setFixedHeight(60)
        toolbar_layout = QHBoxLayout(self.toolbar)
        toolbar_layout.setContentsMargins(25, 0, 25, 0)

        self.title_label = QLabel("📄 Markdown Viewer")
        toolbar_layout.addWidget(self.title_label)
        
        toolbar_layout.addStretch()

        self.btn_theme = QPushButton("🌙 Karanlık Mod")
        self.btn_theme.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_theme.setFixedWidth(130)
        self.btn_theme.clicked.connect(self.toggle_theme)
        toolbar_layout.addWidget(self.btn_theme)

        self.btn_sec = QPushButton("📂 Dosya Aç")
        self.btn_sec.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_sec.clicked.connect(self.dosya_ac)
        toolbar_layout.addWidget(self.btn_sec)
        
        self.main_layout.addWidget(self.toolbar)

        # --- Browser ---
        self.browser = QTextBrowser()
        self.browser.setFrameStyle(0)
        self.main_layout.addWidget(self.browser)

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.update_theme()
        if self.current_content:
            self.render_markdown(self.current_content)

    def update_theme(self):
        # Tema Renk Tanımlamaları
        if self.is_dark:
            bg, toolbar_bg, text, border = "#0d1117", "#161b22", "#c9d1d9", "#30363d"
            btn_theme_text = "☀️ Aydınlık Mod"
            btn_style = "background-color: #21262d; color: #c9d1d9; border: 1px solid #30363d;"
        else:
            bg, toolbar_bg, text, border = "#ffffff", "#f6f8fa", "#1f2328", "#d0d7de"
            btn_theme_text = "🌙 Karanlık Mod"
            btn_style = "background-color: #ffffff; color: #24292f; border: 1px solid #d0d7de;"

        self.btn_theme.setText(btn_theme_text)
        self.setStyleSheet(f"background-color: {bg};")
        self.toolbar.setStyleSheet(f"background-color: {toolbar_bg}; border-bottom: 1px solid {border};")
        self.title_label.setStyleSheet(f"color: {text}; font-size: 14px; font-weight: 600; border: none;")
        self.browser.setStyleSheet(f"background-color: {bg}; border: none;")
        
        self.btn_theme.setStyleSheet(btn_style + "border-radius: 6px; padding: 6px; font-size: 12px;")
        self.btn_sec.setStyleSheet("background-color: #2ea44f; color: white; border-radius: 6px; padding: 6px 15px; font-weight: bold; border: none;")

    def dosya_ac(self):
        yol, _ = QFileDialog.getOpenFileName(self, "Markdown Dosyası Seç", "", "Markdown (*.md)")
        if yol:
            with open(yol, "r", encoding="utf-8") as f:
                self.current_content = f.read()
            self.render_markdown(self.current_content)
            self.title_label.setText(f"📄 {yol.split('/')[-1]}")

    def render_markdown(self, content):
        html = markdown.markdown(content, extensions=['extra', 'codehilite', 'sane_lists', 'toc'])
        # HTML'e dinamik CSS enjekte et
        styled_html = f"<html><head>{self.get_styles()}</head><body><div class='wrapper'>{html}</div></body></html>"
        self.browser.setHtml(styled_html)

    def get_styles(self):
        if self.is_dark:
            bg, text, border, code_bg, pre_bg, table_row = "#0d1117", "#c9d1d9", "#30363d", "#21262d", "#161b22", "#161b22"
            h_color, link_color = "#f0f6fc", "#58a6ff"
        else:
            bg, text, border, code_bg, pre_bg, table_row = "#ffffff", "#1f2328", "#d0d7de", "#f6f8fa", "#f6f8fa", "#f6f8fa"
            h_color, link_color = "#1f2328", "#0969da"

        return f"""
        <style>
            body {{ background-color: {bg}; margin: 0; padding: 0; }}
            .wrapper {{
                background-color: {bg}; color: {text};
                padding: 40px 10%; font-family: -apple-system, Segoe UI, Helvetica, Arial, sans-serif;
                line-height: 1.6; font-size: 16px;
            }}
            h1, h2 {{ border-bottom: 1px solid {border}; padding-bottom: 8px; color: {h_color}; font-weight: 600; }}
            h3, h4 {{ color: {h_color}; font-weight: 600; }}
            a {{ color: {link_color}; text-decoration: none; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; border: 1px solid {border}; }}
            th, td {{ border: 1px solid {border}; padding: 12px; text-align: left; }}
            th {{ background-color: {table_row}; font-weight: 600; }}
            tr:nth-child(even) {{ background-color: {table_row}; }}
            code {{ background-color: {code_bg}; padding: 3px 6px; border-radius: 4px; font-family: 'Consolas', monospace; color: {"#ff7b72" if self.is_dark else "#cf222e"}; }}
            pre {{ background-color: {pre_bg}; padding: 16px; border-radius: 8px; border: 1px solid {border}; overflow: auto; }}
            blockquote {{ border-left: 4px solid {border}; padding-left: 16px; color: #8b949e; font-style: italic; }}
            img {{ max-width: 100%; border-radius: 6px; }}
        </style>
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PremiumMarkdownViewerV6()
    window.show()
    sys.exit(app.exec())