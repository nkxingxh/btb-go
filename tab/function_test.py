import gradio as gr
from util.CtokenClient import CtokenClient

def function_test_tab():
    with gr.Column():
        # 原有过码测试功能
        with gr.Row():
            gr.Markdown("### 过码测试")
        with gr.Row():
            test_btn = gr.Button("测试过码", variant="primary")
            test_output_ui = gr.Textbox(label="测试结果", interactive=False)

        # 新增ctoken测试功能
        with gr.Row():
            gr.Markdown("### ctoken获取测试")
        with gr.Row():
            ctoken_server_ui = gr.Textbox(
                label="ctoken服务器地址",
                value="http://localhost:8080",
                placeholder="请输入ctoken服务器地址"
            )
            ctoken_test_btn = gr.Button("测试获取ctoken", variant="primary")
            ctoken_output_ui = gr.Textbox(label="ctoken获取结果", interactive=False)

        # ctoken测试功能逻辑
        def test_ctoken(server_url):
            try:
                client = CtokenClient(server_url)
                ctoken = client.get_ctoken()
                return f"获取成功: {ctoken}"
            except Exception as e:
                return f"获取失败: {str(e)}"

        ctoken_test_btn.click(
            fn=test_ctoken,
            inputs=[ctoken_server_ui],
            outputs=[ctoken_output_ui]
        )
