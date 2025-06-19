from urllib.parse import urlencode

import gradio as gr
from service.RiskClient import RiskClient
from tab.go import ways, ways_detail
from util import main_request


def function_test_tab():
    with gr.Column():

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
                client = RiskClient(server_url)
                ctoken = client.get_ctoken()
                return f"获取成功: {ctoken}"
            except Exception as e:
                return f"获取失败: {str(e)}"

        ctoken_test_btn.click(
            fn=test_ctoken,
            inputs=[ctoken_server_ui],
            outputs=[ctoken_output_ui]
        )
        with gr.Row():
            gr.Markdown("### 通过验证码测试")
    _request = main_request
    # 验证码选择
    way_select_ui = gr.Radio(
        ways, label="验证码", info="过验证码的方式", type="index", value=ways[0]
    )

    select_way = 0

    def choose_option(way):
        nonlocal select_way
        select_way = way

    way_select_ui.change(choose_option, inputs=way_select_ui, outputs=[])

    test_get_challenge_btn = gr.Button("开始测试")
    test_log = gr.JSON(label="测试结果（显示验证码过期则说明成功）")

    def test_get_challenge():
        test_res = _request.get(
            "https://passport.bilibili.com/x/passport-login/captcha?source=main_web"
        ).json()
        test_challenge = test_res["data"]["geetest"]["challenge"]
        test_gt = test_res["data"]["geetest"]["gt"]
        test_token = test_res["data"]["token"]
        test_csrf = _request.cookieManager.get_cookies_value("bili_jct")
        test_geetest_validate = ""
        test_geetest_seccode = ""
        validator = ways_detail[select_way]
        test_geetest_validate = validator.validate(gt=test_gt, challenge=test_challenge)
        test_geetest_seccode = test_geetest_validate + "|jordan"

        _url = "https://api.bilibili.com/x/gaia-vgate/v1/validate"
        _payload = {
            "challenge": test_challenge,
            "token": test_token,
            "seccode": test_geetest_seccode,
            "csrf": test_csrf,
            "validate": test_geetest_validate,
        }
        test_data = _request.post(_url, urlencode(_payload))
        yield [
            gr.update(value=test_data.json()),
        ]

    test_get_challenge_btn.click(
        fn=test_get_challenge,
        inputs=[],
        outputs=[test_log],
    )
