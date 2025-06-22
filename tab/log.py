import gradio as gr
import os

from util import LOG_DIR


def read_last_logs(n=1000):
    app_log_path = os.path.join(LOG_DIR, "app.log")
    if not os.path.exists(app_log_path):
        return "No logs found."
    try:
        with open(app_log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(app_log_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    return "".join(lines[-n:])


def log_tab():
    log_textbox = gr.Textbox(label="最近日志", lines=20, interactive=False)
    refresh_btn = gr.Button("刷新日志")
    gr.File(
        label="下载完整日志", value=os.path.join(LOG_DIR, "app.log"), interactive=False
    )

    refresh_btn.click(fn=read_last_logs, inputs=None, outputs=log_textbox)
    timer = gr.Timer(5.0)
    timer.tick(fn=read_last_logs, outputs=log_textbox)